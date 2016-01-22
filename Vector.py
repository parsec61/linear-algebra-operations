import math

class Vector(object):
  def __init__(self, coordinates):
    try:
      if not coordinates:
        raise ValueError
      self.coordinates = tuple(coordinates)
      self.demension = len(coordinates)
    
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

  def times_scalar(self, s):
    new_coordinates = [x*s for x in self.coordinates]
    return Vector(new_coordinates)

  def magnitude(self):
    magnitude = 0
    for x in range(len(self.coordinates)):
      magnitude = magnitude + self.coordinates[x]**2
    return math.sqrt(magnitude)

  def normalize(self):
    return self.times_scalar(1/self.magnitude())
  
  def __str__(self):
    return 'Vector: {}'.format(self.coordinates)
    
  def __eq__(self, v):
    return self.coordinates == v.coordinates

    
