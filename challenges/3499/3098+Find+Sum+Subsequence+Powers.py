'''
You are given an integer array nums of length n, and a positive integer k.

The power of a subsequence is defined as the minimum absolute difference between any two elements in the subsequence.

Return the sum of powers of all subsequences of nums which have length equal to k.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3,4], k = 3

Output: 4

Explanation:

There are 4 subsequences in nums which have length 3: [1,2,3], [1,3,4], [1,2,4], and [2,3,4]. The sum of powers is |2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4.

Example 2:

Input: nums = [2,2], k = 2

Output: 0

Explanation:

The only subsequence in nums which has length 2 is [2,2]. The sum of powers is |2 - 2| = 0.

Example 3:

Input: nums = [4,3,-1], k = 2

Output: 10

Explanation:

There are 3 subsequences in nums which have length 2: [4,3], [4,-1], and [3,-1]. The sum of powers is |4 - 3| + |4 - (-1)| + |3 - (-1)| = 10.

Constraints:

2 <= n == nums.length <= 50
-10^8 <= nums[i] <= 10^8
2 <= k <= n
'''

from typing import List
from collections import defaultdict
from functools import lru_cache

class Solution:
  '''
  the core idea is to find the aggregated count of valid subsequences from index <i> 
  that has a lenght of <ln>, after sorting the array; for each index <j> that's bigger 
  than <i> (and nums[i] <= nums[j] due to the sort at the previous step), any counted
  subsequences will have at most min(prev_power, nums[j]-nums[i]) power, so we rebuild
  the aggregated counts for index <i>, and return the result back; the final answer is 
  to iterate all index in nums, and count the number of subsequences <c> with power <d>;
  '''
  def sumOfPowers(self, nums: List[int], k: int) -> int:
    mod = 10**9+7
    n, sums = len(nums), 0
    nums.sort()
    
    if k == n:
      return min((nums[i]-nums[i-1]) for i in range(1, n))
    
    @lru_cache(None)
    def dp(i: int, ln: int):
      if i >= n or ln == 0:
        return tuple()
      
      cnt = defaultdict(int)
      
      for j in range(i+1, n):
        d0 = nums[j]-nums[i]
        if ln == 1:
          cnt[d0] += 1
          continue
        
        cand = dp(j, ln-1)
        if len(cand) == 0:
          break
          
        for d1, c1 in cand:
          cnt[min(d0, d1)] += c1
        
      return sorted(cnt.items())
    
    for i in range(n):
      # subseq starts at i, and needs to add k-1 more elements into it
      cand = dp(i, k-1)
      if not cand:
        break
        
      sums = (sums + sum(d*c for d, c in cand)) % mod
      
    return sums
        