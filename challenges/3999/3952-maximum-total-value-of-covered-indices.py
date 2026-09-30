'''
3952-maximum-total-value-of-covered-indices
'''


class Solution:
  def maxTotal(self, nums: list[int], s: str) -> int:
    n = len(nums)
    d0 = [0]*n
    d1 = [0]*n
      
    for i in range(n):
      t = s[i]

      # init
      if i == 0:
        if t == '1':
          d1[i] += nums[i]

        continue

      # not having the token initially
      if t == '0':
        d0[i] = max(d0[i-1], d1[i-1])
        continue

      # if stay
      d1[i] = max(d0[i-1], d1[i-1]) + nums[i]

      # if move, count the val from the prev cell
      d0[i] = d0[i-1] + nums[i-1]
      
    # print('done:', list(zip(d0, d1)))
    return max(d0[-1], d1[-1])
        