# Реализовать проект расчета суммарного расхода ткани на производство одежды. 
from abc import ABC, abstractmethod

class Clothes(ABC):
  
  def __init__(self, a):
    self.a = a
    
  @abstractmethod
  def rashod(self):
    pass
  
class Coat(Clothes):
      
  def __init__(self, a):
    super().__init__(a)
    print(f"пальто размером {self.a}")
      
  @property
  def rashod(self):
    return round(self.a/6.5 + 0.5, 2)

class Suit(Clothes):
      
  def __init__(self, a):
    super().__init__(a)
    print(f"костюм с ростом {self.a}")
      
  @property
  def rashod(self):
    return round(self.a * 2 + 0.3, 2)
  
my_coat = Coat(56)
print(f"На пальто указанного размера требуется {my_coat.rashod}")
my_suit = Suit(1.82)
print(f"На костюм указанного роста требуется {my_suit.rashod}")
print(f"Всего требуется {my_suit.rashod + my_coat.rashod}")
    