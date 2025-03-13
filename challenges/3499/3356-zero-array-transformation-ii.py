'''
3356-zero-array-transformation-ii
'''

from typing import List


class Solution:
  def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
    if all(val == 0 for val in nums):
      return 0
    
    m = len(nums)
    n = len(queries)
    l, r = 1, n+1

    def check(ln: int) -> bool:
      if ln > n:
        return True

      changes = [0]*m
      for l, r, val in queries[:ln]:
        changes[l] += val
        if r+1 < m:
          changes[r+1] -= val

      curr = 0
      for i, delta in enumerate(changes):
        curr += delta
        if curr < nums[i]:
          return False

      return True

    while l <= r:
      mid = (l+r) // 2
      if check(mid):
        r = mid-1
      else:
        l = mid+1

    return l if l <= n else -1 
