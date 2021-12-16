# Реализовать базовый класс Worker (работник)

class Worker:
  
  def __init__(self, name, surname, position, wage, bonus):
    self.name = name
    self.surname = surname
    self.position = position
    self._income = {"wage":wage, "bonus":bonus }
    
    
class Position(Worker):
  
  def FulName(self):
    return f"{self.name} {self.surname}"
  
  def zp(self):
    return(self._income["wage"] + self._income["bonu"])
  
  
my_stuff = Position("Теодор", "Рузвельт", "Кладовщик", 10000, 2000)
print( f"Всего причитается {my_stuff.FulName()} - {my_stuff.zp()}")    