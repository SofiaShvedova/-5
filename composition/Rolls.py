 class Rolls:
   def __init__(self,len,wid): # �������� ������ Rolls
      self.len = len
      self.wid = wid
   def roll(self): # �������-�����: ���������� ������� ��� �������
      return math.ceil(self.squares/(self.len * self.wid))
