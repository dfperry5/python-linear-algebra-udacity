from lib.vector import Vector

#Chapter 5 -- Parallel and Orthogonal Vectors
#5.1
v51 = Vector([-7.569, -7.88])
v51b = Vector([22.737, 23.64])
print("5.1: Are they parallel? " + str(v51.is_Parallel_To(v51b)))
print("5.1: Are they orthogonal? " + str(v51.is_Orthogonal_To(v51b)))

#5.2
v52 = Vector([-2.029, 9.97, 4.172])
v52b = Vector([-9.231, -6.639, -7.245])
print("5.2: Are they parallel? " + str(v52.is_Parallel_To(v52b)))
print("5.2: Are they orthogonal? " + str(v52.is_Orthogonal_To(v52b)))

#5.3
v53 = Vector([-2.328, -7.284, -1.214])
v53b = Vector([-1.821, 1.072, -2.94])
print("5.3: Are they parallel? " + str(v53.is_Parallel_To(v53b)))
print("5.3: Are they orthogonal? " + str(v53.is_Orthogonal_To(v53b)))

#5.4
v54 = Vector([2.118, 4.827])
v54b = Vector([0,0])
print("5.4: Are they parallel? " + str(v54.is_Parallel_To(v54b)))
print("5.4: Are they orthogonal? " + str(v54.is_Orthogonal_To(v54b)))
