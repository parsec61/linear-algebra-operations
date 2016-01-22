import Vector

my_vector1 = Vector.Vector([8.218, -9.341])
my_vector2 = Vector.Vector([-1.129, 2.111])

my_vector3 = Vector.Vector([7.119, 8.215])
my_vector4 = Vector.Vector([-8.223, 0.878])

my_scalar = 7.41
my_vector5 = Vector.Vector([1.671, -1.012, -0.318])

print(my_vector1.plus(my_vector2))

print(my_vector3.minus(my_vector4))

print(my_vector5.times_scalar(my_scalar))
