from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List
import json


class EnumType(Enum):
  TypeOne = auto()
  TypeTwo = auto()


@dataclass
class Product:
  name: str
  price: float
  quantity: int = 0
  tags: List[str] = field(default_factory=list)


if __name__ == '__main__':
  val = EnumType.TypeOne
  item = Product('laptop', 1200.50, 1, ['tag'])
  print('done', val, val.value, EnumType.TypeTwo._name_, item)
  path = './main1.py'

  import os
  if not os.path.exists(path) or not os.path.isfile(path):
    raise ValueError('not valid path')
  
  try:
    with open(path, 'r', encoding='utf-8') as f:
      for line in f.readlines():
        try:
          data = json.loads(line)
        except json.JSONDecodeError as e:
          print('error:', e)
          continue

        except OSError as e:
          print('os error:', e)
          continue

        except Exception as e:
          print('generic error:', e)
          continue

        print(line, data)

  except OSError as e:
    print(e)
