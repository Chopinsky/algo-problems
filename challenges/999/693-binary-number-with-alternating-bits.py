'''
693-binary-number-with-alternating-bits
'''


mask = 0
vals = set[int]()

while mask < (1<<31):
  mask <<= 1
  mask |= 1
  vals.add(mask)
  
  mask <<= 1
  vals.add(mask)


class Solution:
  def hasAlternatingBits(self, n: int) -> bool:
    # print("init", vals)
    return n in vals

        