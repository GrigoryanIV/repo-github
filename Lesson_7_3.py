# Реализовать программу работы с органическими клетками.  

class Cell:
  
  def __init__(self, a):
    try:
      if a <=0:
        raise ValueError()
      self.a = int(a)
    except TypeError:
      self.a = 1
    except ValueError:
      self.a = 1
      
  def __add__(self, another):
    return Cell(self.a + another.a)
  
  def __sub__(self, another):
    if self.a - another.a > 0:
      return Cell(self.a - another.a)
    
  def __mull__(self, another):
    return Cell(self.a * another.a)
  
  def __truediv__(self, another):
    return Cell(self.a // another.a)
    
  def make_order(self, b):
    return (("*" * b) + "\n") * (self.a//b) +"*" * (self.a%b)
     
cell_1 = Cell(50)
cell_2 = Cell(35)

cell_3 = cell_1 + cell_2
print(cell_3.make_order(12))

cell_3 = cell_1 - cell_2
print(cell_3.make_order(12))

cell_3 = cell_1 / cell_2
print(cell_3.make_order(12))
 