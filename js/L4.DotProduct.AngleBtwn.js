const Vector = require('./vector.js');

//Section 4.1 -- Dot product
//4.1.1
let v411 = new Vector([7.887, 4.138])
let v411b = new Vector([-8.802, 6.776])
console.log("Dot Product 4.1.1: " + v411.dotProductWith(v411b));

//4.1.1
let v4112 = new Vector([-5.955, -4.904, -1.874])
let v4112b = new Vector([-4.496, -8.755, 7.103])
console.log("Dot Product 4.1.2: " + v4112.dotProductWith(v4112b));

//4.2.1 -- Get Angle
let v4211 = new Vector([3.183, -7.627])
let v4211b = new Vector([-2.668, 5.319])
console.log("Angle for 4.2.1: " + v4211.angleWith(v4211b));

//4.2.2 -- Get Angle
let v4222 = new Vector([7.35, 0.221, 5.188])
let v4222b = new Vector([2.751, 8.259, 3.985])
console.log("Angle for 4.2.1 in degrees: " + v4222.angleWith(v4222b, true));
