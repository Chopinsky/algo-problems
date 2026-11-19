'''
3364-minimum-positive-sum-subarray
'''

class Solution:
  def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
    n = len(nums) 
    curr = sum(nums[:l])
    res = -1

    for i in range(n):
      sub = curr
      if sub > 0:
        if res >= 0:
          res = min(res, sub)
        else:
          res = sub          

      for j in range(l, r):
        if i+j >= n:
          break

        sub += nums[i+j]
        if sub > 0:
          if res >= 0:
            res = min(res, sub)
          else:
            res = sub

      if i+l >= n:
        break

      curr -= nums[i]
      curr += nums[i+l]

    return res
