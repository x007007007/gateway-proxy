import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gateway-proxy",
    version="0.0.1",
    author="xxc",
    author_email="x007007007@hotmail.com",
    description="gateway-proxy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/x007007007/gateway-proxy",
    packages=setuptools.find_packages('src'),
    package_dir={
        '': 'src'
    },
    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "gateway-proxy-admin = gateway_proxy.manage:main",
        ],
    }
)
