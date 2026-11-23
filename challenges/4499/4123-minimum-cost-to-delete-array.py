'''
4123-minimum-cost-to-delete-array
'''


class Solution:
  '''
  essentially we need to find the pairs as the pairs of the
  subarray to delete from.

  the problem is now to find the series of even number of elements
  that sum to the minimum cost
  '''
  def minCost(self, nums: list[int]) -> int:
    even = 0
    odd = float('inf')
    n = len(nums)

    for i in range(1, n-1):
      val = nums[i]
      pe = even
      po = odd
      even = min(even, po+val)  # odd series + current value -> even series
      odd = min(odd, pe+val)    # even series + current value -> odd series

    return nums[0] + nums[-1] + even
        