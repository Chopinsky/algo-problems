'''
Given the strings s1 and s2 of size n and the string evil, return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 109 + 7.

Example 1:

Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51 
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da". 
Example 2:

Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0 
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.
Example 3:

Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2
 

Constraints:

s1.length == n
s2.length == n
s1 <= s2
1 <= n <= 500
1 <= evil.length <= 50
All strings consist of lowercase English letters.
'''


from functools import lru_cache


class Solution:
  def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
    start = 0
    while start < n and s1[start] == s2[start]:
      start += 1
      
    if evil in s1[:start]:
      return 0
    
    if start >= n:
      return 1
    
    mod = 1_000_000_007
    m = len(evil)
    evil_chars = set()
    evil_tail_idx = ord(evil[-1]) - ord('a')
    evil_str_prefix = set()
    
    for i in range(m):
      evil_str_prefix.add(evil[:i+1])
      evil_chars.add((ord(evil[i])-ord('a')))
    
    # jump to the next evil prefix match
    @lru_cache(None)
    def nxt_prefix_ln(pos: int, ch_idx: int) -> int:
      if ch_idx not in evil_chars:
        return 0
      
      if pos == 0:
        return 1 if (ord(evil[0])-ord('a') == ch_idx) else 0
      
      base = evil[:pos] + chr(ord('a')+ch_idx)
      for i in range(pos+1):
        if base[i] == evil[0] and base[i:] in evil_str_prefix:
          return pos-i+1
        
      return 0
    
    @lru_cache(None)
    def dp(pos: int, evil_pos: int, equal1: bool, equal2: bool) -> int:
      l = 0 if not equal1 else (ord(s1[pos])-ord('a'))
      r = 25 if not equal2 else (ord(s2[pos])-ord('a'))
      # print(pos, evil_pos, equal1, equal2, l, r)
      
      # if we're at the end of the string matching, count and done
      if pos == n-1:
        cnt = r-l+1

        # exclude the full evil string match choice
        if evil_pos == m-1 and l <= evil_tail_idx <= r:
          cnt -= 1
          
        return cnt
        
      # try all possible combinations
      cnt = 0
      evil_idx = ord(evil[evil_pos]) - ord('a')
      
      for idx in range(l, r+1):
        nxt_evil_pos = evil_pos+1 if (idx == evil_idx) else nxt_prefix_ln(evil_pos, idx)
        if nxt_evil_pos >= m:
          # if a full match to the evil string, skip this char choice
          continue
        
        cnt += dp(pos+1, nxt_evil_pos, equal1 and idx == l, equal2 and idx == r)
          
      return cnt % mod
    
    # find the initial evil string partial matching with the prefix
    evil_ln = min(m-1, start)
    while evil_ln > 0 and s1[start-evil_ln:start] != evil[:evil_ln]:
      evil_ln -= 1
    
    # print('init:', start, evil_ln)
    return dp(start, evil_ln, True, True)
  