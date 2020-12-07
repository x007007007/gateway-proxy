

// Setup context for Storybook here
import 'quasar/dist/quasar.min.css'
import '@quasar/extras/roboto-font/roboto-font.css'
import '@quasar/extras/material-icons/material-icons.css'
import '@quasar/extras/material-icons-outlined/material-icons-outlined.css'

// import 'src/css/app.scss' // if you have an app.scss|sass|styl main file

import Vue from 'vue';
import Vuex from 'vuex';
import Quasar from 'quasar';


Vue.use(Vuex);
Vue.use(Quasar, { config: {}, directives: {} });

export const parameters = {
  actions: { argTypesRegex: "^on[A-Z].*" },
}
