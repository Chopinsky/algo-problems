'''
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.

Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ** 4
'''

from typing import List
from functools import lru_cache


class Solution:
  def stoneGameII(self, piles: List[int]) -> int:
    suffix = [p for p in piles]
    n = len(piles)
    for i in range(n-2, -1, -1):
      suffix[i] += suffix[i+1]
      
    @lru_cache(None)
    def dp(i: int, m: int) -> tuple:
      if i >= n:
        return 0, 0
      
      if n-i <= 2*m:
        return suffix[i], 0
      
      curr = 0
      s0, s1 = 0, 0
      
      for x in range(0, 2*m):
        if i+x >= n:
          break
          
        curr += piles[i+x]
        b, a = dp(i+x+1, max(m, x+1))
        if curr+a > s0:
          s0 = curr+a
          s1 = b
      
      return s0, s1
    
    a, _ = dp(0, 1)
    
    return a
