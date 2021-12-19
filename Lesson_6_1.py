# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск)
from time import sleep
class TrafficLight:
  colors = ("red", "yellow", "green")
  time_sec = (7,2,4)
  
  def __init__(self, color):
    self.__color = color
  
  def running(self):
    n = self.colors.index(self.__color)
    while True:
     print(self.colors[n])
     sleep(self.time_sec[n])
     n+=1
     if n == 3:
       n = 0

my_TrafficLight = TrafficLight("green")
my_TrafficLight.running()
 
    
    