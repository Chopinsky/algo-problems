'''
3995-minimum-cost-to-convert-string-iii
'''

from math import inf


class Solution:
  def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
    n = len(source)
    if n != len(target):
      return -1

    dp = [inf]*(n+1)
    dp[n] = 0

    cand = []
    for (pat, rep), c in zip(rules, costs):
      cand.append((pat, rep, len(pat), c+pat.count('*')))

    for i in range(n-1, -1, -1):
      # can skip any replacement use past
      # best results
      if source[i] == target[i]:
        dp[i] = dp[i+1]

      for pat, rep, l, cost in cand:
        if i+l > n:
          continue

        ok = True

        # check if pattern can be applied
        for k in range(l):
          if pat[k] != '*' and pat[k] != source[i+k]:
            ok = False
            break

        if not ok:
          continue

        # check if replacement is the correct target seg
        for k in range(l):
          if rep[k] != target[i+k]:
            ok = False
            break

        if not ok:
          continue

        # can replace with this cand pattern
        # at char position i
        dp[i] = min(dp[i], dp[i+l] + cost)
        
    return -1 if dp[0] >= inf else dp[0]
