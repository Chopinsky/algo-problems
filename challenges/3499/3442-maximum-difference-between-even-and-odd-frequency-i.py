'''
3442-maximum-difference-between-even-and-odd-frequency-i
'''

from collections import Counter


class Solution:
  def maxDifference(self, s: str) -> int:
    c = Counter(s)
    odd = max(val for val in c.values() if val%2 == 1)
    even = min(val for val in c.values() if val%2 == 0)
    # print('init:', odd, even)
    return odd - even
        