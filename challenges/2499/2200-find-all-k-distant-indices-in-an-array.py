'''
2200-find-all-k-distant-indices-in-an-array
'''

from typing import List


class Solution:
  def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
    n = len(nums)
    cand = [i for i in range(n) if nums[i] == key]
    ans = []

    if not cand:
      return ans

    j = 0
    for i in range(n):
      while j < len(cand) and cand[j]+k < i:
        j += 1

      if j < len(cand) and abs(i-cand[j]) <= k:
        ans.append(i)

    return ans
        