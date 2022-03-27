'''
You are given an integer array nums. In one move, you can choose one element of nums and change it by any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

from typing import List


class Solution:
  def minDifference(self, nums: List[int]) -> int:
    if len(nums) <= 4:
      return 0
    
    nums.sort()
    
    return min(
      nums[-4] - nums[0],
      nums[-3] - nums[1],
      nums[-2] - nums[2],
      nums[-1] - nums[3]
    )
    