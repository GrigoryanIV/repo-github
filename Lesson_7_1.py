# Реализовать класс Matrix (матрица). 

class Matrix:
  
  def __init__(self, matrix):
    self.matrix = matrix
    
    
  def __str__(self):
    my_str = "\n"
    for row in self.matrix:
      my_str += "\n"
      for el in row:
        my_str += str(el)
        my_str += " "
    return my_str
      
    
  def __add__(self, another):
    matr1 = []
    for i in range(len(self.matrix)):
      matr2 = []
      for j in range(len(self.matrix[i])):
        matr2.append(self.matrix[i][j]+ another.matrix[i][j])
      matr1.append(matr2)
    return Matrix(matr1)
  
m1 = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
m2 = Matrix([[5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [15, 14, 13, 12, 11]])
m3 = m1+m2
print (m3)
  
    