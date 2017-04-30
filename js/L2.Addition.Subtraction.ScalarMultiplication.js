const Vector = require('./vector.js');

let v1 = new Vector( [8.218, -9.341]);
let v2 = new Vector([-1.129, 2.111])
console.log("Lesson 1 Problem 1: [8.218, -9.341] + [-1.129, 2.111] = " + v1.plus(v2).toString());

v21 = new Vector([7.119, 8.215]);
y21b = new Vector([-8.223, 0.878]);
console.log("Lesson 1 Problem 2: [7.119, 8.215] - [-8.223, 0.878] = " + v21.minus(y21b).toString());

let c = 7.41
let z = new Vector([1.671, -1.012, -0.318])
console.log("Lesson 1 Problem 3: 7.41 * [1.671, -1.012, -0.318] = " + z.times_scalar(c).toString());