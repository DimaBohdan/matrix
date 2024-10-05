from matrix import Matrix, SquareMatrix, IdentityMatrix, raw_matrix_type, matrices_types
from typing import Union

def square_checker(raw_matrix: raw_matrix_type) -> matrices_types:
    if len(raw_matrix) == len(raw_matrix[0]):
        return SquareMatrix(raw_matrix)
    return Matrix(raw_matrix)

def multiply_scalar(matrix: matrices_types, scalar: [int, float]) -> matrices_types:
    multiply = [[i * scalar for i in k] for k in matrix.raw_matrix]
    result = square_checker(multiply)
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
        result = square_checker(multiply)
        return result
    else:
        raise Exception("Can not be multiplied")

def __add__(this: matrices_types, other: matrices_types) -> matrices_types:
    if this.rows_number == other.rows_number and this.columns_number == other.columns_number:
        sum_raw_matrix = []
        for k in this.raw_matrix:
            for i in k:
               sum_raw_matrix = [[i + n for n in m] for m in other.raw_matrix]
        result = square_checker(sum_raw_matrix)
        return result

def __eq__(this: matrices_types, other: matrices_types) -> bool:
    if this.raw_matrix == other.raw_matrix:
        return True
    return False

def __mul__(this: matrices_types, other: Union[matrices_types, int, float]) -> matrices_types:
    if isinstance(other, Matrix):
        return multiply_matrix(this, other)
    elif isinstance(other, (float, int)):
        return multiply_scalar(this, other)

def __pow__(square_matrix: SquareMatrix, power: int) -> SquareMatrix:
    if power <= 0:
        raise Exception("Cannot raise a matrix to the negative power")
        # Initialize the result as the identity matrix
    power = IdentityMatrix(square_matrix.rows_number, square_matrix.rows_number)
    while power > 0:
        even_number = 2
        if power % even_number == 1:
            power = power * square_matrix.origin
        square_matrix.origin *= square_matrix.origin
        power //= even_number
    return SquareMatrix(power.raw_matrix)

def inverse_matrix(square_matrix: SquareMatrix) -> SquareMatrix:
    determinant = square_matrix.determinant
    if determinant == 0:
        raise Exception("Cannot be inversed, because determinant equals to zero")
    transposed_cofactor_matrix = square_matrix.cofactor.transpose
    inverse = multiply_scalar(transposed_cofactor_matrix, 1/determinant).raw_matrix
    result = square_checker(inverse)
    return result