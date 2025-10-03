'''
1518-water-bottles
'''


class Solution:
  def numWaterBottles(self, b: int, e: int) -> int:
    total = 0
    rem = 0

    while b > 0:
      total += b
      rem += b % e
      b //= e
      if rem >= e:
        rem %= e
        b += 1

    return total
        