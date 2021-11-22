import math
class Win_Door: # создание класса Win_Door
  def __init__(self,x,y): # конструктор
    self.square = x*y
class Room: # создание класса Room
  def __init__(self,width,lenght,height): # конструктор
    self.width = width
    self.lenght = lenght
    self.height = height
    self.wd = []
  def square(self): # функция-метод 1: вычисление общей площади
    self.squares = 2*self.height*(self.width+self.lenght)
    return self.squares
  def addWD(self,w,h): # функция-метод 2: добавление окна/двери в список
    self.wd.append(Win_Door(w,h))
  def workSurface(self): # функция-метод 3: вычисление оклеиваемой площади
    new_square = self.squares
    for i in self.wd:
      new_square -=i.square
    return new_square
