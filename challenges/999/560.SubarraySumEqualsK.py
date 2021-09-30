'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''


class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    idx = defaultdict(int)
    s = 0
    
    for n in nums:
      s += n
      # print(s)
      
      if s == k:
        count += 1
        count += idx[0]
          
      else:
        count += idx[s-k]
      
      idx[s] += 1
    
    # print(idx)
    return count
