var purify = require('purify-css');
var content = ['jquery-ui.js', 'bootstrap.js', 'script.js', 'index.html'];
var css = ['bootstrap-theme.css','bootstrap.css','style.css']

var options = {
  output: 'style.min.css',

  // Will minify CSS code in addition to purify.
  minify: true,

  // Logs out removed selectors.
  rejected: true
};

purify(content, css, options);