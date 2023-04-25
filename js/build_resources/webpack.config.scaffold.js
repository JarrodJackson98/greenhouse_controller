
const ModuleFederationPlugin = require('webpack').container.ModuleFederationPlugin;
const deps = require('./build_resources/package.json').dependencies
const path = require('path');
const ConcatPlugin = require('/ConcatPlugin');


module.exports = (entry, ) => {

    return {
  entry: './src/index',
  mode: 'production',
  target: 'web',

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

  plugins: [
    new ModuleFederationPlugin({
      name: 'app4',
      filename: 'remoteEntry.js',
      exposes: {
        './AppTest': './src/AppTest',},
        shared: {
          react: {
            import: 'react', // the "react" package will be used a provided and fallback module
            shareKey: 'react', // under this name the shared module will be placed in the share scope
            shareScope: 'default', // share scope with this name will be used
            singleton: true, // only a single version of the shared module is allowed
          },
          'react-dom': {
            requiredVersion: deps['react-dom'],
            singleton: true, // only a single version of the shared module is allowed
            },
          },
      }),
    new ConcatPlugin({
        source: 'dist',
        destination: 'static1',
        name: 'widget4.js',
        ignore: 'main.js'
      }),
  ],
};
}
