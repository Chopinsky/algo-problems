'''
3670-maximum-product-of-two-integers-with-no-common-bits
'''


class Solution:
  def maxProduct(self, nums: list[int]) -> int:
    k = max(nums).bit_length()
    mask =  1 << k
    dp = [0]*mask

    for val in nums:
      dp[val] = val

    for v0 in range(mask):
      if dp[v0]:
        continue

      for j in range(k):
        v1 = 1 << j

        # find the max value from all existing submask
        if v0 & v1:
          if dp[v0^v1] > dp[v0]:
            dp[v0] = dp[v0^v1]

    return max(val * dp[(mask-1)^val] for val in nums)
      