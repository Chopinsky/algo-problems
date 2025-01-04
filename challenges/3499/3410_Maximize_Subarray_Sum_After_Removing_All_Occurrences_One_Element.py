'''
3410. Maximize Subarray Sum After Removing All Occurrences of One Element

[-3,2,-2,-1,3,-2,3]
[1,2,3,4]
[-31,-23,-47]
'''

from typing import List
from bisect import bisect_left, bisect_right
from collections import defaultdict


class Solution:
  def maxSubarraySum(self, nums: List[int]) -> int:
    if all(val >= 0 for val in nums):
      return sum(nums)

    if all(val < 0 for val in nums):
      return max(nums)

    n = len(nums)
    tree = [None]*(4*n)
    pos = defaultdict(list)
    for i, val in enumerate(nums):
      pos[val].append(i)

    def iterate(i: int, l: int, r: int):
      if l > r:
        return [0, 0, 0, 0]

      if l == r:
        val = nums[l]
        tree[i] = [val, val, max(0, val), max(0, val)]
        return tree[i]

      mid = (l+r)//2
      lsb, lsum, lpf, lsf = iterate(2*i+1, l, mid)
      rsb, rsum, rpf, rsf = iterate(2*i+2, mid+1, r)
      curr_sb = lsb+rsb
      curr_sum = max(lsum, rsum, lsf+rpf, lsf+rsb, lsb+rpf)
      curr_prefix = max(0, lpf, lsb+rpf)
      curr_suffix = max(0, rsf, lsf+rsb)
      tree[i] = [curr_sb, curr_sum, curr_prefix, curr_suffix]
      
      return tree[i]

    def excl(i: int, l: int, r: int, idx: List):
      if l > r:
        return [0, 0, 0, 0]

      li = bisect_left(idx, l)
      ri = bisect_right(idx, r)-1

      # val not included in this subtree, done
      if li > ri or li >= len(idx):
        return tree[i]

      if l == r:
        return [0, 0, 0, 0]

      mid = (l+r)//2
      lsb, lsum, lpf, lsf = excl(2*i+1, l, mid, idx)
      rsb, rsum, rpf, rsf = excl(2*i+2, mid+1, r, idx)

      curr_sb = lsb+rsb
      curr_sum = max(lsum, rsum, lsf+rpf, lsf+rsb, lsb+rpf)
      curr_prefix = max(0, lpf, lsb+rpf)
      curr_suffix = max(0, rsf, lsf+rsb)
      return [curr_sb, curr_sum, curr_prefix, curr_suffix]

    iterate(0, 0, n-1)
    ans = tree[0][1]
    # print('init:', tree, ans)

    for val, idx in pos.items():
      if val >= 0:
        continue
      
      _, res, _, _ = excl(0, 0, n-1, idx)
      ans = max(ans, res)

    return ans
