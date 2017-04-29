from lib.vector import Vector

v_1 = Vector([ 8.462, 7.893, -8.187])
w_1 = Vector([6.984, -5.975, 4.778]) 

print(v_1.cross_product(w_1))

v_2 = Vector([-8.987, -9.838, 5.031])
w_2 = Vector([-4.268, -1.861, -8.866])

#Area of parallelogram  spanned by 2 vectors = magnitude of cross_product of those two vectors
print( v_2.area_of_parallelogram_with(w_2))

v_3 = Vector([1.5, 9.547, 3.691])
w_3 = Vector([-6.007, 0.124, 5.772])

print(v_3.area_of_triangle_with(w_3))