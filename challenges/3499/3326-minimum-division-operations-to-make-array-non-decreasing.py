'''
3326-minimum-division-operations-to-make-array-non-decreasing
'''

from typing import List


siv = list(range(10**6+1))
for v0 in range(2, len(siv)):
  if siv[v0] < v0:
    continue

  for v1 in range(v0*v0, len(siv), v0):
    siv[v1] = min(siv[v1], v0)

class Solution:
  def minOperations(self, nums: List[int]) -> int:
    # print('init:', siv)
    idx = len(nums)-2
    ops = 0

    while idx >= 0:
      v0 = nums[idx]
      v1 = nums[idx+1]
      if v0 > v1:
        if siv[v0] > v1:
          return -1

        nums[idx] = siv[v0]
        ops += 1
        
      idx -= 1

    return ops

