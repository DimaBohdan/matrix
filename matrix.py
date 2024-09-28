from copy import deepcopy
from square_matrix import *

class Matrix:
   def __init__(self, raw_matrix: list[list[float]]):
      self.origin = self
      self.rows_number = len(raw_matrix)
      self.columns_number = len(raw_matrix[0])
      self.raw_matrix = raw_matrix
      self.range_rows_number = range(self.rows_number)
      self.range_columns_number = range(self.columns_number)
      self.is_square = (self.rows_number == self.columns_number)
      self.is_row_vector = (self.rows_number == 1)
      self.is_column_vector = (self.columns_number == 1)


   def transpose(self):
      transpose = [[i[elem] for i in self.raw_matrix] for elem in self.range_columns_number]
      return Matrix(transpose)

   def multiply_scalar(self, scalar):
      multiply_scalar = [[i * scalar for i in k] for k in self.raw_matrix]
      return Matrix(multiply_scalar)

   def multiply_matrix(self, other):
      if self.columns_number == other.rows_number:
         multiply_matrix = []
         for row in range(self.rows_number):
            multiply_row = []
            for column in range(other.columns_number):
               multiply_elem = sum(self.raw_matrix[row][k] * other.raw_matrix[k][column] for k in range(other.rows_number))
               multiply_row.append(multiply_elem)
            multiply_matrix.append(multiply_row)
         return Matrix(multiply_matrix)
      else:
            return "Can not be multiplied"

   def __str__(self):
      return '\n'.join([' '.join(map(str, row)) for row in self.raw_matrix])

   def __add__(self, other):
      if self.rows_number == other.rows_number and self.columns_number == other.columns_number:
         var = []
         for k in self.raw_matrix:
            for i in k:
               var = [[i + n for n in m] for m in other.raw_matrix]
         return Matrix(var)

   def __eq__(self, other):
      if self.raw_matrix == other.raw_matrix:
         return True
      else:
         return False

   def __mul__(self,other):
      if isinstance(other, Matrix):
         return self.multiply_matrix(other)
      elif isinstance(other, float) or isinstance(other, int):
         return self.multiply_scalar(other)

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


'''
Enter number of rows: 4
Enter number of columns: 4
2 3 4 1
8 9 2 6
2 4 5 9
8 1 3 2
'''
if __name__ == "__main__":
   m = int(input("Enter number of rows: "))
   #columns_number = int(input("Enter number of columns: "))
   a = SquareMatrix(fill_matrix(m))
   print(a.determinant())
   print(a.inverse_matrix())
   print(a.transpose())
   d = a.transpose()
   print(a)
   print((a**3).raw_matrix)
   if a==d:
      print('Ok')
   else:
      print('No')
#print(d)
#input example: 4
   print(d*5)
   e = a
   print(e.transpose().raw_matrix)
   result = a + d
   print(f' New {result.raw_matrix}')
#print([f,h])
   mult = a * result
   print(mult.raw_matrix)