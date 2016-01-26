import Vector
from Line import Line
from Plane import Plane
from Linsys import Linsys


my_vector1 = Vector.Vector([8.218, -9.341])
my_vector2 = Vector.Vector([-1.129, 2.111])

my_vector3 = Vector.Vector([7.119, 8.215])
my_vector4 = Vector.Vector([-8.223, 0.878])

my_scalar = 7.41
my_vector5 = Vector.Vector([1.671, -1.012, -0.318])

#print(my_vector1.plus(my_vector2))

#print(my_vector3.minus(my_vector4))

#print(my_vector5.times_scalar(my_scalar))


my_vector6 = Vector.Vector([-0.221, 7.437])
my_vector7 = Vector.Vector([8.813, -1.331, -6.247])
my_vector8 = Vector.Vector([5.581, -2.136])
my_vector9 = Vector.Vector([1.996, 3.108, -4.554])

#print(my_vector6.magnitude())

#print(my_vector7.magnitude())

#print(my_vector8.normalize())

#print(my_vector9.normalize())

my_vector10 = Vector.Vector([7.887, 4.138])
my_vector11 = Vector.Vector([-8.802, 6.776])

#print(my_vector10.dot(my_vector11))

my_vector12 = Vector.Vector([-5.955, -4.904, -1.874])
my_vector13 = Vector.Vector([-4.496, -8.755, 7.103])

#print(my_vector12.dot(my_vector13))

my_vector14 = Vector.Vector([3.183, -7.627])
my_vector15 = Vector.Vector([-2.668, 5.319])

#print(my_vector14.angle_with(my_vector15))

my_vector16 = Vector.Vector([7.35, 0.221, 5.188])
my_vector17 = Vector.Vector([2.751, 8.259, 3.985])

#print(my_vector16.angle_with(my_vector17, True))



my_vector18 = Vector.Vector(['-7.579', '-7.88'])
my_vector19 = Vector.Vector(['22.737', '23.64'])

#print(my_vector18.is_parallel_to(my_vector19))
#print(my_vector18.is_orthogonal_to(my_vector19))

my_vector20 = Vector.Vector(['-2.029', '9.97', '4.172'])
my_vector21 = Vector.Vector(['-9.231', '-6.639', '-7.245'])

#print(my_vector20.is_parallel_to(my_vector21))
#print(my_vector20.is_orthogonal_to(my_vector21))

my_vector22 = Vector.Vector(['-2.328', '-7.284', '-1.214'])
my_vector23 = Vector.Vector(['-1.821', '1.072', '-2.94'])

#print(my_vector22.is_parallel_to(my_vector23))
#print(my_vector22.is_orthogonal_to(my_vector23))

my_vector24 = Vector.Vector(['2.118', '4.827'])
my_vector25 = Vector.Vector(['0', '0'])

#print(my_vector24.is_parallel_to(my_vector25))
#print(my_vector24.is_orthogonal_to(my_vector25))

my_vector1 = Vector.Vector([3.039, 1.879])
my_vector2 = Vector.Vector([0.825, 2.036])

#print(my_vector1.component_parallel_to(my_vector2))

my_vector1 = Vector.Vector([-9.88, -3.264, -8.159])
my_vector2 = Vector.Vector([-2.155, -9.353, -9.473])

#print(my_vector1.component_orthogonal_to(my_vector2))

my_vector1 = Vector.Vector([3.009, -6.172, 3.692, -2.51])
my_vector2 = Vector.Vector([6.404, -9.144, 2.759, 8.718])

#print(my_vector1.component_parallel_to(my_vector2))
#print(my_vector1.component_orthogonal_to(my_vector2))

v1 = Vector.Vector([8.462, 7.893, -8.187])
v2 = Vector.Vector([6.984, -5.975, 4.778])

#print(v1.cross(v2))

v1 = Vector.Vector([-8.987, -9.838, 5.031])
v2 = Vector.Vector([-4.268, -1.861, -8.866])

#print(v1.area_of_parallelogram(v2))

v1 = Vector.Vector([1.5, 9.547, 3.691])
v2 = Vector.Vector([-6.007, 0.124, 5.772])

#print(v1.area_of_triangle(v2))

##l1 = Line(['4.046', '2.836'], '1.21')
##l2 = Line(['10.115', '7.09'], '3.025')
##
##print(l1.is_parallel_to(l2))
##print(l1 == l2)
##print(l1.intersection_with(l2))
##
##l1 = Line(['7.204', '3.182'], '8.68')
##l2 = Line(['8.172', '4.114'], '9.883')
##
##print(l1.is_parallel_to(l2))
##print(l1 == l2)
##print(l1.intersection_with(l2))
##
##l1 = Line(['1.182', '5.562'], '6.744')
##l2 = Line(['1.773', '8.343'], '9.525')

#print(l1.is_parallel_to(l2))
#print(l1 == l2)
#print(l1.intersection_with(l2))

p1 = Plane(['-0.412', '3.806', '0.728'], '-3.46')
p2 = Plane(['1.03', '-9.515', '-1.82'], '8.65')

print(p1.is_parallel_to(p2))
print(p1 == p2)

p1 = Plane(['2.611', '5.528', '0.283'], '4.6')
p2 = Plane(['7.715', '8.306', '5.342'], '3.76')

print(p1.is_parallel_to(p2))
print(p1 == p2)

p1 = Plane(['-7.926', '8.625', '-7.217'], '-7.952')
p2 = Plane(['-2.642', '2.875', '-2.404'], '-2.443')

print(p1.is_parallel_to(p2))
print(p1 == p2)



