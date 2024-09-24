
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
   def __init__(self, raw_matrix):
      self.rows_number = len(raw_matrix)
      self.columns_number = len(raw_matrix[0])
      self.raw_matrix = raw_matrix
      self.range_rows_number = range(self.rows_number)
      self.range_columns_number = range(self.columns_number)

   def transpose(self):
      transpose = [[i[elem] for i in self.raw_matrix] for elem in self.range_columns_number]
      return transpose

   def multiply_scalar(self, scalar):
      multiply_scalar = [[i * scalar for i in k] for k in self.raw_matrix]
      return multiply_scalar

   def determinant(self):
      if self.rows_number != self.columns_number:
         return "Cannot find a determinant for a non-square matrix"

      if self.rows_number == 1:
         return self.raw_matrix[0][0]

      if self.rows_number == 2:
         return self.raw_matrix[0][0] * self.raw_matrix[1][1] - self.raw_matrix[0][1] * self.raw_matrix[1][0]

      determinant_sum = 0
      for i in range(self.rows_number):
         sub_matrix = []
         for row in range(1, self.rows_number):
            sub_row = []
            for col in range(self.columns_number):
               if col != i:
                  sub_row.append(self.raw_matrix[row][col])
            sub_matrix.append(sub_row)

         minor = Matrix(self.rows_number - 1, self.columns_number - 1, sub_matrix).determinant()
         determinant_sum += (-1) ** i * self.raw_matrix[0][i] * minor
      return determinant_sum

   def cofactor (self):
      if self.rows_number != self.columns_number:
         return "Cannot find a cofactor for a non-square matrix"
      cofactor_matrix = []
      for i in range(self.rows_number):
         cofactor_row = []
         for j in range(self.columns_number):
            sub_matrix = []
            for row in range(self.rows_number):
               if row != i:
                  sub_row = []
                  for col in range(self.columns_number):
                     if col != j:
                        sub_row.append(self.raw_matrix[row][col])
                  sub_matrix.append(sub_row)
            minor = Matrix(self.rows_number - 1, self.columns_number - 1, sub_matrix).determinant()
            cofactor_element = (-1) ** (i + j) * minor
            cofactor_row.append(cofactor_element)
         cofactor_matrix.append(cofactor_row)
      return Matrix(self.rows_number, self.columns_number, cofactor_matrix)

   def inverse_matrix(self):
      determinant = self.determinant()
      if determinant == 0:
         return "Cannot be inversed, because determinant equals to zero"
      transponed_cofactor_matrix = Matrix(self.rows_number, self.columns_number, self.cofactor().transpose())
      inverse = transponed_cofactor_matrix.multiply_scalar(1 / determinant)
      return Matrix(self.rows_number, self.columns_number, inverse)
   def __pow__(self, n):
      if self.rows_number != self.columns_number:
         return "Cannot raise a non-square matrix to a power"
      # Initialize the result as the identity matrix
      result = Matrix(self.rows_number, self.columns_number, [[1 if i == j else 0 for j in range(self.columns_number)] for i in range(self.rows_number)])
      base = self
      while n > 0:
         if n % 2 == 1:
            result = result * base
         base = base * base
         n //= 2
      return result

   def __str__(self):
      return '\n'.join([' '.join(map(str, row)) for row in self.raw_matrix])


   def transpon_matrix_class(self):
      return Matrix(len(self.transpose()), len(self.transpose()[0]), self.transpose())

   def __add__(self, other):
      if self.rows_number == other.rows_number and self.columns_number == other.columns_number:
         for k in self.raw_matrix:
            for i in k:
               var = [[i + n for n in m] for m in other.raw_matrix]
         return Matrix(self.rows_number, self.columns_number, var)

   def __eq__(self, other):
      if self.raw_matrix == other.raw_matrix:
         return True
      else:
         return False

   def __mul__(self,other):
      if isinstance(other, Matrix):
         if self.columns_number == other.rows_number:
            c = [[None for __ in range(other.columns_number)] for __ in range(self.rows_number)]
            for i in range(self.rows_number):
               for j in range(other.columns_number):
                  c[i][j] = sum(self.raw_matrix[i][k] * other.raw_matrix[k][j] for k in range(other.rows_number))
            return Matrix(self.rows_number, other.columns_number, c)
         else:
            return "Can not be multiplied"
      elif isinstance(other, float) or isinstance(other, int):
         return Matrix(self.rows_number, self.columns_number, self.multiply_scalar(other))

class SquareMatrix(Matrix):
   def __init__(self, m, raw_matrix):
      super().__init__(m, m, raw_matrix)



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
   a = SquareMatrix(m, fill_matrix(m))
   print(a.determinant())
   print(a.inverse_matrix())
   print(a.transpose())
   d = a.transpon_matrix_class()
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
   print(e.transpon_matrix_class().raw_matrix)
   result = a + d
   print(f' New {result.raw_matrix}')
#print([f,h])
   mult = a * result
   print(mult.raw_matrix)
