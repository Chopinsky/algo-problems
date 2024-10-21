'''
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.
'''

from functools import lru_cache
from typing import Tuple


class Solution:
  def maxUniqueSplit(self, s: str) -> int:
    n = len(s)
    
    @lru_cache(None)
    def dp(i: int, seen: Tuple) -> int:
      if i >= n:
        return len(seen)
      
      cnt = 0
      
      for j in range(i, n):
        s0 = s[i:j+1]
        if s0 in seen:
          continue
          
        nxt = tuple(sorted(seen + (s0, )))
        total = dp(j+1, nxt)
        cnt = max(cnt, total)
        
      return cnt
      
    return dp(0, tuple())
        
  def maxUniqueSplit(self, s: str) -> int:
    most_count = 1
    seen = set()
    
    def split(i: int):
      nonlocal most_count
      
      if i >= len(s):
        most_count = max(most_count, len(seen))
        return
      
      for j in range(i, len(s)):
        if s[i:j+1] in seen:
          continue
          
        seen.add(s[i:j+1])
        split(j+1)
        seen.discard(s[i:j+1])
      
    split(0)
    
    return most_count
  