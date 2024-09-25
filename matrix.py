from copy import deepcopy
def fill_matrix(row_num):
   matrix_list = []
   for num in range(row_num):
      row_list = [float(elem) for elem in input('Input row: ').split(" ")]
      matrix_list.append(row_list)
   return matrix_list

def fill(str):
   a = str.split(']')
   list = []
   list.append([i for i in a if i != ''])
   for i in list[0]:
      if ',[' in i:
         b = ',['
   c = []
   c.append(list[0][0].replace('[[', ""))
   l = [i.replace(b, '') for i in list[0][1:]]
   for i in l:
      c.append(i)
   new_lis = [i.split(",") for i in c]
   new = []
   for k in new_lis:
      new.append([int(i) for i in k])
   return new

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

   def sub_matrix(self, row, column):
      sub_matrix = deepcopy(self.raw_matrix)
      sub_matrix.remove(self.raw_matrix[row])
      for i in range(self.rows_number - 1):
         sub_matrix[i].pop(column)
      return Matrix(sub_matrix)

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

   def minor(self, row, column):
      if self.rows_number == 1 and self.columns_number == 1:
         minor =self.determinant()
      else:
         minor = self.sub_matrix(row, column).determinant()
      return minor

   def adjunct(self, row, column):
      adjunct = (-1) ** (row + column) * self.minor(row, column)
      return adjunct

   def determinant(self):
      if self.rows_number != self.columns_number:
         return "Cannot find a determinant for a non-square matrix"

      if self.rows_number == 1:
         return self.raw_matrix[0][0]

      if self.rows_number == 2:
         return self.raw_matrix[0][0] * self.raw_matrix[1][1] - self.raw_matrix[0][1] * self.raw_matrix[1][0]

      determinant = 0
      for row in self.range_rows_number:
         determinant += self.adjunct(row, 0) * self.raw_matrix[row][0]
      return determinant

   def cofactor (self):
      if self.rows_number != self.columns_number:
         return "Cannot find a cofactor for a non-square matrix"
      cofactor_matrix = []
      for row in self.range_rows_number:
         cofactor_row = [self.adjunct(row, column) for column in self.range_columns_number]
         cofactor_matrix.append(cofactor_row)
      return Matrix(cofactor_matrix)

   def inverse_matrix(self):
      determinant = self.determinant()
      if determinant == 0:
         return "Cannot be inversed, because determinant equals to zero"
      transposed_cofactor_matrix = self.cofactor().transpose()
      inverse = transposed_cofactor_matrix * (1 / determinant)
      return inverse
   def __pow__(self, n):
      if self.rows_number != self.columns_number or n <= 0:
         return "Cannot raise a non-square matrix to a power"
      # Initialize the result as the identity matrix
      power  = IdentityMatrix(self.rows_number, self.rows_number)
      while n > 0:
         if n % 2 == 1:
            power = power * self.origin
         self.origin *= self.origin
         n //= 2
      return power

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

class SquareMatrix(Matrix):
   def __init__(self, raw_matrix):
      super().__init__(raw_matrix)

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