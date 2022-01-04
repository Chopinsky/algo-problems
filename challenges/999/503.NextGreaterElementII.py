'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Constraints:

1 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
'''


from typing import List


class Solution:
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    n = len(nums)
    stack = []
    top = max(nums)
    greater = [None] * n
    
    for i, n0 in enumerate(nums[::-1]):
      if not stack:
        stack.append(n0)
        continue
        
      while stack and n0 >= stack[-1]:
        stack.pop()
        
      if stack:
        greater[n-1-i] = stack[-1]
        
      stack.append(n0)
      
    # print(greater)
    j = 0
    
    for i in range(n-1, -1, -1):
      if greater[i] != None or nums[i] == top:
        if nums[i] == top:
          greater[i] = -1
          
        continue
        
      while j < n and nums[j] <= nums[i]:
        j += 1
        
      if j < n and nums[j] > nums[i]:
        greater[i] = nums[j]
    
    return greater
      