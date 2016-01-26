from decimal import Decimal, getcontext
from copy import deepcopy

from Vector import Vector
from Plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        temp_row = self[row1]
        self[row1] = self[row2]
        self[row2] = temp_row

    def multiply_coefficient_and_row(self, coefficient, row):
        v1 = Vector(self[row].normal_vector)
        c1 = self[row].constant_term
        
        new_normal_vector = v1.times_scalar(coefficient, True)
        new_constant_term = coefficient * c1

        self[row] = Plane(new_normal_vector, new_constant_term)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        v1 = Vector(self[row_to_add].normal_vector)
        c1 = self[row_to_add].constant_term

        v2 = Vector(self[row_to_be_added_to].normal_vector)
        c2 = self[row_to_be_added_to].constant_term

        new_normal_vector = v1.times_scalar(coefficient).plus(v2, True)
        new_constant_term = (c1 * coefficient) + c2

        self[row_to_be_added_to] = Plane(new_normal_vector, new_constant_term)

    def compute_triangular_form(self):
        system = deepcopy(self)

        n = len(system)
        v = system.dimension
        
        j = 0
        for i in range(n):
            while j < v:
                c = MyDecimal(system[i].normal_vector[j])
                if c.is_near_zero():
                    swap_succeeded = system.swap_with_row_below(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue
                system.clear_coefficients_below(i, j)
                j += 1
                break
        
        return system

    def compute_rref(self):
        tf = self.compute_triangular_form()

        n = len(tf)
        indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for i in range(n)[::-1]:
            j = indices[i]
            if j < 0:
                continue
            tf.scale_row_to_make_coefficient_equal_one(i,j)
            tf.clear_coefficients_above(i,j)
            
        return tf

    def scale_row_to_make_coefficient_equal_one(self, row, col):
        n = self[row].normal_vector
        beta = Decimal('1.0') / Decimal(n[col])
        self.multiply_coefficient_and_row(beta, row)

    def clear_coefficients_above(self, row, col):
        for i in range(row)[::-1]:
            n = self[i].normal_vector
            alpha = -(MyDecimal(n[col]))
            self.add_multiple_times_row_to_row(alpha, row, i)

    def swap_with_row_below(self, row, col):
        n = len(self)

        for i in range(row+1, n):
            coefficient = MyDecimal(self[i].normal_vector[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row,i)
                return True
        return False

    def clear_coefficients_below(self, row, col):
        n = len(self)
        beta = MyDecimal(self[row].normal_vector[col])

        for i in range(row+1, n):
            m = self[i].normal_vector
            gamma = MyDecimal(m[col])
            alpha = -gamma/beta
            self.add_multiple_times_row_to_row(alpha, row, i)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


p0 = Plane(['1','1','1'], '1')
p1 = Plane(['0','1','0'], '2')
p2 = Plane(['1','1','-1'], '3')
p3 = Plane(['1','0','-2'], '2')

s = LinearSystem([p0,p1,p2,p3])

#print (s.indices_of_first_nonzero_terms_in_each_row())
#print ('{},{},{},{}'.format(s[0],s[1],s[2],s[3]))
#print (len(s))
#print (s)
#print("------")

#s[0] = p1
#print (s[0])

#s.swap_rows(0,1)
#print(s)

#print(s[0])
#s.multiply_coefficient_and_row(2, 0)
#print(s[0])

#print (MyDecimal('1e-9').is_near_zero())
#print (MyDecimal('1e-11').is_near_zero())



##p0 = Plane(['1','1','1'], '1')
##p1 = Plane(['0','1','0'], '2')
##p2 = Plane(['1','1','-1'], '3')
##p3 = Plane(['1','0','-2'], '2')
##
##s = LinearSystem([p0,p1,p2,p3])
##s.swap_rows(0,1)
##if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
##    print ('test case 1 failed')
##
##s.swap_rows(1,3)
##if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
##    print ('test case 2 failed')
##
##s.swap_rows(3,1)
##if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
##    print ('test case 3 failed')
##
##s.multiply_coefficient_and_row(1,0)
##if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
##    print ('test case 4 failed')
##
##s.multiply_coefficient_and_row(-1,2)
##if not (s[0] == p1 and
##        s[1] == p0 and
##        s[2] == Plane(['-1','-1','1'], '-3') and
##        s[3] == p3):
##    print ('test case 5 failed')
##
##s.multiply_coefficient_and_row(10,1)
##if not (s[0] == p1 and
##        s[1] == Plane(['10','10','10'], '10') and
##        s[2] == Plane(['-1','-1','1'], '-3') and
##        s[3] == p3):
##    print ('test case 6 failed')
##
##s.add_multiple_times_row_to_row(0,0,1)
##if not (s[0] == p1 and
##        s[1] == Plane(['10','10','10'], '10') and
##        s[2] == Plane(['-1','-1','1'], '-3') and
##        s[3] == p3):
##    print ('test case 7 failed')
##
##s.add_multiple_times_row_to_row(1,0,1)
##if not (s[0] == p1 and
##        s[1] == Plane(['10','11','10'], '12') and
##        s[2] == Plane(['-1','-1','1'], '-3') and
##        s[3] == p3):
##    print ('test case 8 failed')
##
##s.add_multiple_times_row_to_row(-1,1,0)
##if not (s[0] == Plane(['-10','-10','-10'], '-10') and
##        s[1] == Plane(['10','11','10'], '12') and
##        s[2] == Plane(['-1','-1','1'], '-3') and
##        s[3] == p3):
##    print ('test case 9 failed')


p1 = Plane(['1','1','1'], '1')
p2 = Plane(['0','1','1'], '2')
s = LinearSystem([p1,p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and t[1] == p2):
    print ('test case 1 failed')

p1 = Plane(['1','1','1'], '1')
p2 = Plane(['1','1','1'], '2')
s = LinearSystem([p1,p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == Plane(['0','0','0'], '1')):
    print ('test case 2 failed')

p1 = Plane(['1','1','1'], '1')
p2 = Plane(['0','1','0'], '2')
p3 = Plane(['1','1','-1'], '3')
p4 = Plane(['1','0','-2'], '2')
s = LinearSystem([p1,p2,p3,p4])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2 and
        t[2] == Plane(['0','0','-2'], '2') and
        t[3] == Plane(['0','0','0'], '0')):
    print ('test case 3 failed')

p1 = Plane(['0','1','1'], '1')
p2 = Plane(['1','-1','1'], '2')
p3 = Plane(['1','2','-5'], '3')
s = LinearSystem([p1,p2,p3])
t = s.compute_triangular_form()
if not (t[0] == Plane(['1','-1','1'], '2') and
        t[1] == Plane(['0','1','1'], '1') and
        t[2] == Plane(['0','0','-9'], '-2')):
    print ('test case 4 failed')


p1 = Plane(['1','1','1'], '1')
p2 = Plane(['0','1','1'], '2')
s = LinearSystem([p1,p2])
r = s.compute_rref()
if not (r[0] == Plane(['1','0','0'], '-1') and
        r[1] == p2):
    print ('test case 1 failed')

p1 = Plane(['1','1','1'], '1')
p2 = Plane(['1','1','1'], '2')
s = LinearSystem([p1,p2])
r = s.compute_rref()
if not (r[0] == p1 and
        r[1] == Plane(['0','0','0'], '1')):
    print ('test case 2 failed')

p1 = Plane(['1','1','1'], '1')
p2 = Plane(['0','1','0'], '2')
p3 = Plane(['1','1','-1'], '3')
p4 = Plane(['1','0','-2'], '2')
s = LinearSystem([p1,p2,p3,p4])
r = s.compute_rref()
if not (r[0] == Plane(['1','0','0'], '0') and
        r[1] == p2 and
        r[2] == Plane(['0','0','-2'], '2') and
        r[3] == Plane(['0','0','0'], '0')):
    print ('test case 3 failed')

p1 = Plane(['0','1','1'], '1')
p2 = Plane(['1','-1','1'], '2')
p3 = Plane(['1','2','-5'], '3')
s = LinearSystem([p1,p2,p3])
r = s.compute_rref()
if not (r[0] == Plane(['1','0','0'], Decimal('23')/Decimal('9')) and
        r[1] == Plane(['0','1','0'], Decimal('7')/Decimal('9')) and
        r[2] == Plane(['0','0','1'], Decimal('2')/Decimal('9'))):
    print ('test case 4 failed')
