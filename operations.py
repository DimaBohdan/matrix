import matrix
import math
from typing import Union

class Operator:
    def __init__(self):
        pass

    @staticmethod
    def square_checker(raw_matrix: matrix.raw_matrix_type) -> 'Matrix, SquareMatrix':
        if len(raw_matrix) == len(raw_matrix[0]):
            return matrix.SquareMatrix(raw_matrix)
        return matrix.Matrix(raw_matrix)

    @staticmethod
    def _multiply_scalar(matrix_arg, scalar: (list[Union[int, float]], Union[int, float])) -> 'Matrix, SquareMatrix':
        try:
            scalar = math.prod(scalar)
        except:
            raise TypeError
        multiply = [[i * scalar for i in k] for k in matrix_arg.raw_matrix]
        result = Operator.square_checker(multiply)
        return result

    @staticmethod
    def _multiply_matrix(argument: 'Matrix, SquareMatrix') \
            -> 'Matrix, SquareMatrix':
        this, other = argument
        if this.columns_number == other.rows_number:
            multiply = [
                [
                    sum(this.raw_matrix[row][common] * other.raw_matrix[common][col]
                        for common in other.range_rows_number)
                    for col in other.range_columns_number
                ]
                for row in this.range_rows_number
            ]
            result = Operator.square_checker(multiply)
            return result
        else:
            raise Exception("Can not be multiplied")

    @staticmethod
    def same_dimension(this: 'Matrix, SquareMatrix', other: 'Matrix, SquareMatrix'):
        if this.rows_number == other.rows_number and \
                this.columns_number == other.columns_number:
            return True
        return False

    @staticmethod
    def add(this: 'Matrix, SquareMatrix', other: 'Matrix, SquareMatrix') -> 'Matrix, SquareMatrix':
        if Operator.same_dimension(this, other):
            sum_raw_matrix = [
                [
                    this.raw_matrix[row][col] + other.raw_matrix[row][col]
                    for col in range(len(this.raw_matrix[0]))
                ]
                for row in range(len(this.raw_matrix))
            ]
            result = Operator.square_checker(sum_raw_matrix)
            return result
        else:
            raise TypeError

    @staticmethod
    def eq(this: 'Matrix, SquareMatrix', other: 'Matrix, SquareMatrix') -> bool:
        if not Operator.same_dimension(this, other):
            return False
        for i in this.range_rows_number:
            for j in this.range_columns_number:
                if this.raw_matrix[i][j] != other.raw_matrix[i][j]:
                    return False
        return True

    @staticmethod
    def mul(*args: Union['Matrix, SquareMatrix', int, float]) \
            -> 'Matrix, SquareMatrix':
        scalar = []
        matrix_args = []
        for arg in args:
            if isinstance(arg, (int, float)):
                scalar.append(arg)
            elif hasattr(arg, '__class__') and 'Matrix' in arg.__class__.__name__:
                matrix_args.append(arg)
            else:
                raise TypeError
        if (len(matrix_args) == 2) and  (scalar == []):
            return Operator._multiply_matrix(matrix_args)
        elif (len(matrix_args) == 1) and (scalar != []):
            return Operator._multiply_scalar(matrix_args[0],
                                        scalar)
        else:
            raise TypeError

    @staticmethod
    def pow(square_matrix: 'class SquareMatrix', power: int) -> 'class SquareMatrix':
        if power <= 0:
            raise Exception("Cannot raise a matrix to the power")
            # Initialize the result as the identity matrix
        result = matrix.IdentityMatrix(square_matrix.rows_number, square_matrix.rows_number)
        while power > 0:
            even_number = 2
            if power % even_number == 1:
                result = result * square_matrix.origin
            square_matrix.origin *= square_matrix.origin
            power //= even_number
        return matrix.SquareMatrix(result.raw_matrix)


#a = matrix.Matrix([[3,4,5], [2, 3, 1]])
#print(Operator._multiply_scalar(a, [5, 10, 12]))