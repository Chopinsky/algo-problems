'''
3911-k-th-smallest-remaining-even-integer-in-subarray-queries
'''

from bisect import bisect_left, bisect_right


class Solution:
  def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
    n = len(nums)
    idx = []
    evens = []

    for i, val in enumerate(nums):
      if val%2 == 0:
        idx.append(i)
        evens.append(val)

    def check(i: int, j: int, k: int, target: int) -> bool:
      '''
      find if more than k numbers available at or before `target`
      after removing overlapping vals from the [i, j] range in the
      `evens` array
      '''
      pos = bisect_right(evens, target, lo=i, hi=j+1)
      x = pos-i
      y = target//2 - x
      return y >= k

    res = []
    for l, r, k in queries:
      i = bisect_left(idx, l)
      j = bisect_right(idx, r)-1

      if i > j:
        # no evens in this interval, all seq
        # is available
        res.append(2*k)
        continue

      before = evens[i]//2 - 1
      if k <= before:
        # the removed evens are after the k-th
        res.append(2*k)
        continue

      total = j-i+1  # total evens in this range
      low, high = 1, k+total
      ans = 0

      while low <= high:
        mid = (low + high) // 2
        target = mid*2

        if check(i, j, k, target):
          ans = target
          high = mid-1
        else:
          low = mid+1
        
      res.append(ans)

    return res
      

        