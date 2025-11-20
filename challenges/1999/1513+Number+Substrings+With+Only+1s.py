'''
1513. Number of Substrings With Only 1s

Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.

Constraints:

1 <= s.length <= 10^5
s[i] is either '0' or '1'.
'''

from functools import lru_cache
from math import comb


class Solution:
  def numSub(self, s: str) -> int:
    mod = 10**9 + 7
    count = 0
    total = 0

    for ch in s:
      if ch == '0':
        count = 0
        continue

      count += 1
      total = (total + count) % mod

    return total
        
  def numSub(self, s: str) -> int:
    mod = 10**9 + 7
    count = 0
    total = 0
    
    @lru_cache(None)
    def get_pairs(cnt: int) -> int:
      if cnt <= 1:
        return cnt
      
      return comb(cnt, 2) + cnt
    
    for ch in s:
      if ch == '1':
        count += 1
        continue

      total = (total + get_pairs(count)) % mod
      count = 0
    
    return (total + get_pairs(count)) % mod
