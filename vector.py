import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize Zero Vector'
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    #Allows Pythons built in print function to work on class
    def __str__(self):
        return ' Vector: {}'.format(self.coordinates)

    # Allows Python equality checks.
    def __eq__(self,v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def times_scalar(self, c):
        new_coordinates = [x*Decimal(c) for x in self.coordinates]
        return Vector(new_coordinates)

    # The Square Root of the sum of all the coordinates in the vector squared
    def get_magnitude(self):
        coordinatesSquared =[x**2 for x in self.coordinates]
        return Decimal(math.sqrt(sum(coordinatesSquared)))

    #Get Normalization of my_vector
    # Scalar multiplication
    # (1 / magnitude of v ) * (v)
    def get_normalization(self):
        try:
            return(self.times_scalar(1/self.get_magnitude()))
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def get_dot_product(self, v):
        product = sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
        return product
    
    def get_angle_btwn(self, v, inDegrees=False):
        try:
            if inDegrees:
                return math.acos( (self.get_dot_product(v)) / (self.get_magnitude() * v.get_magnitude()))
            else:
                return math.acos( (self.get_dot_product(v)) / (self.get_magnitude() * v.get_magnitude()))
        except Exception as e:
                if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                    raise Exception('Cannot compute an angle with Zero Vector')
                else:
                    raise e
            
                
        

    

#Lesson 1 
my_vector = Vector([1,2,3])
print (my_vector)
my_vector_2 = Vector([1,2,3])
my_vector_3 = Vector([-1,2,3])

print (my_vector == my_vector_2)
print (my_vector_2 == my_vector_3)

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

#Lesson 3

#3.1 Magniture
v311 = Vector([-0.221, 7.437])
print("v3.1 Problem 1 Magnitude: " + str(v311.get_magnitude()))

v312 = Vector([8.813, -1.331, -6.247])
print("v3.1 Problem 2 Magnitude: " + str(v312.get_magnitude()))

#3.2 Normalization
v321 = Vector([5.581, -2.136])
print ("Normalizaiton of v321: " + str(v321.get_normalization()))

v322 = Vector([1.996, 3.108, -4.554])
print ("Normalizaiton of v322: " + str(v322.get_normalization()))

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
print("Angle for 4.2.1 in degrees: " + str(math.degrees(v4222.get_angle_btwn(v4222b))))

