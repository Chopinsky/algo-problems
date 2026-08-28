'''
3909-compare-sums-of-bitonic-parts
'''


class Solution:
  def compareBitonicSums(self, nums: list[int]) -> int:
    val = max(nums)
    idx = nums.index(val)
    prefix = sum(nums[:idx+1])
    suffix = sum(nums[idx:])
    # print('init:', val, idx, prefix, suffix)

    if prefix == suffix:
      return -1

    return 0 if prefix > suffix else 1
    
        