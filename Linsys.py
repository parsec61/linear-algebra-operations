from decimal import Decimal, getcontext
from copy import deepcopy

from Vector import Vector
from Plane import Plane
from Hyperplane import Hyperplane

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

    def compute_solution(self):
        try:
            return self.do_gaussian_elimination_and_parametrize_solution()

        except Exception as e:
            if str(e) == self.NO_SOLUTIONS_MSG:
                return str(e)
            else:
                raise e

    def do_gaussian_elimination_and_parametrize_solution(self):
        rref = self.compute_rref()

        rref.raise_exception_if_contradictory_equation()

        direction_vectors = rref.extract_direction_vectors_for_parametrization()
        basepoint = rref.extract_basepoint_for_parametrization()

        return Parametrization(basepoint, direction_vectors)

    def extract_direction_vectors_for_parametrization(self):
        n = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indices = set(range(n)) - set(pivot_indices)

        direction_vectors = []

        for free_var in free_variable_indices:
            vector_coords = [0] * n
            vector_coords[free_var] = 1
            for i,p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var < 0:
                    break
                vector_coords[pivot_var] = -p.normal_vector[free_var]
            direction_vectors.append(Vector(vector_coords))
        return direction_vectors

    def extract_basepoint_for_parametrization(self):
        n = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()

        basepoint_coords = [0] * n

        for i,p in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0:
                break
            basepoint_coords[pivot_var] = p.constant_term

        return Vector(basepoint_coords)

    def raise_exception_if_contradictory_equation(self):
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == 'No nonzero elements found':
                    constant_term = MyDecimal(p.constant_term)
                    if not constant_term.is_near_zero():
                        raise Exception(self.NO_SOLUTIONS_MSG)
                else:
                    raise e
                    
    def raise_exception_if_too_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >= 0 else 0 for index in pivot_indices])
        n = self.dimension

        if num_pivots < n:
            raise Exception(self.INF_SOLUTIONS_MSG)

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

class Parametrization(object):

    BASE_AND_DIR_VECTOR_MUST_BE_IN_SAME_DIM_MSG = ("The basepoint and direction vectors should all live in the same dimension")

    def __init__(self, basepoint, direction_vectors):
        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(BASE_AND_DIR_VECTOR_MUST_BE_IN_SAME_DIM_MSG)

class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

