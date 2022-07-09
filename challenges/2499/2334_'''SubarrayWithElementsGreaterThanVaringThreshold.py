'''
You are given an integer array nums and an integer threshold.

Find any subarray of nums of length k such that every element in the subarray is greater than threshold / k.

Return the size of any such subarray. If there is no such subarray, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,3,4,3,1], threshold = 6
Output: 3
Explanation: The subarray [3,4,3] has a size of 3, and every element is greater than 6 / 3 = 2.
Note that this is the only valid subarray.
Example 2:

Input: nums = [6,5,6,5,8], threshold = 7
Output: 1
Explanation: The subarray [8] has a size of 1, and 8 > 7 / 1 = 7. So 1 is returned.
Note that the subarray [6,5] has a size of 2, and every element is greater than 7 / 2 = 3.5. 
Similarly, the subarrays [6,5,6], [6,5,6,5], [6,5,6,5,8] also satisfy the given conditions.
Therefore, 2, 3, 4, or 5 may also be returned.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i], threshold <= 10^9
'''

from typing import List


class Solution:
  '''
  the trick is to find the longest subarray (assuming with length k) for each index of the 
  array, such that the element at this index is the minimum element of the subarray; then
  we can compare the threshold of the longest subarray at each index: if `nums[i] > threshold / k`,
  then `k` is a subarray length that will satisfy the requirement. 

  to calculate the subarray length, we can use monotonic increamental array: calculate the 
  first element to the left/right of the current index that is smaller, then add the number of
  elements in between, that will get us the size of the subarray where the minimum value of it is
  the element at index-i.
  
  time complexity is O(3*n) -> O(n), memory complexity is O(n)
  '''
  def validSubarraySize(self, nums: List[int], th: int) -> int:
    n = len(nums)
    stack, size = [], [1]*n
    
    for i, val in enumerate(nums):
      # pop all elements that are greater or equal to `val`
      while stack and stack[-1][0] >= val:
        stack.pop()
    
      # the index of the first element to the left that is smaller
      j = -1 if not stack else stack[-1][1]

      # add # of elements between
      size[i] += i-j-1

      # push the element to the stack
      stack.append((val, i))
      
    # print('left', size)
    stack.clear()
    
    for i in range(n-1, -1, -1):
      val = nums[i]

      # pop all elements that are greater or equal to `val`
      while stack and stack[-1][0] >= val:
        stack.pop()
        
      # the index of the first element to the right that is smaller
      j = n if not stack else stack[-1][1]

      # add # of elements between
      size[i] += j-i-1

      # push the element to the stack
      stack.append((val, i))
      
    # print('fin:', size)
    # loop through all indexs and find the elements that is the smallest
    # element in the subarray with length of size[i], and compare it with
    # the threshold requirements.
    for i, k in enumerate(size):
      if nums[i] > th/k:
        return k
    
    # no element satisfy the requirements, fail
    return -1
    