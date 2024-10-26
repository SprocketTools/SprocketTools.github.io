import * as navbar from "/scripts/buildNavBar.js";
const pageTitle = document.title;

const contestPages = {
  Active_Contests: "/contests/index.html",
  Code_of_Conduct: "/contests/CodeOfConduct.html",
  Contest_Tank_Picker: "/contests/ContestTankPicker.html",
};

window.addEventListener(
  "load",
  navbar.makePage(
    document,
    navbar.buildNav(contestPages, pageTitle, "center navbar", false),
  ),
);
