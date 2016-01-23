from math import sqrt, degrees, acos, pi
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
    coordinates_squared = [x**Decimal('2.0') for x in self.coordinates]
    return Decimal(sqrt(sum(coordinates_squared)))

  def normalize(self):
    try:
      magnitude = self.magnitude()
      return self.times_scalar(Decimal('1.0')/magnitude)

    except ZeroDivisionError:
      raise Exeption(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

  def dot(self, v): #v1*w1 + v2*w2 + ... + vn*wn
    return round(sum([x*y for x,y in zip(self.coordinates, v.coordinates)]), 10)

  def angle_with(self, v, in_deg = False):
    try:
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

  def is_parallel(self, v):
    return (self.is_zero() or
            v.is_zero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == pi)

  def is_orthogonal_to(self, v, tolerance = 1e-10):
    return abs(self.dot(v)) < tolerance

  def is_zero(self, tolerance = 1e-10):
    return self.magnitude() < tolerance
  
  def __str__(self):
    return 'Vector: {}'.format(self.coordinates)
    
  def __eq__(self, v):
    return self.coordinates == v.coordinates

    
