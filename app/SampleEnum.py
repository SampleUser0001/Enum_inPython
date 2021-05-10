# -*- coding: utf-8 -*-
from enum import Enum

class SampleEnum(Enum):
  HOGE = ("HOGE",{
    "key":"hoge",
    "hoge":"hogehoge"
  })
  PIYO = ("PIYO",{
    "key":"piyo",
    "piyo":"piyopiyo"
  })

  def __init__(self, id, keys):
    self.id = id
    self.keys = keys
    # 変数名にvalueは使えない。
    
  def getId(self):
    return self.id
  
  def getKeys(self):
    return self.keys

  @classmethod
  def value_of(cls, id):
    for e in SampleEnum:
      if e.getId() == id:
        return e
    raise ValueError("{} is not found.".format(id))
