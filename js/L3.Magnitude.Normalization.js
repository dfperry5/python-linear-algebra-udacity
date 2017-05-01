const Vector = require('./vector.js');

let v311 = new Vector([-0.221, 7.437])
console.log(v311.getMagnitude());

let v312 = new Vector([8.813, -1.331, -6.247])
console.log("v3.1 Problem 2 Magnitude: " + v312.getMagnitude())

//3.2 Normalization
let v321 = new Vector([5.581, -2.136])
console.log("Normalizaiton of v321: " + v321.getNormalization());

let v322 = new Vector([1.996, 3.108, -4.554])
console.log("Normalizaiton of v322: " + v322.getNormalization());