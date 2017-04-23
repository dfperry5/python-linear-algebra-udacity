import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize Zero Vector'
    PI = 3.14
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

    def is_zero_vector(self, tolerance=1e-10):
        return (self.get_magnitude() < tolerance)

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
        product = sum([Decimal(x*y) for x,y in zip(self.coordinates, v.coordinates)])
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
    
    def is_Orthogonal_To(self, v, tolerance=1e-10):
        return (abs(self.get_dot_product(v)) < tolerance)

    def is_Parallel_To(self, v):
        return (
            self.is_zero_vector() or 
            v.is_zero_vector() or 
            self.get_angle_btwn(v) == 0 or
             round(self.get_angle_btwn(v),2) == round(math.pi,2)
             )

