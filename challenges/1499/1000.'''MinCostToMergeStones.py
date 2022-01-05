'''
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

Example 1:

Input: stones = [3,2,4,1], k = 2
Output: 20
Explanation: We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.

Example 2:

Input: stones = [3,2,4,1], k = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.

Example 3:

Input: stones = [3,5,1,2,6], k = 3
Output: 25
Explanation: We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.

Constraints:

n == stones.length
1 <= n <= 30
1 <= stones[i] <= 100
2 <= k <= 30
'''


from typing import List
from functools import lru_cache
import math


class Solution:
  def mergeStones0(self, stones: List[int], k: int) -> int:
    n = len(stones)
    if (n-1) % (k-1) != 0:
      return -1
    
    dp = [[0] * n for _ in range(n)]
    prefix = [0] * (n+1)
    
    for i in range(1, n+1):
      prefix[i] = prefix[i-1] + stones[i-1]
      
    for length in range(k, n+1):
      for i in range(n-length+1):
        # now consider combining the stones[i:j+1]
        # into 1 pile, set init score to math.inf
        j = i + length - 1
        # dp[i][j] = math.inf
        
        # min scores to form piles within the current
        # section, with the head pile from stones[i:t+1]
        for t in range(i, j, k-1):
          dp[i][j] = min(dp[i][j], dp[i][t] + dp[t+1][j])
          
        # we can form a pile from stones[i:j+1]
        if (j-i)%(k-1) == 0:
          dp[i][j] += prefix[j+1] - prefix[i]
          
    return dp[0][n-1]


  def mergeStones(self, stones: List[int], k: int) -> int:
    if len(stones) == 1:
      return 0
    
    prefix = [stones[i] for i in range(len(stones))]
    for i in range(1, len(stones)):
      prefix[i] += prefix[i-1]
    
    @lru_cache(None)
    def combine(l: int, r: int, rem: int) -> int:
      n = r-l+1
      
      if (n == rem) or (rem == k and n == 1):
        # special case -- we are taking all stones and
        # make them 1 pile
        if rem == k and n == rem:
          return prefix[r] - (prefix[l-1] if l > 0 else 0)  
        
        # no further work to meet the requirements
        return 0
      
      # not going to make it
      if (n < k) or (rem == k and (n-1)%(k-1) != 0):
        return -1
      
      # best score to get 1 pile from stones[l:r+1]
      if rem == 1:
        return combine(l, r, k)
        
      best_score = -1
      
      # try different length to form the current pile (or the rem-th pile)
      # in the current section
      for ln in range(1, n, k-1):
        if l+ln > r:
          break
          
        rest_scores = combine(l+ln, r, rem-1)
        if rest_scores < 0:
          break
          
        curr_score = combine(l, l+ln-1, k)
        if curr_score < 0:
          continue
          
        curr_score += rest_scores
        best_score = curr_score if best_score < 0 else min(best_score, curr_score)
      
      # taking all pieces and combine them into 1 pile
      if best_score >= 0 and rem == k:
        best_score += prefix[r] - (prefix[l-1] if l > 0 else 0)
        
      return best_score
      
    return combine(0, len(stones)-1, k)
    