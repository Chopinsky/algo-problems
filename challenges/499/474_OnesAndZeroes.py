'''
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
'''

from typing import List, Tuple
from functools import lru_cache


class Solution:
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    # (zero_count, one_count, ln), start with a blank set
    dp = {(0, 0, 0)}

    for s in strs:
      zeros = s.count("0")
      ones = len(s) - zeros
      nxt_dp = set()

      for z, o, ln in dp:
        if zeros+z <= m and ones+o <= n:
          nxt_dp.add((zeros+z, ones+o, ln+1))

      dp |= nxt_dp

    return max(val[3] for val in dp)


  def findMaxForm0(self, strs: List[str], m: int, n: int) -> int:
    @lru_cache(None)
    def count(s: str) -> Tuple:
      c0 = s.count('0')
      return c0, len(s) - c0
      
    @lru_cache(None)
    def dp(i: int, m0: int, n0: int) -> int:
      if (m0 <= 0 and n0 <= 0) or i >= len(strs):
        return 0
      
      # if don't use i-th str
      size = dp(i+1, m0, n0)
      z, o = count(strs[i])
      
      if z <= m0 and o <= n0:
        size = max(size, 1+dp(i+1, m0-z, n0-o))
      
      return size
      
    return dp(0, m, n)
  