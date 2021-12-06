'''
You are given an integer array nums. The value of this array is defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.

Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68
 

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
'''

class Solution:
  def maxValueAfterReverse(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
      return 0
    
    if n == 2:
      return abs(nums[0] - nums[1])
    
    # min_vals = [0 if i == 0 else min(nums[i], nums[i-1]) for i in range(n)]
    diff = [0 if i == 0 else abs(nums[i]-nums[i-1]) for i in range(n)]
    src_sum = sum(diff)
    
    top, bottom = -math.inf, math.inf
    for i in range(1, n):
      top = max(top, min(nums[i], nums[i-1]))
      bottom = min(bottom, max(nums[i], nums[i-1]))

    max_inc = max(0, (top - bottom) * 2)
    
    for i in range(2, n):
      max_inc = max(max_inc, abs(nums[i]-nums[0]) - diff[i])
      
    for i in range(n-2, 0, -1):
      max_inc = max(max_inc, abs(nums[-1]-nums[i-1]) - diff[i])
    
    return src_sum + max_inc
    
