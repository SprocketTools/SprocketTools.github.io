export const globalPages = {
  Home: "/index.html",
  Gear_Calculator: "/TopGearCalculator.html",
  Contests: "/contests/index.html",
  Random_Tank_Picker: "/VehicleGenerator.html",
  Guides: "/resources.html",
  Credits: "/credits.html",
  Get_Trolled: "https://www.youtube.com/watch?v=p7YXXieghto",
  Decal_Catalog: "/Decals/index.html",
  RGB_Decal_Maker: "/Decals/RGBmaker.html",
};

/**
 * Builds a navbar with provided options
 * @param {object} pl - Page list
 * @param {string} pt - Current page title (document.title)
 * @param {string} c - Div class
 * @param {string} extra - extra html content to insert before the list
 * @returns {string}
 */
export function buildNav(pl, pt = "", c = "navbar", extra = "") {
  let list = `<div class="${c}">\n${extra}`;
  for (let p in pl) {
    let pname = p.replace(/_/g, " ");
    let url = pl[`${p}`];

    if (new RegExp(`.*${pname}.*`).test(pt)) {
      list += `<a class="active" href="${pl[`${p}`]}">${pname}</a>\n`;
    } else {
      list += `<a href="${url}">${pname}</a>\n`;
    }
  }
  let finalBar = `${list}</div>`;
  return finalBar;
}

/**
 * @param {Document} doc - document object
 * @param {string} h - Header string
 * @param {string} s - Style string
 */
export function makePage(doc, h = "", s = "") {
  doc.body.innerHTML = h + doc.body.innerHTML;
  doc.head.innerHTML = s + doc.head.innerHTML;
}
