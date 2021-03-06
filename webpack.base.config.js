var path = require('path');
var nodeModulesDir = path.resolve(__dirname, 'node_modules');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = [{
  context: __dirname,
  entry: [
    // defined in local or prod
  ],
  output: {
    // defined in local or prod
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        loaders: [
          'style-loader',
          'css-loader',
          'postcss-loader',
        ],
      },
      {
        test: /\.scss$/,
        loaders: [
          'style-loader',
          'css-loader',
          'postcss-loader',
          'sass-loader',
        ],
      },
      {
        test: /\.(svg)(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url-loader?limit=100000',
      },
      {
        test: /\.(jpg|png)?$/,
        loaders: [
          'file-loader?name=i-[hash].[ext]',
        ],
      },
    ],
  },
  plugins: [
    // defined in local or prod
  ],
  resolve: {
    modules: [
      'node_modules',
      'bower_components',
      path.resolve(__dirname, 'assets/js/'),
    ],
    extensions: ['.js', '.jsx'],
  },
}];
