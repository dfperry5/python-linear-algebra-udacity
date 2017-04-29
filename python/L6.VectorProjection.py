from lib.vector import Vector

v = Vector([3.039, 1.879])
b = Vector([0.825, 2.036])
print("4.1 Projection: " + str(v.component_parallel_to(b)))

v = Vector([-9.88, -3.264, -8.159])
b = Vector([-2.155, -9.353, -9.473])
print("4.2 Ortogonal to V, off of base vector: " + str(v.component_orthogonal_to(b)))

v = Vector([3.009, -6.172, 3.692, -2.51])
b = Vector([6.404, -9.144, 2.759, 8.718])
print("4.3 Projection: " + str(v.component_parallel_to(b)))
print("4.3 Orthogonal to V, off of base vector b " + str(v.component_orthogonal_to(b)))