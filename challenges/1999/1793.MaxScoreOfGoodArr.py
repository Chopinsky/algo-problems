'''
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 2 * 10^4
0 <= k < nums.length
'''

from typing import List


class Solution:
  def maximumScore(self, nums: List[int], k: int) -> int:
    score = nums[k]
    left, right = [], []
    
    # subarray low to the left
    curr_low = nums[k]
    for i in range(k-1, -1, -1):
      curr_low = min(curr_low, nums[i])
      left.append(curr_low)
      
    # subarray low to the right
    curr_low = nums[k]
    for i in range(k+1, len(nums)):
      curr_low = min(curr_low, nums[i])
      right.append(curr_low)
    
    # print(left, right)
    l, r = 0, 0
    nl, nr = len(left), len(right)
    
    while l < nl:
      while r < nr and right[r] >= left[l]:
        r += 1
      
      # print('left:', l, r, left[l] * (l+r+2))
      score = max(score, left[l] * (l+r+2))
      l += 1
      
    l, r = 0, 0
    while r < nr:
      while l < nl and left[l] >= right[r]:
        l += 1
      
      # print('right', l, r, right[l] * (l+r+2))
      score = max(score, right[r] * (l+r+2))
      r += 1
    
    return score

   
  def maximumScore(self, nums: List[int], k: int) -> int:
    n = len(nums)
    l, r = k, k
    low = nums[k]
    score = low
  
    while l > 0 or r < n-1:
      if l == 0:
        r += 1
        low = min(low, nums[r])
        score = max(score, low*(r+1))
        continue
        
      if r == n-1:
        l -= 1
        low = min(low, nums[l])
        score = max(score, low*(n-l))
        continue
        
      left_low, right_low = min(low, nums[l-1]), min(low, nums[r+1])
      score_left, score_right = left_low*(r-l+2), right_low*(r-l+2)
      
      # extend to the left if left-side makes a higher score
      # than the right side
      if score_left >= score_right:
        l -= 1
        score = max(score, score_left)
        low = left_low
        
      # otherwise, extend to the right side
      else:
        r += 1
        score = max(score, score_right)
        low = right_low
        
    return score
  
