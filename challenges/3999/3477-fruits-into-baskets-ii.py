'''
3477-fruits-into-baskets-ii
'''

from typing import List


class Solution:
  def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
    n = len(fruits)
    used = set()
    rem = 0

    for f in fruits:
      done = False

      for i, cnt in enumerate(baskets):
        if i in used:
          continue

        if cnt < f:
          continue

        done = True
        used.add(i)
        break
        
      if not done:
        # print('??', f, used)
        rem += 1

    return rem
        