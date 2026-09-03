'''
4037-maximum-valid-split-positions-ii
'''

from math import gcd


class Solution:
  def maxValidSplits(self, nums: list[int]) -> int:
    n = len(nums)
    pre = [0]
    ans = 0

    for i, val in enumerate(nums):
      pre.append(gcd(pre[-1], val))

    def solve(skip: int) -> int:
      p = [0]*(n+1)
      s = [0]*(n+1)
      cnt = 0

      # calc prefix
      for i in range(1, 1+n):
        if i-1 == skip:
          p[i] = p[i-1]
        else:
          p[i] = gcd(p[i-1], nums[i-1])

      # calc suffix
      for i in range(n-1, -1, -1):
        if i == skip:
          s[i] = s[i+1]
        else:
          s[i] = gcd(s[i+1], nums[i])

      # count all prefix_i == suffix_i+1 positions
      for i in range(n-1):
        if i == skip:
          continue

        # valid split after removing i
        if p[i+1] == s[i+1]:
          cnt += 1
      
      return cnt

    for i in range(n+1):
      # not affecting the score, skip the scan
      if i > 0 and pre[i] == pre[i-1]:
        continue

      # calc the score with removing val here
      # solve(-1) does not remove any val from the nums
      ans = max(ans, solve(i-1))      

    return ans
