'''
1523-Count-Odds-in-an-Interval-Range
'''


class Solution:
  def countOdds(self, low: int, high: int) -> int:
    if low == high:
      return 1 if low%2 == 1 else 0

    if low%2 == 0:
      low += 1

    cnt = high-low

    return 1+cnt//2
        