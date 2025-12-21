'''
3100-water-bottles-ii
'''


class Solution:
  def maxBottlesDrunk(self, b: int, e: int) -> int:
    full = b
    empty = 0
    total = 0

    while full > 0 or empty >= e:
      while empty >= e:
        full += 1
        empty -= e
        e += 1

      total += full
      empty += full
      full = 0

    return total
