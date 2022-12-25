'''
2518. Number of Great Partitions

You are given an array nums consisting of positive integers and an integer k.

Partition the array into two ordered groups such that each element is in exactly one group. A partition is called great if the sum of elements of each group is greater than or equal to k.

Return the number of distinct great partitions. Since the answer may be too large, return it modulo 109 + 7.

Two partitions are considered distinct if some element nums[i] is in different groups in the two partitions.

Example 1:

Input: nums = [1,2,3,4], k = 4
Output: 6
Explanation: The great partitions are: ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) and ([4], [1,2,3]).
Example 2:

Input: nums = [3,3,3], k = 4
Output: 0
Explanation: There are no great partitions for this array.
Example 3:

Input: nums = [6,6], k = 2
Output: 2
Explanation: We can either put nums[0] in the first partition or in the second partition.
The great partitions will be ([6], [6]) and ([6], [6]).
 

Constraints:

1 <= nums.length, k <= 1000
1 <= nums[i] <= 109
'''

from typing import List
from functools import lru_cache


class Solution:
  def countPartitions(self, nums: List[int], k: int) -> int:
    mod = 10**9 + 7
    n = len(nums)
    nums.sort(reverse=True)

    prefix = [val for val in nums]
    for i in range(1, n):
      prefix[i] += prefix[i-1]
    
    # print(prefix)
    if prefix[-1] < k*2:
      return 0
    
    @lru_cache(None)
    def dp(i, s1):
      if i >= n:
        # print('idx??', i, s1, prefix[-1]-s1)
        return 1 if s1 >= k and prefix[-1]-s1 >= k else 0
      
      s2 = prefix[i] - nums[i] - s1
      rem = prefix[-1] - (0 if i == 0 else prefix[i-1])
      
      if s1+rem < k or s2+rem < k:
        # print('out:', i, s1, s2, rem)
        return 0
      
      if s1 >= k and s2 >= k:
        # print('stop:', i, s1, s2, pow(2, n-i, mod))
        return pow(2, n-i, mod) 
      
      if s1 > s2:
        return dp(i, s2)
      
      return (dp(i+1, s1+nums[i]) + dp(i+1, s1)) % mod
    
    return dp(0, 0)
    