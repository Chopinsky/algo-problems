'''
2778-sum-of-squares-of-special-elements
'''


class Solution:
  def sumOfSquares(self, nums: List[int]) -> int:
    n = len(nums)
    cand = list(val*val if n%(i+1) == 0 else 0 for i, val in enumerate(nums))
    # print('cand', cand)
    return sum(cand)
