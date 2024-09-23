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
