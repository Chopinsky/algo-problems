
'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 10 ** 4
-2 ** 31 <= nums[i] <= 2 ** 31 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    curr, cnt = nums[0], 1
    
    for val in nums[1:]:
      if val == curr:
        cnt += 1
        continue

      cnt -= 1
      if cnt == 0:
        curr = val
        cnt += 1
      
    return curr
        

  def majorityElement(self, nums: List[int]) -> int:
    count = 0
    cand = None
    
    for num in nums:
      if count == 0:
        cand = num
        
      count += (1 if num == cand else -1)
      
    return cand
  