'''
3579-minimum-steps-to-convert-string-with-operations
'''

from math import inf
from collections import Counter


class Solution:
  def minOperations(self, word1: str, word2: str) -> int:
    n = len(word1)
    dp = [inf]*n + [0]

    for i in range(n-1, -1, -1):
      for j in range(i, n):
        w1 = word1[i:j+1]
        w2 = word2[i:j+1]

        c1 = Counter(zip(w1, w2))
        m1 = sum(v for (a, b), v in c1.items() if a != b)
        s1 = sum(min(c1[a, b], c1[b, a]) for (a, b) in c1 if a < b)
        dp[i] = min(dp[i], m1-s1+dp[j+1])

        c2 = Counter(zip(w1[::-1], w2))
        m2 = sum(v for (a, b), v in c2.items() if a != b)
        s2 = sum(min(c2[a, b], c2[b, a]) for (a, b) in c2 if a < b)
        dp[i] = min(dp[i], 1+m2-s2+dp[j+1])
        
    return dp[0]
