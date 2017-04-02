import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
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
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)

    # The Square Root of the sum of all the coordinates in the vector squared
    def get_magnitude(self):
        coordinatesSquared =[x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinatesSquared))

    #Get Normalization of my_vector
    # Scalar multiplication
    # (1 / magnitude of v ) * (v)
    def get_normalization(self):
        try:
            return(self.times_scalar(1/self.get_magnitude()))
        except ZeroDivisionError:
            raise Exception('Cannot normalize Zero Vector')
        

    

#Lesson 1 -- 
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





            
    