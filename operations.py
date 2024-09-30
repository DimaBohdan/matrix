from matrix import Matrix, SquareMatrix, IdentityMatrix, raw_matrix_type, matrices_types
from typing import Union

def square_checker(raw_matrix: raw_matrix_type) -> bool:
    if len(raw_matrix) == len(raw_matrix[0]):
        return True
    return False

def multiply_scalar(matrix: matrices_types, scalar: [int, float]) -> matrices_types:
    multiply = [[i * scalar for i in k] for k in matrix.raw_matrix]
    result = (SquareMatrix(multiply) if square_checker(multiply) else Matrix(multiply))
    return result

def multiply_matrix(this: matrices_types, other: matrices_types) -> matrices_types:
    if this.columns_number == other.rows_number:
        multiply = []
        for row in range(this.rows_number):
            multiply_row = []
            for column in range(other.columns_number):
                multiply_elem = sum(
                    this.raw_matrix[row][k] * other.raw_matrix[k][column] for k in range(other.rows_number))
                multiply_row.append(multiply_elem)
            multiply.append(multiply_row)
        return Matrix(multiply)
    else:
        raise Exception("Can not be multiplied")

def __add__(this: matrices_types, other: matrices_types) -> matrices_types:
    if this.rows_number == other.rows_number and this.columns_number == other.columns_number:
        var = []
        for k in this.raw_matrix:
            for i in k:
               var = [[i + n for n in m] for m in other.raw_matrix]
        return Matrix(var)

def __eq__(this: matrices_types, other: matrices_types) -> bool:
    if this.raw_matrix == other.raw_matrix:
        return True
    else:
        return False

def __pow__(square_matrix: SquareMatrix, power: int) -> SquareMatrix:
    if power <= 0:
        raise Exception("Cannot raise a matrix to the negative power")
        # Initialize the result as the identity matrix
    power = IdentityMatrix(square_matrix.rows_number, square_matrix.rows_number)
    while power > 0:
        if power % 2 == 1:
            power = power * square_matrix.origin
        square_matrix.origin *= square_matrix.origin
        power //= 2
    return power
def inverse_matrix(square_matrix: SquareMatrix) -> SquareMatrix:
    determinant = square_matrix.determinant()
    if determinant == 0:
        raise Exception("Cannot be inversed, because determinant equals to zero")
    transposed_cofactor_matrix = square_matrix.cofactor().transpose()
    inverse = multiply_scalar(transposed_cofactor_matrix, 1/determinant)
    return inverse