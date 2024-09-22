from functools import cache
def fill_matrix(row_num):
   matrix_list = []
   for num in range(row_num):
      row_list = [float(elem) for elem in input().split(" ")]
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
   def __init__(self, m, n, string):
      self.m = m
      self.n = n
      self.string = string
   def __del__(self):
      del self
   def view(self):
       for i in self.string:
          print(i)
   def transpon_fun(self):
      a = [[i[k] for i in self.string] for k in range(self.n)]
      return a
   def multiply_num_matr_fun(self, numer):
      a = [[i*numer for i in k] for k in self.string]
      return a

   def determinant(self):
      if self.m != self.n:
         return "Cannot find a determinant for a non-square matrix"

      if self.m == 1:
         return self.string[0][0]

      if self.m == 2:
         return self.string[0][0] * self.string[1][1] - self.string[0][1] * self.string[1][0]

      determinant_sum = 0
      for i in range(self.m):
         sub_matrix = []
         for row in range(1, self.m):
            sub_row = []
            for col in range(self.n):
               if col != i:
                  sub_row.append(self.string[row][col])
            sub_matrix.append(sub_row)

         minor = Matrix(self.m - 1, self.n - 1, sub_matrix).determinant()
         determinant_sum += (-1) ** i * self.string[0][i] * minor

      return determinant_sum
   def cofactor (self):
      if self.m != self.n:
         return "Cannot find a cofactor for a non-square matrix"
      cofactor_matrix = []
      for i in range(self.m):
         cofactor_row = []
         for j in range(self.n):
            # Create the minor matrix by removing row i and column j
            sub_matrix = []
            for row in range(self.m):
               if row != i:
                  sub_row = []
                  for col in range(self.n):
                     if col != j:
                        sub_row.append(self.string[row][col])
                  sub_matrix.append(sub_row)

            # Find the determinant of the minor
            minor = Matrix(self.m - 1, self.n - 1, sub_matrix).determinant()

            # Calculate the cofactor element
            cofactor_element = (-1) ** (i + j) * minor
            cofactor_row.append(cofactor_element)
         cofactor_matrix.append(cofactor_row)
      return Matrix(self.m, self.n, cofactor_matrix)
   def inverse_matrix(self):
      determinant = self.determinant()
      if determinant == 0:
         return "Cannot be inversed, because determinant equals to zero"
      transponed_cofactor_matrix = Matrix(self.m, self.n, self.cofactor().transpon_fun())
      inverse = transponed_cofactor_matrix.multiply_num_matr_fun(1/determinant)
      return Matrix(self.m, self.n, inverse)
   def __pow__(self, n):
      if self.m != self.n:
         return "Cannot raise a non-square matrix to a power"
      # Initialize the result as the identity matrix
      result = Matrix(self.m, self.n, [[1 if i == j else 0 for j in range(self.n)] for i in range(self.m)])
      base = self
      # Exponentiation by squaring
      while n > 0:
         if n % 2 == 1:
            result = result * base
         base = base * base
         n //= 2

      return result

   def __str__(self):
      return '\n'.join([' '.join(map(str, row)) for row in self.string])
   @classmethod
   def transpon_matrix_class(cls, self):
      return cls(len(self.transpon_fun()), len(self.transpon_fun()[0]), self.transpon_fun())
   @classmethod
   def multiply_matrix_class(cls, self, n):
      return cls(len(self.multiply_num_matr_fun(n)), len(self.multiply_num_matr_fun(n)[0]), self.multiply_num_matr_fun(n))
   def __add__(self, other):
      if self.m == other.m and self.n == other.n:
         for k in self.string:
            for i in k:
               var = [[i + n for n in m] for m in other.string]
         return Matrix(self.m, self.n, var)
   def __eq__(self, other):
      if self.string == other.string:
         return True
      else:
         return False
   def __mul__(self,other):
      if self.n == other.m:
         c = [[None for __ in range(other.n)] for __ in range(self.m)]
         for i in range(self.m):
            for j in range(other.n):
               c[i][j] = sum(self.string[i][k] * other.string[k][j] for k in range(other.m))
         return Matrix(self.m, other.n, c)
      else:
         return "Can not be multiplied"
class Coordinate:
   def __init__(self, x, y, clss):
      self.x = x
      self.y = y
      self.clss = clss
   def is_valid_coor(self):
      if self.x in range(self.clss.m) and self.y in range(self.clss.n):
         return True
      else:
         return False
   @classmethod
   def up(cls, self):
      if self.is_valid_coor():
         return cls(self.x, self.y + 1, self.clss)
      else:
         return "Error"
   @classmethod
   def down(cls, self):
      if self.is_valid_coor():
         return cls(self.x, self.y - 1, self.clss)
      else:
         return "Error"
   @classmethod
   def right(cls, self):
      if self.is_valid_coor():
         return cls(self.x + 1, self.y, self.clss)
      else:
         return "Error"
   @classmethod
   def left(cls, self):
      if self.is_valid_coor():
         return cls(self.x - 1, self.y, self.clss)
      else:
         return "Error"
   def possibility(self):
      if self.x == 0:
         if self.y == 0:
            self.down(self)
            self.right(self)
         elif self.x == self.clss.n:
            self.down(self)
            self.left(self)
         else:
            self.down(self)
            self.right(self)
            self.left(self)
      if self.x == self.clss.m:
         if self.y == 0:
            self.up(self)
            self.right(self)
         elif self.x == self.clss.n:
            self.up(self)
            self.left(self)
         else:
            self.up(self)
            self.right(self)
            self.left(self)
      else:
         self.up(self)
         self.down(self)
         self.right(self)
         self.left(self)

#input as example: [[2,3,1],[3,4,5],[3,7,9]]
m = int(input())
n = int(input())

a = Matrix(m, n, fill_matrix(m))
print(a.determinant())
print(a.inverse_matrix())
print(a.transpon_fun())
d = a.transpon_matrix_class(a)
print(a)
print((a**3).string)
if a==d:
   print('Ok')
else:
   print('No')
#print(d)
#input example: 4
print(d.multiply_num_matr_fun(5))
e = a.multiply_matrix_class(a,int(input("num: ")))
print(e.transpon_matrix_class(e).string)
result = a + d
print(f' New {result.string}')
b = Coordinate(2,1,d)
b.is_valid_coor()
f = b.up(b).y
h = b.up(b).x
print([f,h])
mult = a * result
print(mult.string)
