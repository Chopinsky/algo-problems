'''
4011-count-subarrays-with-even-odd-ratio-i
'''

from sortedcontainers import SortedList
from bisect import bisect_right


class Solution:
  def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
    s = SortedList([0])
    curr = 0
    count = 0

    for num in nums:
      val = a if num%2 > 0 else -b
      curr += val
      idx = bisect_right(s, curr)
      count += idx
      s.add(curr)

    return count
        