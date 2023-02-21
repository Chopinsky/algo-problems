'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
'''


from typing import List


class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 3:
      if n == 1:
        return nums[0]
      
      return nums[0] if nums[-1] == nums[-2] else nums[-1]

    if nums[0] != nums[1]:
      return nums[0]
    
    if nums[-1] != nums[-2]:
      return nums[-1]
      
    def check(idx: int) -> bool:
      val = nums[idx]
      vl = -1 if idx == 0 else nums[idx-1]
      vr = -1 if idx == n-1 else nums[idx+1]
      return val == vl or val == vr
      
    l, r = 0, n-1
    while l <= r:
      if not check(l):
        break
        
      if not check(r):
        l = r
        break
        
      mid = (l + r) // 2
      if not check(mid):
        l = mid
        break
      
      lc, rc = mid-l, r-mid
      
      # if even count of numbers, shift boundry
      # to make odd counts
      if lc != rc:
        if nums[l] == nums[l+1]:
          r += 1
        else:
          l -= 1
          
        continue
        
      if (lc%2 == 0 and nums[mid] != nums[mid-1]) or (lc%2 == 1 and nums[mid] == nums[mid-1]):
        l = mid+1
      else:
        r = mid-1
      
    return nums[l]
    

  def singleNonDuplicate(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
      return nums[0]
    
    l, r = 0, n
    
    def check(i: int) -> bool:
      # print(i, n)
      return (i == 0 and nums[i] != nums[i+1]) or (i == n-1 and nums[i] != nums[i-1]) or (0 < i < n-1 and nums[i] != nums[i+1] and nums[i] != nums[i-1])
    
    while l < r:
      m = (l + r) // 2
      # print(l, m, r)
      
      if check(m):
        return nums[m]
      
      if (m-l) % 2 == 0:
        if nums[m] == nums[m+1]:
          l = m+2
        else:
          r = m-2
        
      else:
        if nums[m] == nums[m+1]:
          r = m-1
        else:
          l = m+1
        
    # print('out', l, r)
    return nums[l] if check(nums[l]) else nums[r]
  