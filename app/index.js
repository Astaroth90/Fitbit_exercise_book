
import document from "document";
/*
import exercise from "exercise";
import { user } from "user-profile";
import { me } from "appbit";
import { vibration } from "haptics";
*/

import exercises from "./exercises.js";

//const svgStart = document.getElementById("svgStart");

var exer = new exercises("Bauch",10,20,5);

let demotext = document.getElementById("demotext");
demotext.text = exer.Name;

console.log('Hello world!');
