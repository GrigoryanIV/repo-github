# Реализуйте базовый класс Car

class Car:
  
  def __init__(self, speed, color, name, is_police):
    self.speed = speed
    self.name = name
    self.color = color
    self.is_police = is_police
    
  def go(self):
    print(f"Машина {self.color} {self.name} поехала ")
    
  def stop(self):
    print(f"Машина {self.color} {self.name} остановилась.")
    
  def turn(self, direction):
    print(f"Машина {self.color} {self.name} повернула на  {direction} ")
    
  def show_speed(self):
    print(f"Текущая скорость - {self.speed} ")
    
    
class TownCar(Cars):
   def show_speed(self):
     if self.speed > 60:
       print(f"Скорость превышена!")
     else:
       Cars.show_speed(self)
       
class SportCar(Cars):
  def __init__(self, speed, color, name):
    super().__init__(self, speed, color, name, is_police=False)

class WorkCar(Cars):
  
  def show_speed(self):
     if self.speed > 40:
       print(f"Скорость превышена!")
     
class PoliceCar(Cars):
  def __init__(self, speed, color, name):
    Cars.__init__(self, speed, color, name, is_police=True)
    
my_police_car = PoliceCar(120, "синий", "BMV")
my_police_car.go()
my_police_car.turn("право")
my_police_car.stop()
my_police_car.show_speed()
      
my_TownCar = TownCar(40, "белый", "RENO megan", False)
my_TownCar.go()
my_TownCar.turn("влево")
my_TownCar.stop()
my_TownCar.show_speed()  