'''
2681. Power of Heroes

You are given a 0-indexed integer array nums representing the strength of some heroes. The power of a group of heroes is defined as follows:

Let i0, i1, ... ,ik be the indices of the heroes in a group. Then, the power of this group is max(nums[i0], nums[i1], ... ,nums[ik])2 * min(nums[i0], nums[i1], ... ,nums[ik]).
Return the sum of the power of all non-empty groups of heroes possible. Since the sum could be very large, return it modulo 109 + 7.

Example 1:

Input: nums = [2,1,4]
Output: 141
Explanation: 
1st group: [2] has power = 22 * 2 = 8.
2nd group: [1] has power = 12 * 1 = 1. 
3rd group: [4] has power = 42 * 4 = 64. 
4th group: [2,1] has power = 22 * 1 = 4. 
5th group: [2,4] has power = 42 * 2 = 32. 
6th group: [1,4] has power = 42 * 1 = 16. 
​​​​​​​7th group: [2,1,4] has power = 42​​​​​​​ * 1 = 16. 
The sum of powers of all groups is 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141.

Example 2:

Input: nums = [1,1,1]
Output: 7
Explanation: A total of 7 groups are possible, and the power of each group will be 1. Therefore, the sum of the powers of all groups is 7.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''

from typing import List


class Solution:
  """
  first sort the array, then the formula you need to calculate is the following:
    sum(
      sum(
        x_i * (x_j**2) * (2**(max(j-i-2, 0))) 
        for i in range(j+1)
      ) 
      for j in range(n)
    )

  in this formula, first of all, we consider all sequences with (i, j) as the start
  and end index, and the number of such sequences is 2**(max(j-i-2, 0)), the sum of
  all these sequences equals x_i * (x_j**2) * (2**(max(j-i-2, 0))), and we need to
  add all (i, j) pairs in the array.

  the optimization happens to the prefix sum of the `sum(x_i * (2**(max(j-i-2, 0))))` part:
  say we have computed the sum for s_j, then s_(j+1) = x_j + 2*s_j, so we can iterate over
  index of j only.
  """
  def sumOfPower(self, nums: List[int]) -> int:
    nums.sort()
    prefix, total = 0, 0
    mod = 10**9 + 7
    
    for val in nums:
      # update the total
      total = (total + (prefix+val)*val*val) % mod

      # update the min-bound prefix
      prefix = (val + 2*prefix) % mod
    
    return total
        