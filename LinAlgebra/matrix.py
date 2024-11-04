from __future__ import annotations
from functools import wraps
import numpy as np
from typing import Callable, Self, Any


class Matrix:
    def __init__(self, raw_matrix: np.ndarray[Any, np.dtype]) -> None:
        self.raw_matrix = raw_matrix
        self.__rows_number = len(self.raw_matrix)
        self.__columns_number = len(self.raw_matrix[0])
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

    @staticmethod
    def same_dimension(func: Callable[[Matrix, Matrix], Any]) -> Callable[[Matrix, Matrix], Any]:
        @wraps(func)
        def wrapper(this: Matrix, other: Matrix) -> Any:
            if this.matrix_shape == other.matrix_shape:
                return func(this, other)
            else:
                raise ValueError("Matrices should have same dimensions to do this action!")

        return wrapper

    @staticmethod
    def is_multipliable(func: Callable[[Matrix, Matrix], Any]) -> Callable[[Matrix, Matrix], Any]:
        @wraps(func)
        def wrapper(this: Matrix, other: Matrix) -> Any:
            if this.matrix_shape[1] == other.matrix_shape[0]:
                return func(this, other)
            else:
                raise ValueError("Unable to do this action, invalid matrices!")

        return wrapper

    @staticmethod
    def only_squared(func: Callable[[Matrix, Any], Any]) -> Callable[[Matrix, Any], Any]:
        @wraps(func)
        def wrapper(matrix: Matrix, *args: Any, **kwargs: Any) -> Any:
            if matrix.is_square:
                return func(matrix, *args, **kwargs)
            else:
                raise ValueError("Matrix should be squared to do this action!")

        return wrapper

    @staticmethod
    def only_vector(func: Callable[[Matrix, Any], Any]) -> Callable[[Matrix, Any], Any]:
        @wraps(func)
        def wrapper(self, *args, **kwargs) -> Any:
            if self.is_row_vector() or self.is_column_vector():
                return func(self, *args, **kwargs)
            else:
                raise ValueError("Matrix should be vector to do this action!")

        return wrapper

    @staticmethod
    def only_invertible(func: Callable[[Matrix, Any], Any]) -> Callable[[Matrix, Any], Any]:
        @wraps(func)
        def wrapper(self, *args, **kwargs) -> Any:
            if self.determinant() != 0:
                return func(self, *args, **kwargs)
            else:
                raise ValueError("Matrix should be invertible to do this action!")

        return wrapper

    @staticmethod
    def only_able_to_power(func: Callable[[Matrix, int], Any]) -> Callable[[Matrix, int], Any]:
        @wraps(func)
        def wrapper(self, power, *args, **kwargs) -> Any:
            if power % 1 == 0:
                return func(self, power, *args, **kwargs)
            else:
                raise ValueError("Power should be a whole number to do this action!")

        return wrapper

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

    @only_squared
    def sub_matrix(self, row: int = -1, column: int = -1) -> Matrix:
        submatrix = np.delete(np.delete(self.raw_matrix, row, axis=0), column, axis=1)
        return Matrix(submatrix)

    @only_squared
    def minor(self, row: int, column: int) -> int | float:
        if self.__rows_number == 1 and self.__columns_number == 1:
            minor = self.determinant()
        else:
            minor = self.sub_matrix(row, column).determinant()
        return minor

    @only_squared
    def adjunct(self, row: int, column: int) -> int | float:
        adjunct = (-1) ** (row + column) * self.minor(row, column)
        return adjunct

    @only_squared
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
            return round(determinant, 6)

    @only_squared
    def cofactor(self) -> Matrix:
        cofactor_matrix = np.array([[round(self.adjunct(row, column), 6)
                                     for column in range(self.raw_matrix.shape[1])]
                                    for row in range(self.raw_matrix.shape[0])])
        return Matrix(cofactor_matrix)

    @only_squared
    @only_invertible
    def __invert__(self) -> Matrix:
        determinant = self.determinant()
        transposed_cofactor_matrix = self.cofactor().transpose()
        inverse = transposed_cofactor_matrix * (1 / determinant)
        return inverse

    @only_able_to_power
    @only_squared
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
