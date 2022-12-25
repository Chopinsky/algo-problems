'''
912. Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:

1 <= nums.length <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
'''

from typing import List


class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    def merge_sort(src: List[int]):
      n = len(src)
      if n <= 2:
        if n == 2 and src[0] > src[1]:
          src[0], src[1] = src[1], src[0]
          
        return src
      
      sorted = True
      for i in range(1, n):
        if src[i] < src[i-1]:
          src[i], src[i-1] = src[i-1], src[i]
          sorted = False

      if sorted:
        return src

      a = merge_sort(src[:n//2])
      b = merge_sort(src[n//2:])
      
      ans = []
      i, j = 0, 0
      na, nb = len(a), len(b)
            
      while i < na or j < nb:
        if i >= na:
          ans += b[j:]
          break
          
        if j >= nb:
          ans += a[i:]
          break
          
        if a[i] <= b[j]:
          ans.append(a[i])
          i += 1
          
        else:
          ans.append(b[j])
          j += 1
        
      return ans
    
    return merge_sort(nums)
    