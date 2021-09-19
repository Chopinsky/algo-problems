'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
'''


from collections import defaultdict, Counter
from bisect import bisect_right


class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    if len(t) > len(s):
      return 0
    
    pos = defaultdict(list)
    tc = Counter(t)
    
    for i, ch in enumerate(s):
      pos[ch].append(i)
    
    for k in tc:
      if len(pos[k]) < tc[k]:
        return 0
    
    cache = {}
    
    def dp(i: int, j: int) -> int:
      src = pos[t[j]]
      if not src:
        return 0
      
      idx = bisect_right(src, i-1)
      if idx >= len(src):
        return 0
      
      if j == len(t)-1:
        # print('last', i, j, len(src)-idx)
        return len(src) - idx
      
      if (src[idx], j) in cache:
        return cache[src[idx], j]
      
      count = 0
      for p in src[idx:]:
        count += dp(p+1, j+1)
      
      cache[src[idx], j] = count
      return count
    
    return dp(0, 0)
