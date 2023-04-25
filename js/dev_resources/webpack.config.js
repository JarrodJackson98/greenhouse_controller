const HtmlWebpackPlugin = require('html-webpack-plugin');
const ModuleFederationPlugin = require('webpack').container.ModuleFederationPlugin;
const path = require('path');
const ConcatenatePlugin = require('../ConcatPlugin');

module.exports = {
  entry: './src/index',
  mode: 'development',
  target: 'web',
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'),
    },
    port: 3001,
  },
  // output: {
    //publicPath: 'auto',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'main.js',
    },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        options: {
          presets: ['@babel/preset-react'],
        },
      },
    ],
  },
};
