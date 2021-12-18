# Реализовать класс Road (дорога)

class Road:
  
  def __init__(self, width, length):
    self._width = width
    self._length = length
  
  def square (self):
    return self._width * self._length
  
  def weight(self, p, h):
    return self.square() * p * h
  
 
my_road = Road(20,5000)
print(my_road.weight(25,1))
    
    