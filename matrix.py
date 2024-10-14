from functools import wraps
from typing import Callable, Self, Any
from copy import deepcopy

import numpy
import numpy as np
from numpy import ndarray


class Matrix:
    def __init__(self, raw_matrix: np.ndarray[Any, np.dtype]) -> None:
        self.origin = self
        self.__rows_number = len(raw_matrix)
        self.__columns_number = len(raw_matrix[0])
        self.raw_matrix = raw_matrix
        self.range_rows_number = range(self.__rows_number)
        self.range_columns_number = range(self.__columns_number)
        self.is_row_vector = (self.__rows_number == 1)
        self.is_column_vector = (self.__columns_number == 1)

    @staticmethod
    def matrix_from_raw(raw_matrix) -> "Matrix":
        return Matrix(raw_matrix)

    @property
    def matrix_shape(self) -> list[int]:
        return [self.__rows_number, self.__columns_number]

    @staticmethod
    def same_dimension(func: Callable[["Matrix", "Matrix"], ...]):
        @wraps(func)
        def wrapper(this: "Matrix", other: "Matrix") -> ...:
            if this.matrix_shape == other.matrix_shape:
                return func(this, other)
            else:
                raise ValueError("Matrices should have same dimensions to do this action!")
        return wrapper

    @staticmethod
    def is_multipliable(func: Callable[["Matrix", "Matrix"], ...]):
        @wraps(func)
        def wrapper(this: "Matrix", other: "Matrix") -> ...:
            if this.matrix_shape[1] == other.matrix_shape[0]:
                return func(this, other)
            else:
                raise ValueError("Unable to do this action, invalid matrices!")

        return wrapper

    @staticmethod
    def __only_squared(func: Callable[["Matrix", ...], ...]) -> Callable[['Matrix', ...], ...]:
        @wraps(func)
        def wrapper(matrix: "Matrix", *args: tuple, **kwargs: dict) -> ...:
            if matrix.is_square():
                return func(matrix, *args, **kwargs)
            else:
                raise ValueError("Matrix should be squared to do this action!")
        return wrapper

    @staticmethod
    def __only_vector(func: Callable[["Matrix", ...], ...]) -> ...:
        def wrapper(self, *args, **kwargs):
            if self.is_row_vector() or self.is_column_vector():
                return func(self, *args, **kwargs)
            else:
                raise ValueError("Matrix should be vector to do this action!")
        return wrapper

    @staticmethod
    def __only_invertible(func: Callable[["Matrix", ...], ...]) -> ...:
        def wrapper(self, *args, **kwargs):
            if self.determinant() != 0:
                return func(self, *args, **kwargs)
            else:
                raise ValueError("Matrix should be invertible to do this action!")
        return wrapper

    @staticmethod
    def __only_able_to_power(func: Callable[["Matrix", int, ...], ...]) -> ...:
        def wrapper(self, power, *args, **kwargs):
            if  power % 1 == 0:
                return func(self, power, *args, **kwargs)
            else:
                raise ValueError("Power should be a whole number to do this action!")
        return wrapper


    def is_square(self) -> bool:
        return self.__rows_number == self.__columns_number

    def is_row_vector(self) -> bool:
        return self.__rows_number == 1

    def is_column_vector(self) -> bool:
        return self.__columns_number == 1

    def transpose(self) -> Self:
        transpose = np.transpose(self.raw_matrix)
        return Matrix(transpose)

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.raw_matrix])

    @same_dimension
    def add_matrix(self, other):
        return Matrix(self.raw_matrix + other.raw_matrix)

    def __add__(self, *args) -> Self:
        result = self
        for other in args:
            if isinstance(self, Matrix) and isinstance(other, Matrix):
                result = self.add_matrix(other)
            elif isinstance(other, int | float):
                result = Matrix(self.raw_matrix + other * np.eye(self.matrix_shape[0],
                                self.raw_matrix.shape[1]))
            else:
                raise ValueError(f"Adding not supported between Matrix and {type(other)}")
        return result

    def __radd__(self, other):
        if isinstance(other, int | float):
            return Matrix(self.raw_matrix * (-1)+ other * np.eye(self.matrix_shape[0],
                                self.raw_matrix.shape[1]))
        else:
            raise ValueError(f"Right-side adding not supported between Matrix and {type(other)}")

    @same_dimension
    def subtract_matrix(self, other):
        return Matrix(self.raw_matrix - other.raw_matrix)

    def __sub__(self, *args) -> Self:
        result = self
        for other in args:
            if isinstance(self, Matrix) and isinstance(other, Matrix):
                result = self.subtract_matrix(other)
            elif isinstance(other, int | float):
                result = Matrix(self.raw_matrix - other * np.eye(self.matrix_shape[0],
                                self.raw_matrix.shape[1]))
            else:
                raise ValueError(f"Subtraction not supported between Matrix and {type(other)}")
        return result

    def __rsub__(self, other):
        if isinstance(other, int | float):
            return Matrix(self.raw_matrix * (-1) + other * np.eye(self.matrix_shape[0],
                                self.raw_matrix.shape[1]))
        else:
            raise ValueError(f"Right-side subtraction not supported between Matrix and {type(other)}")

    @is_multipliable
    def multiply_matrix(self, other: "Matrix") -> Self:
        multiplication = np.matmul(self.raw_matrix, other.raw_matrix)
        return Matrix(multiplication)

    def __mul__(self, *args) -> ...:
        result = self
        for other in args:
            if isinstance(other, Matrix):
                result = result.multiply_matrix(other)
            elif isinstance(other, (int, float)):
                result = Matrix(result.raw_matrix * other)
            else:
                raise ValueError(f"Multiplication not supported between Matrix and {type(other)}")
        return result

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return Matrix(self.raw_matrix * other)
        else:
            raise ValueError(f"Right-side multiplication not supported between Matrix and {type(other)}")

    def __eq__(self, other: Self) -> bool:
        return self.raw_matrix == other.raw_matrix

    @__only_squared
    def sub_matrix(self, row: int = -1, column: int = -1) -> Self:
        submatrix = np.delete(np.delete(self.raw_matrix, row, axis=0), column, axis=1)
        return Matrix(submatrix)

    @__only_squared
    def minor(self, row: int, column: int) -> int | float:
        if self.__rows_number == 1 and self.__columns_number == 1:
            minor = self.determinant()
        else:
            minor = self.sub_matrix(row, column).determinant()
        return minor

    @__only_squared
    def adjunct(self, row: int, column: int) -> int | float:
        adjunct = (-1) ** (row + column) * self.minor(row, column)
        return adjunct

    @__only_squared
    def determinant(self) -> int | float:
        if self.__rows_number == 1:
            return float(self.raw_matrix[0, 0])
        elif self.__rows_number == 2:
            return float(self.raw_matrix[0, 0] * self.raw_matrix[1, 1] -
                    self.raw_matrix[0, 1] * self.raw_matrix[1, 0])
        else:
            determinant = 0
            for row in self.range_rows_number:
                determinant += self.adjunct(row, 0) * self.raw_matrix[row, 0]
            return determinant

    @__only_squared
    def cofactor(self) -> Self:
        cofactor_matrix = np.array([[self.adjunct(row, column)
                                     for column in range(self.raw_matrix.shape[1])]
                                    for row in range(self.raw_matrix.shape[0])])
        return Matrix(cofactor_matrix)

    @__only_squared
    @__only_invertible
    def __invert__(self) -> Self:
        determinant = self.determinant()
        transposed_cofactor_matrix = self.cofactor().transpose()
        inverse = transposed_cofactor_matrix * (1 / determinant)
        return inverse

    @__only_able_to_power
    @__only_squared
    def __pow__(self, power: int) -> Self:
        result = Matrix(np.identity(self.matrix_shape[0]))
        base_matrix = self
        even_divider = 2
        if power <= -1:
            return (self ** power).__invert__()
        elif power == 0:
            return result
        elif power > 0:
            while power > 0:
                if power % even_divider == 1:
                    result = base_matrix * result
                base_matrix *= base_matrix
                power //= even_divider
            return result


'''
Enter number of rows: 4
Enter number of columns: 4
2 3 4 1
8 9 2 6
2 4 5 9
8 1 3 2
'''
if __name__ == "__main__":
    a = Matrix(np.array([[3, 9, -4], [1, 5, -8], [4, 2, -9]]))
    b = Matrix(np.array([[3, 9, -4], [1, 5, -8], [4, 2, -9]]))
    print(a.determinant())
    print(a.cofactor())
    print(3 - a + 4)