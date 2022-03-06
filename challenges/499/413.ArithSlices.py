'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
'''


from typing import List


class Solution:
  def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
      return 0
    
    cnt = 0
    start = 0
    diff = 0
    # print([nums[i]-nums[i-1] for i in range(1, n)])
    
    for i in range(1, n):
      if i == start+1:
        diff = nums[i] - nums[i-1]
        continue
        
      if nums[i]-nums[i-1] == diff:
        cnt += i-start-1
        # print(i, start)
        continue
        
      start = i-1
      diff = nums[i]-nums[i-1]
      
    return cnt
    