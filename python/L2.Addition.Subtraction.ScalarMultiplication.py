from lib.vector import Vector

#Lesson 2

#2.1 Addition
v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111]) 
print("V + W =" + str(v.plus(w)))

#2.2 Subtraction
x = Vector([7.119, 8.215])
y = Vector([-8.223, 0.878])
print("X - Y = " + str(x.minus(y)))

#2.3 Scalar Multiplication
c = 7.41
z = Vector([1.671, -1.012, -0.318])
print("Scalar c x Vector z = " + str(z.times_scalar(c)))