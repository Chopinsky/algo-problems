'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''

from typing import List


class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    slow, fast = 0, 0
    init = True
    
    while init or slow != fast:
      init = False
      slow = nums[slow]
      fast = nums[nums[fast]]
      
    slow = 0
    while slow != fast:
      slow = nums[slow]
      fast = nums[fast]
      
    return slow
        
        
  def findDuplicate(self, nums: List[int]) -> int:
    # Find the intersection point of the two runners.
    fast, slow = nums[0], nums[0]
    while True:
      slow = nums[slow]
      fast = nums[nums[fast]]
      if slow == fast:
        break

    # Find the "entrance" to the cycle.
    slow = nums[0]
    while slow != fast:
      slow = nums[slow]
      fast = nums[fast]

    return slow
      
    
  def findDuplicate0(self, nums: List[int]) -> int:
    for val in nums:
      idx = abs(val) - 1
      if nums[idx] < 0:
        return abs(val)
      
      nums[idx] = -nums[idx]
      
    return -1
    
  