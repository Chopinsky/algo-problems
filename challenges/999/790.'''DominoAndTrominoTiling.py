'''
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Example 1:

Input: n = 3
Output: 5
Explanation: The five different ways are show above.

Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 1000
'''

from functools import lru_cache


class Solution:
  def numTilings(self, n: int) -> int:
    mod = 10**9 + 7

    @lru_cache(None)
    def partial(n):  
      if n == 2:
        return 1
      
      # 1 partial (add hor to flip side) + full with a tromino
      return (partial(n - 1) + full(n - 2)) % mod

    @lru_cache(None)
    def full(n):  
      if n <= 2:
        return n
      
      # 1 ver + 1 hor (2 hor stacking on top of each other) + 2 
      # partials (with opposite sides)
      return (full(n - 1) + full(n - 2) + 2 * partial(n - 1)) % mod

    return full(n)
  

  def numTilings(self, n: int) -> int:
    mod = 1_000_000_007

    @lru_cache(None)  
    def partial(n):  
      if n == 2:
        return 1
      
      return (partial(n - 1) + full(n - 2)) % mod

    @lru_cache(None)
    def full(n):  
      if n <= 2:
        return n
      
      return (full(n - 1) + full(n - 2) + 2 * partial(n - 1)) % mod

    return full(n)