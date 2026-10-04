'''
3891-minimum-increase-to-maximize-special-indices
'''

class Solution:
  def minIncrease(self, nums: list[int]) -> int:
    n = len(nums)
    dp = [[0, 0] for _ in range(n)]

    def calc(i: int) -> int:
      if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        return 0

      return max(nums[i-1], nums[i+1]) + 1 - nums[i]

    for i in range(1, n-1):
      prev = i-2
      if prev >= 0:
        c0, o0 = dp[prev]
      else:
        c0, o0 = 0, 0

      # make the peak at index-i
      ops = calc(i)
      c0 += 1
      o0 += ops

      # don't make the peak
      c1, o1 = dp[i-1]
      # print('iter:', i, ops, (c0, o0), (c1, o1))

      # take the best
      if c0 == c1:
        dp[i][0] = c0
        dp[i][1] = min(o0, o1)
      elif c0 > c1:
        dp[i][0] = c0
        dp[i][1] = o0
      else:
        dp[i][0] = c1
        dp[i][1] = o1

    # print('done:', dp)
    return dp[n-2][1]
        