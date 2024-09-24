from matrix import Matrix
from matrix import fill_matrix

class Coordinate:
   def __init__(self, x, y, clss):
      self.x = x
      self.y = y
      self.clss = clss
   def __str__(self):
      return f"Coordinate: ({self.x}, {self.y}) in Matrix {self.clss.rows_number} * {self.clss.columns_number}"
   def is_valid_coor(self):
      if self.x in range(self.clss.rows_number) and self.y in range(self.clss.columns_number):
         return True
      else:
         return False

   def up(self):
      if self.is_valid_coor():
         return Coordinate(self.x, self.y + 1, self.clss)
      else:
         return "Error"

   def down(self):
      if self.is_valid_coor():
         return Coordinate(self.x, self.y - 1, self.clss)
      else:
         return "Error"

   def right(self):
      if self.is_valid_coor():
         return Coordinate(self.x + 1, self.y, self.clss)
      else:
         return "Error"

   def left(self):
      if self.is_valid_coor():
         return Coordinate(self.x - 1, self.y, self.clss)
      else:
         return "Error"

# function opportunity_actions in development
'''
   def opportunity_actions(self):
      if self.x == 0:
         if self.y == 0:
            self.down()
            self.right()
         elif self.x == self.clss.columns_number:
            self.down()
            self.left()
         else:
            self.down()
            self.right()
            self.left()
      if self.x == self.clss.rows_number:
         if self.y == 0:
            self.up()
            self.right()
         elif self.x == self.clss.columns_number:
            self.up()
            self.left()
         else:
            self.up()
            self.right()
            self.left()
      else:
         self.up()
         self.down()
         self.right()
         self.left()
'''
''' Input as an example:
Enter x: 2
Enter y: 3
Enter number of rows: 4
Enter number of columns: 4
2 3 4 1
8 9 2 6
2 4 5 9
8 1 3 2
'''
x_coor =int(input('Enter x: '))
y_coor =int(input('Enter y: '))
m = int(input('Enter number of rows: '))
n = int(input('Enter number of columns: '))
b = Coordinate(x_coor, y_coor, Matrix(m, n, fill_matrix(m)))
print(b.is_valid_coor())
print(b.left())