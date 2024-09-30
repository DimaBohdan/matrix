from matrix import Matrix, SquareMatrix

def space_separated_row_by_row(row_num: int) -> list:
   matrix_list = []
   for num in range(row_num):
      row_list = [float(elem) for elem in input('Input row: ').split(" ")]
      matrix_list.append(row_list)
   return matrix_list
text = input()
def space_separated(text: str) -> list:
   rows = text.split("\n")
   matrix_list = [row.split(" ") for row in rows]
   return matrix_list


