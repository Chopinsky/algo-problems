'''
There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to arrange the sticks such that exactly k sticks are visible from the left. A stick is visible from the left if there are no longer sticks to the left of it.

For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and 5 are visible from the left.
Given n and k, return the number of such arrangements. Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input: n = 3, k = 2
Output: 3
Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that exactly 2 sticks are visible.
The visible sticks are underlined.

Example 2:

Input: n = 5, k = 5
Output: 1
Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are visible.
The visible sticks are underlined.

Example 3:

Input: n = 20, k = 11
Output: 647427950
Explanation: There are 647427950 (mod 109 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.

Constraints:

1 <= n <= 1000
1 <= k <= n
'''


from functools import lru_cache
from math import factorial, comb


class Solution:
  def rearrangeSticks(self, n: int, k: int) -> int:
    mod = 1_000_000_007
    
    @lru_cache(None)
    def dp(total: int, rem: int) -> int:
      # all sticks must be in ascending order
      if total == rem:
        return 1
      
      # invalid case, 0 ways of making this 
      if rem == 0:
        return 0
      
      # consider {total} sticks, if the last stick is the largest,
      # we need to see {rem-1} from the left {total-1} sticks; if
      # the last stick is not the largest, then we have {total-1}
      # choices for the last stick, and we need to find {rem} sticks
      # from the {total-1} sticks
      return (dp(total-1, rem-1) + dp(total-1, rem) * (total-1)) % mod
      
    return dp(n, k)
      
      
    
  def rearrangeSticks1(self, n: int, k: int) -> int:
    mod = 1_000_000_007
    if n == k:
      return 1
    
    if k == 1:
      return factorial(n-1) % mod
    
    @lru_cache(None)
    def calc(i: int, j: int) -> int:
      return comb(n-i-1, j-i-1) * factorial(j-i-1)
    
    @lru_cache(None)
    def dp(i: int, rem: int) -> int:
      if n-i == rem:
        return 1
      
      if rem == 1:
        return factorial(n-i-1)
      
      count = 0
      for j in range(i+1, n-rem+2):
        count += calc(i, j) * dp(j, rem-1)
        count %= mod
      
      return count
    
    return dp(0, k)
  