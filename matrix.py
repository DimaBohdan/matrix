from __future__ import annotations
from typing import Union, Generic
from copy import deepcopy
from functools import partial
from operations import Operator

raw_matrix_type = Union[list[list[float]], list[list[int]]]
def matrix_checker(raw_matrix):
   list_checker = all(isinstance(row, list) for row in raw_matrix)
   digit_checker = 0
   for row in raw_matrix:
      digit_checker = all(isinstance(elem, (int, float)) for elem in row)
      if not digit_checker:
         break
   if isinstance(raw_matrix, list) and list_checker and digit_checker:
      return True
   return False

class Matrix:
   def __init__(self, raw_matrix: raw_matrix_type):
      self.origin = self
      self.rows_number = len(raw_matrix)
      self.columns_number = len(raw_matrix[0])
      self.raw_matrix = raw_matrix
      self.range_rows_number = range(self.rows_number)
      self.range_columns_number = range(self.columns_number)
      self.is_square = (self.rows_number == self.columns_number)
      self.is_row_vector = (self.rows_number == 1)
      self.is_column_vector = (self.columns_number == 1)
      if not matrix_checker(self.raw_matrix):
         raise TypeError

   @property
   def transpose(self) -> matrices_types:
      transpose = [[i[elem] for i in self.raw_matrix] for elem in self.range_columns_number]
      return Matrix(transpose)

   def __str__(self) -> str:
      return '\n'.join([' '.join(map(str, row)) for row in self.raw_matrix])
   def __add__(self):
      return partial(Operator(self).__add__())

class SquareMatrix(Matrix):
   def __init__(self, raw_matrix):
      super().__init__(raw_matrix)
      if self.rows_number != self.columns_number:
         raise TypeError

   def sub_matrix(self, row: int, column: int) -> SquareMatrix:
      sub_matrix = deepcopy(self.raw_matrix)
      sub_matrix.remove(self.raw_matrix[row])
      for i in range(self.rows_number - 1):
         sub_matrix[i].pop(column)
      return SquareMatrix(sub_matrix)

   def minor(self, row: int, column: int) -> Union[int, float]:
      if self.rows_number == 1 and self.columns_number == 1:
         minor = self.determinant
      else:
         minor = self.sub_matrix(row, column).determinant
      return minor

   def adjunct(self, row: int, column: int) -> Union[int, float]:
      adjunct = round((-1) ** (row + column) * self.minor(row, column), 7)
      return adjunct

   @property
   def determinant(self) -> Union[int, float]:
      if self.rows_number == 1:
         return self.raw_matrix[0][0]

      if self.rows_number == 2:
         return (self.raw_matrix[0][0] * self.raw_matrix[1][1] -
                 self.raw_matrix[0][1] * self.raw_matrix[1][0])

      determinant = 0
      for row in self.range_rows_number:
         determinant += self.adjunct(row, 0) * self.raw_matrix[row][0]
      return round(determinant, 7)
   @property
   def cofactor(self) -> SquareMatrix:
      if self.rows_number != self.columns_number:
         raise Exception("Cannot find a cofactor for a non-square matrix")
      cofactor_matrix = []
      for row in self.range_rows_number:
         cofactor_row = [self.adjunct(row, column) for column in self.range_columns_number]
         cofactor_matrix.append(cofactor_row)
      return SquareMatrix(cofactor_matrix)


class IdentityMatrix(Matrix):
   def __init__(self, rows_number, columns_number):
      raw_matrix = []
      self.rows_number = rows_number
      self.columns_number = columns_number
      self.range_rows_number = range(self.rows_number)
      self.range_columns_number = range(self.columns_number)
      for row in self.range_rows_number:
         row = [1 if row == column else 0 for column in self.range_columns_number]
         raw_matrix.append(row)
      super().__init__(raw_matrix)

matrices_types = Union[Matrix, SquareMatrix]


'''
Enter number of rows: 4
Enter number of columns: 4
2 3 4 1
8 9 2 6
2 4 5 9
8 1 3 2
'''
if __name__ == "__main__":
   print(Matrix([[3, 4, 5], [2, 8.0, 7.1]]))
   print(SquareMatrix([[3, "4", 5], [2, 8.0, 7.1]]).transpose)
   function = getattr(Matrix([[3, 4]]), "transpose")
   print(function)
   m = int(input("Enter number of rows: "))
   #columns_number = int(input("Enter number of columns: "))
   #a = Matrix(input_handler.space_separated_row_by_row(m))
   #print(a.determinant())
   #print(a.inverse_matrix())
   #print(a.transpose())
   #d = a.transpose()
   #print(a)
   #print((a**3).func)
   #if a==d:
     # print('Ok')
   #else:
    #  print('No')
#print(d)
#input example: 3
   #print(d*5)
   #e = a
   #print(e.transpose().func)
   #result = a + d
   #print(f' New {result.func}')
#print([f,h])
   #mult = a * result
   #print(mult.func)