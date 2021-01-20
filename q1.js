let context;
let canvas;
let man;
let man2;
let man3;
let man4;
let colour_button;
let score =0;
let interval_id;

document.addEventListener('DOMContentLoaded', init, false);
function init () {
  document.getElementById("enter").outerHTML = "";
  colour_button =document.getElementById("man")
  colour_button.addEventListener("click",clicky);


}
function clicky() {
  document.getElementById("man").outerHTML =""
  man3 =document.createTextNode("Q1:October 5th,Q2:10,Q3:True,Q4:2004,Q5:Damage its head");
  man4 =document.getElementById("yes3")
  man4.appendChild(man3)
}
