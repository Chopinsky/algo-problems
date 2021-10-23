'''
Suppose an array of length n sorted in ascending order is rotated 
between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] 
might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return 
the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, 
but nums may contain duplicates. Would this affect the runtime complexity? 
How and why?
'''


from typing import List


class Solution:
  def findMin(self, nums: List[int]) -> int:
    if nums[0] < nums[-1]:
      return nums[0]

    n = len(nums)
    if n <= 2:
      return min(nums)
    
    l, r = 0, n-1
    while l < r:
      # break the tie since this will lead to m == l, and for some test 
      # cases (where we assign r = m) it means infinite loop
      if l+1 == r:
        return min(nums[l], nums[r])
        
      m = (l+r) // 2
      
      # it's the /// or --/ or /-- shape, left-most element is the smallest
      if (nums[l] <= nums[m] < nums[r]) or (nums[l] < nums[m] <= nums[r]):
        break

      # if it's the --\ or /-\ shape
      if nums[l] == nums[m] > nums[r] or (nums[l] < nums[m] and nums[r] < nums[m]):
        l = m + 1
        continue
        
      # if it's the \-- shape
      if (nums[l] > nums[m] == nums[r]) or (nums[l] > nums[m] and nums[r] > nums[m]):
        r = m
        continue
        
      # complicate case: --- shape, must find the first non-uniform number
      # to decide the directions
      while l < m and nums[l] == nums[m]:
        l += 1

      while r > m and nums[r] == nums[m]:
        r -= 1
    
    return nums[l]
  