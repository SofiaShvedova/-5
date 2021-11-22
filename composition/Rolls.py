 class Rolls:
   def __init__(self,len,wid): # создание класса Rolls
      self.len = len
      self.wid = wid
   def roll(self): # функция-метод: количество рулонов для оклейки
      return math.ceil(self.squares/(self.len * self.wid))
