class Rolls:
  def __init__(self,len,wid): # �������� ������ Rolls
    self.len = len
    self.wid = wid
  def square(self,height,width,lenght): # �������-�����: ������� �������
    self.squares = 2*height*(width+lenght)
    return self.squares
  def roll(self): # �������-�����: ���������� ������� ��� �������
    return math.ceil(self.squares/(self.len * self.wid))