'''
3575-maximum-good-subtree-score
'''

from typing import List


class Solution:
  def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
    mod = 10**9 + 7
    n = len(vals)
    adj = [[] for _ in range(n)]
    ans = 0
    for u in range(1, n):
      adj[par[u]].append(u)

    def dfs(u: int):
      nonlocal ans

      dist = {0: 0}
      s = str(abs(vals[u]))
      if len(s) == len(set(s)):
        m = sum(1 << int(ch) for ch in s)
        dist[m] = vals[u]

      for v in adj[u]:
        dv = dfs(v)
        for mv, sv in dv.items():
          for mu, su in list(dist.items()):
            if mu & mv == 0:
              dist[mu|mv] = max(dist.get(mu|mv, 0), su+sv)

      ans += max(dist.values())
      return dist

    dfs(0)

    return ans % mod

        