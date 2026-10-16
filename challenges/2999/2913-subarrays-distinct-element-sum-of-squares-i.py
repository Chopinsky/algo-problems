'''
2913-subarrays-distinct-element-sum-of-squares-i
'''


class Solution:
  def sumCounts(self, nums: list[int]) -> int:
    n = len(nums)
    res = 0

    for i in range(n):
      s = set()
      for val in nums[i:]:
        s.add(val)
        ln = len(s)
        res += ln*ln
        
    return res
