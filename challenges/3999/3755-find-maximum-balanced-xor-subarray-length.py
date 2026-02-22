'''
3755-find-maximum-balanced-xor-subarray-length
'''


class Solution:
  def maxBalancedSubarray(self, nums: list[int]) -> int:
    prefix = 0
    oc = 0
    ec = 0
    seen = {(0, 0): -1}
    dist = 0

    for i in range(len(nums)):
      val = nums[i]
      prefix ^= val
      if val%2 == 0:
        ec += 1
      else:
        oc += 1

      diff = ec-oc
      # print('prefix', prefix, diff)
      
      if (prefix, diff) in seen:
        dist = max(dist, i-seen[prefix, diff])
      else:
        seen[prefix, diff] = i

    return dist

        