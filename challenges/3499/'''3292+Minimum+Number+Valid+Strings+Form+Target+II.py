'''
3292. Minimum Number of Valid Strings to Form Target II

Test cases:

["abc","aaaaa","bcdef"]
"aabcdabc"
["abababab","ab"]
"ababaababa"
["abcdef"]
"xyz"
'''

import math
from typing import List

class Solution:
  '''
  use kmp to calculate length of all prefix matches from `word` that's inside target,
  i.e., find the longest prefix from `word` that ended at each character index; then 
  iterate from the end of `target` and update `dp` for the minimum count of substring
  prefix counts;
  '''
  def minValidStrings(self, words: List[str], target: str) -> int:
    n = len(target)
    vals = [set() for _ in range(n)]

    def kmp(pat, text):
      k = 0
      jumps = [0] 
      m = len(pat)

      # build the pattern jumps
      for i in range(1, m):
        while k > 0 and pat[k] != pat[i]:
          k = jumps[k-1]

        if pat[k] == pat[i]:
          k += 1

        jumps.append(k)

      k = 0
      ans = []

      # find all prefix from `pat` that's ended at `ch` of the `target`, with 
      # the prefix length of `k`
      for ch in text:
        while k > 0 and (k == m or pat[k] != ch):
          k = jumps[k-1]

        if pat[k] == ch: 
          k += 1

        ans.append(k)

      return ans

    for word in words: 
      cand = kmp(word, target)
      for i, k in enumerate(cand): 
        if k > 0:
          vals[i].add(k)

    dp = [math.inf]*(n+1)
    dp[n] = 0 

    for i in range(n-1, -1, -1): 
      for k in vals[i]:
        dp[i-k+1] = min(dp[i-k+1], 1+dp[i+1])

    return dp[0] if dp[0] < math.inf else -1
