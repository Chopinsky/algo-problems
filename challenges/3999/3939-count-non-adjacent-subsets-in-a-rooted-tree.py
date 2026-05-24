'''
3939-count-non-adjacent-subsets-in-a-rooted-tree
'''

from typing import List


class Solution:
  def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
    mod = 10**9 + 7
    n = len(parent)

    dp0 = [[0]*k for _ in range(n)]
    dp1 = [[0]*k for _ in range(n)]

    for i in range(n):
      dp0[i][0] = 1
      dp1[i][nums[i]%k] = 1

    for i in range(n-1, 0, -1):
      p = parent[i]
      nxt_dp0 = [0]*k
      nxt_dp1 = [0]*k
      any_ch = [(dp0[i][r] + dp1[i][r])%mod for r in range(k)]

      for r in range(k):
        if dp0[p][r]:
          for c in range(k):
            if any_ch[c]:
              nxt_rem = (r + c) % k
              nxt_dp0[nxt_rem] = (
                nxt_dp0[nxt_rem] + dp0[p][r]*any_ch[c]
              ) % mod
        
        if dp1[p][r]:
          for c in range(k):
            if dp0[i][c]:
              nxt_rem = (r + c) % k
              nxt_dp1[nxt_rem] = (
                nxt_dp1[nxt_rem] + dp1[p][r]*dp0[i][c]
              ) % mod

      dp0[p] = nxt_dp0
      dp1[p] = nxt_dp1

    return (dp0[0][0] + dp1[0][0] - 1) % mod


  def countValidSubsets0(self, parent: List[int], nums: List[int], k: int) -> int:
    n = len(parent)
    adj = [[] for _ in range(n)]
    dp = [[[0]*k, [0]*k] for _ in range(n)]
    mod = 10**9 + 7

    for i in range(n):
      if parent[i] >= 0:
        adj[parent[i]].append(i)

    def dfs(u: int):
      val = nums[u]
      dp[u][0][0] = 1     # do not take u in the subset
      dp[u][1][val%k] = 1 # take u in the subset

      for v in adj[u]:
        dfs(v)
        dp2 = [[0]*k, [0]*k]

        # u not taken
        for v0 in range(k):
          for v1 in range(k):
            x = (dp[v][0][v1] + dp[v][1][v1]) % mod
            dp2[0][(v0+v1)%k] = (
              dp2[0][(v0+v1)%k] + dp[u][0][v0]*x
            ) % mod

        # u taken
        for v0 in range(k):
          for v1 in range(k):
            dp2[1][(v0+v1)%k] = (
              dp2[1][(v0+v1)%k] + dp[u][1][v0]*dp[v][0][v1]
            ) % mod

        dp[u] = dp2

    dfs(0)

    return (dp[0][0][0] + dp[0][1][0] - 1 + mod) % mod
