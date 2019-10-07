// Necessary inclusions!
const path = require('path');
const webpack = require('webpack');

// Necessary declarations!
const nodeModulesPath = path.resolve(__dirname, 'node_modules');
// define the entry point for the app to look at when trying to render
const entryPoint = {
    main: './main',
    vendor: ['jquery','react','react-dom','react-router','react-router-dom','styled-components']
}

// This is the information about webpack's output directory and path.
const outputObj = {
    path: path.join(__dirname, '../static'),
    filename: '[name].js',
    publicPath: './public',
    chunkFilename: "[id].js"
};

const clientConfig = {
    context: path.join(__dirname, './'),
    devtool: 'source-map',
    entry: entryPoint,
    output: outputObj,
    node: {
        net: 'empty',
        tls: 'empty',
        dns: 'empty'
    },
    module: {
        rules: [
            // Allows Babel to load
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
            },

            // Essentially allows styling to work
            {
                test: /\.css$/,
                use: [
                    {loader: 'style-loader'},
                    {loader: 'css-loader'}
                ]
            }
        ]
    },
    resolve: {
        // This allows us to require('file') in place of require('file.js')
        extensions: ['.js', '.jsx', '.json', '.css', '.pug']
    },
    optimization: {
        splitChunks: {
            cacheGroups: {
              commons: {
                test: /[\\/]node_modules[\\/]/,
                name: "vendor",
                chunks: "all",
              }
            }
          }
    },
    plugins: [
        //new CleanWebpackPlugin(['source/static'])
        new webpack.ProvidePlugin({
            "$":        "jquery",
            "jQuery":   "jquery"
        })
    ]
}

// Setting Webpack's Configuration
module.exports = clientConfig;
