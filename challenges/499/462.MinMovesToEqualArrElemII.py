
'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:

Input: nums = [1,10,2,9]
Output: 16

Constraints:

n == nums.length
1 <= nums.length <= 10 ** 5
-10 ** 9 <= nums[i] <= 10 ** 9
'''

from typing import List
import math


class Solution:
  def minMoves2(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    ls, rs = 0, sum(nums)
    moves = math.inf
    
    for i, val in enumerate(nums):
      ls += val
      rs -= val
      moves = min(moves, abs(ls - (i+1)*val) + abs(rs - (n-i-1)*val))
    
    return moves
    

  def minMoves2(self, nums: List[int]) -> int:
    n = len(nums)
    nums.sort()

    presums = [nums[i] for i in range(n)]
    for i in range(1, n):
      presums[i] += presums[i-1]

    # print(nums, presums)
    ans = -1

    for i in range(n):
      if i == 0:
        moves = presums[-1] - n*nums[0]
      elif i == n-1:
        moves = n*nums[-1] - presums[-1]
      else:
        moves = ((i+1)*nums[i] - presums[i]) + \
            ((presums[-1]-presums[i]) - (n-i-1)*nums[i])

      if ans < 0 or moves < ans:
        ans = moves

    return ans
