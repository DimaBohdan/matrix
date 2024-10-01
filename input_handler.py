from matrix import Matrix, SquareMatrix
from operations import multiply_scalar, multiply_matrix

def space_separated_row_by_row(row_num: int) -> list:
   matrix_list = []
   for num in range(row_num):
      row_list = [float(elem) for elem in input('Input row: ').split(" ")]
      matrix_list.append(row_list)
   return matrix_list

def space_separated(text: str) -> list:
   rows = text.split("\n")
   matrix_list = []
   for row in rows:
      matrix_list.append([float(elem) for elem in row.split(" ")])
   return matrix_list

print(space_separated("""4 5 1
8 7 2
4 3 2"""))
