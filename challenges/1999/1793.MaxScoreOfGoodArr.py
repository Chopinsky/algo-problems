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


class Solution:
  def maximumScore(self, nums: List[int], k: int) -> int:
    n = len(nums)
    l, r = k, k
    low = nums[k]
    score = low
  
    while True:
      if l == 0 and r == n-1:
        break
        
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
        
      # only expanding in the direction that can yield a larger product
      ll, rl = min(low, nums[l-1]), min(low, nums[r+1])
      sl, sr = ll * (r-l+2), rl * (r-l+2)
      
      # moving 1 pointer at a time, this algo is correct because nums[r] > 0
      if sl >= sr:
        l -= 1
        score = max(score, sl)
        low = ll
        
      else:
        r += 1
        score = max(score, sr)
        low = rl
    
      # print(l, r, nums[l:r+1], score, low)
      
    return score
  
