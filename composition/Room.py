import math
class Win_Door: # �������� ������ Win_Door
  def __init__(self,x,y): # �����������
    self.square = x*y
class Room: # �������� ������ Room
  def __init__(self,width,lenght,height): # �����������
    self.width = width
    self.lenght = lenght
    self.height = height
    self.wd = []
  def square(self): # �������-����� 1: ���������� ����� �������
    self.squares = 2*self.height*(self.width+self.lenght)
    return self.squares
  def addWD(self,w,h): # �������-����� 2: ���������� ����/����� � ������
    self.wd.append(Win_Door(w,h))
  def workSurface(self): # �������-����� 3: ���������� ����������� �������
    new_square = self.squares
    for i in self.wd:
      new_square -=i.square
    return new_square
