class Rolls:
  def __init__(self,len,wid): # создание класса Rolls
    self.len = len
    self.wid = wid
  def square(self,height,width,lenght): # функция-метод: площадь комнаты
    self.squares = 2*height*(width+lenght)
    return self.squares
  def roll(self): # функция-метод: количество рулонов для оклейки
    return math.ceil(self.squares/(self.len * self.wid))