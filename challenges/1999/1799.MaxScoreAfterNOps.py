'''
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 
Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 10^6
'''


from typing import List
from math import gcd
from functools import lru_cache
from collections import defaultdict


class Solution:
  def maxScore(self, nums: List[int]) -> int:
    n = len(nums)
    limit = int('1'*n, 2)
    # print(n, limit)
    
    @lru_cache(None)
    def dp(i: int, mask: int) -> int:
      if mask == limit or i >= 1+n//2:
        return 0
      
      score = 0
      for a in range(n-1):
        if (1<<a) & mask > 0:
          continue
          
        for b in range(a+1, n):
          if (1<<b) & mask > 0:
            continue
            
          score = max(score, i*gcd(nums[a], nums[b]) + dp(i+1, mask | (1<<a) | (1<<b)))
          
      return score
        
    return dp(1, 0)
  
  
  def maxScore(self, nums: List[int]) -> int:
    pairs = []
    n = len(nums)
    
    for i in range(n):
      for j in range(i+1, n):
        pairs.append((gcd(nums[i], nums[j]), i, j))
        
    pairs.sort(reverse=True)
    size = len(pairs)
    ans = 0
    valid = [True] * n

    def dp(rem, pos, score):
      nonlocal ans
      
      # we've formed a chain, check the final  score
      if rem == 0:
        ans = max(ans, score)
        return
      
      # run out of the candidates, quit
      if pos == size:
        return

      # a better answer exists, quit early
      if ans >= score + sum(range(rem, 0, -1)) * pairs[pos][0]:
        return
      
      # if pos-th pair is usable, try use it to form the
      # chain
      s, x, y = pairs[pos]
      if valid[x] and valid[y]:
        valid[x] = False
        valid[y] = False
        
        dp(rem-1, pos+1, score+rem*s)
        
        valid[x] = True
        valid[y] = True

      # if don't use the pair, try the remainder pair set
      dp(rem, pos+1, score)

    # start the run
    dp(n//2, 0, 0)
    
    return ans
      
      
  def maxScore0(self, nums: List[int]) -> int:
    n = len(nums)
    gcd_map = defaultdict(dict)
    
    for x in nums:
      for y in nums:
        x0, y0 = min(x, y), max(x, y)
        if x == y:
          gcd_map[x0][y0] = x
        else:
          gcd_map[x0][y0] = gcd(x0, y0)
          
    # print(gcd_map)
    
    @lru_cache(None)
    def dp(i: int, mask: int) -> int:
      if i >= n//2:
        return 0
      
      score = 0

      # l is the left number of the pair
      for l in range(n):
        if (1<<l) & mask > 0:
          continue

        # r is the right number of the pair
        for r in range(l+1, n):
          if (1<<r) & mask > 0:
            continue

          x, y = min(nums[l], nums[r]), max(nums[l], nums[r])
          # print(x, y)

          nxt_score = (i+1) * gcd_map[x][y] + dp(i+1, mask | (1<<r) | (1<<l))
          score = max(score, nxt_score)

      return score
    
    return dp(0, 0)
  