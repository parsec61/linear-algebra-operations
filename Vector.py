from math import sqrt, degrees, acos
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

  CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
  
  def __init__(self, coordinates):
    try:
      if not coordinates:
        raise ValueError
      self.coordinates = tuple([Decimal(x) for x in coordinates])
      self.demension = len(self.coordinates)
    
    except ValueError:
      raise ValueError('The coordinates must be nonempty')
    
    except TypeError:
      raise ValueError('The coordinates must be an iterable')

  def plus(self, v):
    new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)

  def minus(self, v):
    new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)

  def times_scalar(self, c):
    new_coordinates = [Decimal(c)*x for x in self.coordinates]
    return Vector(new_coordinates)

  def magnitude(self):
    coordinates_squared = [x**2 for x in self.coordinates]
    return sqrt(sum(coordinates_squared))

  def normalize(self):
    try:
      magnitude = self.magnitude()
      return self.times_scalar(1./magnitude)

    except ZeroDivisionError:
      raise Exeption(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

  def dot(self, v): #v1*w1 + v2*w2 + ... + vn*wn
    return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

  def angle_with(self, v, in_deg = False): #arc cosine (dot product / (magnitudeV * magnitudeW))
    try:
      #dot = self.dot(v)
      #magnitude_s = self.magnitude()
      #magnitude_v = v.magnitude()
      #angle = acos(dot/(magnitude_s*magnitude_v))
      u1 = self.normalize()
      u2 = v.normalize()
      angle = acos(u1.dot(u2))

      if in_deg:
        return degrees(angle)
      else:
        return angle
    except Exception as e:
      if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
        raise Exception('Cannot compute an angle with the zero vector')
      else:
        raise e

  def is_parallel():

  def is_orthogonal():
  
  def __str__(self):
    return 'Vector: {}'.format(self.coordinates)
    
  def __eq__(self, v):
    return self.coordinates == v.coordinates

    
