'''
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.

Example 1:

Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0. 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''

from typing import List


class Solution:
  '''
  since we can only split a number and make the replacement numbers only smaller,
  the idea is that in the end, nums[i] <= nums[i+1] must be satisfied, and we can
  start scanning from right to left, replacing all nums[i] that are larger than nums[i+1];
  another trick is that we have to maximize the smallest number in the replacement numbers,
  i.e. minimize the necessity to further split nums[i-1]; to achieve this goal, we can maximize
  the average of the split numbers array: sum(arr) == v0, and len(arr) == div+1, then the max
  of the smallest number in this array is `v0 // (div+1)`, with `v0 % (div+1)` elements be +1 
  bigger as the number (i.e. `1 + (v0 // (div+1))`).
  '''
  def minimumReplacement(self, nums: List[int]) -> int:
    cnt = 0
    
    for i in range(len(nums)-2, -1, -1):
      v0, v1 = nums[i], nums[i+1]
      if v0 <= v1:
        continue
        
      # how many operations are necessary to reduce v0 to at most v1
      div = v0 // v1

      # v0 can be split into [v1] * div, we're done, and reduce div by 1
      # because each op will produce 2 numbers
      if v0 % v1 == 0:
        div -= 1
        nums[i] = v1

      # v0 will be split into [v0 // (div+1)] * div, with the v0 % (div+1) 
      # count of numbers towards the tail end of the array be +1 bigger, this 
      # will maximize the smallest number that will replace nums[i]
      else:
        nums[i] = v0 // (div+1)
        
      cnt += div
    
    # print(nums)
    return cnt