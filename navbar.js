import * as navbar from "/scripts/buildNavBar.js";
const pageTitle = document.title;

const style =
  '<link rel="icon" type="image/x-icon" href="/assets/SprocketToolsLogo.png">';

window.addEventListener(
  "load",
  navbar.makePage(
    document,
    navbar.buildNav(
      navbar.globalPages,
      pageTitle,
      "navbar",
      '<img src="/assets/SprocketToolsLogo.png">\n',
    ),
    style,
  ),
);
