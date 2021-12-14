'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''


from typing import List


class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    zeros = []
    size = 0
    curr_size = 0
    
    for i, val in enumerate(nums):
      # none or 1 zero
      if val == 1 or not zeros:
        if val == 0:
          zeros.append(i)
        else:
          curr_size += 1
          size = max(size, curr_size)
          
      else:
        if len(zeros) == 2:
          size = max(size, i-zeros[0]-2)
          curr_size = i-zeros[1]-1
          zeros[0] = zeros[1]
          zeros[1] = i

        else:
          size = max(size, i-1)
          curr_size = i-zeros[0]-1
          zeros.append(i)
          
      # print(i, val, zeros, curr_size)
      
    return size - (1 if size == len(nums) else 0)
  