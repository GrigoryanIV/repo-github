# Реализовать класс Stationery (канцелярская принадлежность). 

class Stationary:
  
  def __init__(self, title):
    self.title = title
    
    
  def draw(self):
    print("Запуск отрисовки")
    
    
class Pen(Stationary):
   def draw(self):
     super().draw
     print(f"Рисуем {self.title}")
    
class Pencil(Stationary):
   def draw(self):
     super().draw
     print(f"Рисуем {self.title}")

class Handle(Stationary):
   def draw(self):
     super().draw
     print(f"Рисуем {self.title}")
     
pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
pen.draw()
pencil.draw()
handle.draw()