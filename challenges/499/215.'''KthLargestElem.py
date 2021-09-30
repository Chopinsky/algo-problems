'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
'''


class Solution:
  '''
  https://en.wikipedia.org/wiki/Quickselect
  '''
  def findKthLargest(self, nums: List[int], k: int) -> int:
    def quick(l: int, r: int, k: int) -> int:
      p = (max(nums[l:r+1]) + min(nums[l:r+1])) / 2.0
      i, j = l, r
      
      while i < j:
        while nums[i] <= p and i < r:
          i += 1
          
        while nums[j] > p and j > l:
          j -= 1
          
        if i >= j:
          break
          
        nums[i], nums[j] = nums[j], nums[i]
        
      count = r-i+1
      # print(k, count, i, j, nums)
      
      if count == k:
        return min(nums[i:r+1])
      
      if count > k:
        return quick(i, r, k)
      
      return quick(l, j, k-count)
      
      '''
      p = l
      for i in range(l, r+1):
        # put all numbers smaller than p to the left
        if nums[i] <= nums[r]:
          nums[p], nums[i] = nums[i], nums[p]
          p += 1
          
      nums[p], nums[r] = nums[r], nums[p]
      
      # total amount of numbers that are > pivot
      count = r-p+1
      
      # correct amount in the right, the p-th element
      # is the k-th largest
      if count == k:
        return nums[p]
      
      # too many elements in the right of the pivot, 
      # get a smaller search range
      if count > k:
        return quick(p+1, r, k)
      
      # too little in the right of the pivot, find the 
      # corresponding one from the left of the array
      return quick(l, p-1, k-count)
      '''
      
    return quick(0, len(nums)-1, k)
    
