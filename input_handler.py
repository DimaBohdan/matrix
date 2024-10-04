from logging import raiseExceptions
from matrix import Matrix, SquareMatrix, IdentityMatrix
from operations import multiply_scalar, multiply_matrix

def space_separated_row_by_row(row_num: int) -> list:
   matrix_list = []
   for num in range(row_num):
      row_list = [float(elem) for elem in input('Input row: ').split(" ")]
      matrix_list.append(row_list)
   return matrix_list

def space_separated(text: str) -> list:
   try:
      rows = text.split("\n")
      matrix_list = []
      for row in rows:
         matrix_list.append([float(elem) for elem in row.split(" ")])
      first_row_length = len(matrix_list[0])
      if not all(len(row) == first_row_length for row in matrix_list):
         raise ValueError
      return matrix_list
   except:
      raise ValueError
print(Matrix(space_separated('3 5 1\n8 7 2\n4 3 2')))
