'''
1394-find-lucky-integer-in-an-array
'''

from typing import List
from collections import Counter


class Solution:
  def findLucky(self, arr: List[int]) -> int:
    ans = -1
    c = Counter(arr)

    for val, cnt in c.items():
      if val == cnt:
        ans = max(ans, val)

    return ans
        