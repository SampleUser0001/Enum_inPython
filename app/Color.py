# -*- coding: utf-8 -*-
from enum import Enum

class Color(Enum):
  RED = (1, '赤')
  GREEN = (2, '緑')
  BLUE = (3, '青')

  def __init__(self, id, ja):
    self.id = id
    self.ja = ja
    
  def getId(self):
    return self.id
  
  def getJa(self):
    return self.ja

if __name__ == "__main__":
  print('#=== ja ===#')
  print(Color.RED.getJa())
  print(Color.GREEN.getJa())
  print(Color.BLUE.getJa())
  # 使用可能だが、cloud9はエラーを上げてくる。
  print(Color.RED.ja)
