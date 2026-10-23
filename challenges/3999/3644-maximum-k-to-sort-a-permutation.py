'''
3644-maximum-k-to-sort-a-permutation
'''


class Solution:
  def sortPermutation(self, nums: list[int]) -> int:
    n = len(nums)
    cand = [val for i, val in enumerate(nums) if i != val]
    # print('init:', cand)

    if not cand:
      return 0
    
    res = cand[0]
    for val in cand[1:]:
      res &= val

    return res
        