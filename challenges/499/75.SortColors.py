'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:

Input: nums = [0]
Output: [0]

Example 4:

Input: nums = [1]
Output: [1]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''

from typing import List

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    r, w, b = 0, 0, 0
    for c in nums:
      if c == 0:
        r += 1
      elif c == 1:
        w += 1
      else:
        b += 1
        
    for i in range(len(nums)):
      if i < r:
        nums[i] = 0
      elif i < r+w:
        nums[i] = 1
      else:
        nums[i] = 2
        
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    n = len(nums)
    l, r = 0, n-1
    while l < r and nums[l] == 0:
      l += 1

    while l < r and nums[r] == 2:
      r -= 1

    i = l
    # print(l, r)

    while i <= r:
      num = nums[i]
      # print(i, num, nums)

      if num == 0:
        if l == i:
          l += 1
          i += 1
          continue

        nums[l], nums[i] = nums[i], nums[l]
        l += 1
        continue

      if num == 2:
        nums[r], nums[i] = nums[i], nums[r]
        r -= 1
        continue

      i += 1
