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
    n = len(nums)
    backup = [0]*n
    
    def swap(i, j):
      nums[i], nums[j] = nums[j], nums[i]
      
    def sort(i: int, j: int):
      if i >= j:
        return
      
      if i+1 == j:
        if nums[i] > nums[j]:
          swap(i, j)
        
        return
      
      mid = (i+j) // 2
      sort(i, mid)
      sort(mid+1, j)
      
      p0 = i
      p1 = mid+1
      p2 = i
      
      while p0 <= mid or p1 <= j:
        if p0 > mid:
          backup[p2] = nums[p1]
          p1 += 1
        elif p1 > j:
          backup[p2] = nums[p0]
          p0 += 1
        elif nums[p0] < nums[p1]:
          backup[p2] = nums[p0]
          p0 += 1
        else:
          backup[p2] = nums[p1]
          p1 += 1
          
        p2 += 1
      
      for idx in range(i, j+1):
        nums[idx] = backup[idx]
        
    sort(0, n-1)
    
    return nums
        
  def sortArray(self, nums: List[int]) -> List[int]:
    def mergeSort(i: int, j: int):
      if i >= j:
        return
      
      if i+1 == j:
        if nums[i] > nums[j]:
          nums[i], nums[j] = nums[j], nums[i]
          
        return
      
      # sort left and right
      mid = (i + j) // 2
      mergeSort(i, mid)
      mergeSort(mid+1, j)
      
      # merge left/right
      left = nums[i:mid+1].copy()
      right = nums[mid+1:j+1].copy()
      li, ri = 0, 0
      ln, rn = len(left), len(right)
      idx = i
      
      while li < ln or ri < rn:
        if li >= ln:
          nums[idx] = right[ri]
          ri += 1
          
        elif ri >= rn or left[li] <= right[ri]:
          nums[idx] = left[li]
          li += 1
          
        else:
          nums[idx] = right[ri]
          ri += 1
          
        idx += 1
        
    mergeSort(0, len(nums)-1)
    
    return nums
    

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
    