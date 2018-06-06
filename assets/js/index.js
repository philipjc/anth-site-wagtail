// import external dependencies
// import 'popper.js'
// import 'imports-loader?jQuery=jquery!bootstrap'

// import local dependencies
import Router from './utils/Router';
import common from './routes/common';
import homepage from './routes/homepage';


/** Populate Router instance with DOM routes */
const routes = new Router({
  // All pages
  common,
  // HomePage
  homepage,
});

// Load Events
// jQuery(document).ready(() => routes.loadEvents());
/** Load Events */
document.addEventListener("DOMContentLoaded", () => {
  // Handler when the DOM is fully loaded
  routes.loadEvents()
});

