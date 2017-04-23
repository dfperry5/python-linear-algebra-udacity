from lib.vector import Vector
#Section 4.1 -- Dot product
#4.1.1
v411 = Vector([7.887, 4.138])
v411b = Vector([-8.802, 6.776])
print("Dot Product 4.1.1: " + str(v411.get_dot_product(v411b)))

#4.1.1
v4112 = Vector([-5.955, -4.904, -1.874])
v4112b = Vector([-4.496, -8.755, 7.103])
print("Dot Product 4.1.2: " + str(v4112.get_dot_product(v4112b)))

#4.2.1 -- Get Angle
v4211 = Vector([3.183, -7.627])
v4211b = Vector([-2.668, 5.319])
print("Angle for 4.2.1: " + str(v4211.get_angle_btwn(v4211b)))

#4.2.2 -- Get Angle
v4222 = Vector([7.35, 0.221, 5.188])
v4222b = Vector([2.751, 8.259, 3.985])
print("Angle for 4.2.1 in degrees: " + str(v4222.get_angle_btwn(v4222b, True)))
