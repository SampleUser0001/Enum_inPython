# -*- coding: utf-8 -*-
import sys
sys.path.append('./')
from Color import Color
from SampleEnum import SampleEnum
from string_enum import StringEnum

if __name__ == '__main__':
  print(Color.RED.getId())

  sample_enum = SampleEnum.value_of('HOGE')
  print(sample_enum.getKeys())

  print(StringEnum.HOGE.value)