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

print(my_vector6.magnitude())

print(my_vector7.magnitude())

print(my_vector8.normalize())

print(my_vector9.normalize())
