import math

class Vector:
    def __init__(self, data):
        self._vector = data.copy()

    def __str__(self):
        element = [str(element) for element in self._vector]
        element = ", ".join(element)
        return f"[{element}]"

    def dim(self):
        return len(self._vector)

    def get(self, index):
        return self._vector[index]

    def set(self, index, value):
        self._vector[index] = value

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            result = [element * scalar for element in self._vector]
            return Vector(result)
        else:
            raise TypeError("Can only multiply by an integer or float")

    def __imul__(self, scalar):
        if isinstance(scalar, (int, float)):
            for i in range(len(self._vector)):
                self._vector[i] *= scalar
            return self
        else:
            raise TypeError("Can only multiply by an integer or float")

    def __rmul__(self, scalar):
        if isinstance(scalar, (int, float)):
            result = [element * scalar for element in self._vector]
            return Vector(result)
        else:
            raise TypeError("Can only multiply by a string or float")

    def __add__(self, other_vector):
        result = []
        if type(other_vector) is not Vector or len(other_vector._vector) != len(self._vector):
            return None
        else:
            for a, b in zip(self._vector, other_vector._vector):
                result.append(a + b)
            return Vector(result)

    def __iadd__(self, other_vector):
        if type(other_vector) is not Vector or len(other_vector._vector) != len(self._vector):
            return None
        else:
            for i in range(len(self._vector)):
                self._vector[i] += other_vector._vector[i]
            return self

    def __eq__(self, other_vector):
        if type(other_vector) is not Vector or len(other_vector._vector) != len(self._vector):
            return False
        for a, b in zip(self._vector, other_vector._vector):
            if not math.isclose(a, b, abs_tol = 1e-9):
                return False
        return True

    def __ne__(self, other_vector):
        if type(other_vector) is not Vector or len(other_vector._vector) != len(self._vector):
            return True
        for a, b in zip(self._vector, other_vector._vector):
            if not math.isclose(a, b, abs_tol = 1e-9):
                return True
        return False



# vector1 = Vector([1.0, 2.0, 3.0])
# vector2 = Vector([1.0, 2.0, 3.0])
# vector1 *= 3
# print(vector1)

# my_vector = Vector([1.0, 2.1, 3.2])
# print(my_vector)
# my_vector.scalar_product(3)