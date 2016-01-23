import Vector

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

print(my_vector18.is_parallel(my_vector19))
print(my_vector18.is_orthogonal_to(my_vector19))

my_vector20 = Vector.Vector(['-2.029', '9.97', '4.172'])
my_vector21 = Vector.Vector(['-9.231', '-6.639', '-7.245'])

print(my_vector20.is_parallel(my_vector21))
print(my_vector20.is_orthogonal_to(my_vector21))

my_vector22 = Vector.Vector(['-2.328', '-7.284', '-1.214'])
my_vector23 = Vector.Vector(['-1.821', '1.072', '-2.94'])

print(my_vector22.is_parallel(my_vector23))
print(my_vector22.is_orthogonal_to(my_vector23))

my_vector24 = Vector.Vector(['2.118', '4.827'])
my_vector25 = Vector.Vector(['0', '0'])

print(my_vector24.is_parallel(my_vector25))
print(my_vector24.is_orthogonal_to(my_vector25))
