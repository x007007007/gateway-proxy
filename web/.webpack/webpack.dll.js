const path    = require('path');
const webpack = require('webpack');
module.exports = {
  entry: {
      vendor: ['vue', 'quasar']
  },
  output: {
    path: path.resolve('./dist/dll'),
    filename: 'vendor.bundle.js',
    library: 'vendor_library'
  },
  resolve: {
        fallback: {"path": false }  // require.resolve("path-browserify")
  },
  plugins: [
    new webpack.DllPlugin({
      path: path.resolve('./dist', '[name]-manifest.json'),
      name: '[name]_library'
    })
  ]
};
