from __future__ import annotations
from functools import wraps
from typing import Callable, Self, Any
import numpy as np

class Matrix:
    def __init__(self, raw_matrix: np.ndarray[Any, np.dtype]) -> None:
        self.__rows_number = len(raw_matrix)
        self.__columns_number = len(raw_matrix[0])
        self.raw_matrix = raw_matrix
        self.range_rows_number = range(self.__rows_number)
        self.range_columns_number = range(self.__columns_number)

    @property
    def is_row_vector(self: Matrix) -> bool:
        return self.__rows_number == 1

    @property
    def is_column_vector(self: Matrix) -> bool:
        return self.__columns_number == 1

    @staticmethod
    def matrix_from_raw(raw_matrix: list[list[float]]) -> Matrix:
        return Matrix(np.array(raw_matrix))

    @property
    def matrix_shape(self) -> list[int]:
        return [self.__rows_number, self.__columns_number]

    @property
    def is_square(self) -> bool:
        return self.__rows_number == self.__columns_number

    def transpose(self) -> Matrix:
        transpose = np.transpose(self.raw_matrix)
        return Matrix(transpose)

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.raw_matrix])

    @same_dimension
    def add_matrix(self, other: Matrix) -> Matrix:
        return Matrix(self.raw_matrix + other.raw_matrix)

    def __add__(self, *args: Matrix | int | float) -> Matrix:
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

    def __radd__(self, other: int | float) -> Matrix:
        if isinstance(other, int | float):
            return self + other
        else:
            raise ValueError(f"Right-side adding not supported between Matrix and {type(other)}")

    @same_dimension
    def subtract_matrix(self, other: Matrix) -> Matrix:
        return Matrix(self.raw_matrix - other.raw_matrix)

    def __sub__(self, *args: Matrix | int | float) -> Matrix:
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

    def __rsub__(self, other: int | float) -> Matrix:
        if isinstance(other, int | float):
            return Matrix(self.raw_matrix * (-1) + other * np.eye(self.matrix_shape[0],
                                self.raw_matrix.shape[1]))
        else:
            raise ValueError(f"Right-side subtraction not supported between Matrix and {type(other)}")

    @is_multipliable
    def multiply_matrix(self, other: Matrix) -> Matrix:
        multiplication = np.matmul(self.raw_matrix, other.raw_matrix)
        return Matrix(multiplication)

    def __mul__(self, *args: Matrix | int | float) -> Matrix:
        result = self
        for other in args:
            if isinstance(other, Matrix):
                result = result.multiply_matrix(other)
            elif isinstance(other, (int, float)):
                result = Matrix(result.raw_matrix * other)
            else:
                raise ValueError(f"Multiplication not supported between Matrix and {type(other)}")
        return result

    def __rmul__(self, other: int | float) -> Matrix:
        if isinstance(other, int | float):
            return Matrix(self.raw_matrix * other)
        else:
            raise ValueError(f"Right-side multiplication not supported between Matrix and {type(other)}")

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented
        return np.array_equal(self.raw_matrix, other.raw_matrix)

    @__only_squared
    def sub_matrix(self, row: int = -1, column: int = -1) -> Matrix:
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
    def cofactor(self) -> Matrix:
        cofactor_matrix = np.array([[self.adjunct(row, column)
                                     for column in range(self.raw_matrix.shape[1])]
                                    for row in range(self.raw_matrix.shape[0])])
        return Matrix(cofactor_matrix)

    @__only_squared
    @__only_invertible
    def __invert__(self) -> Matrix:
        determinant = self.determinant()
        transposed_cofactor_matrix = self.cofactor().transpose()
        inverse = transposed_cofactor_matrix * (1 / determinant)
        return inverse

    @__only_able_to_power
    @__only_squared
    def __pow__(self, power: int | float) -> Matrix:
        if power == 0:
            return Matrix(np.identity(self.matrix_shape[0]))
        if power < 0:
            return (self ** abs(power)).__invert__()
        result = Matrix(np.identity(self.matrix_shape[0]))
        base_matrix = self
        while power > 0:
            if power % 2 == 1:
                result = base_matrix * result
            base_matrix *= base_matrix
            power //= 2
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
    print(a ** -3)