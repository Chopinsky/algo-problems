'''
4100-minimum-cost-path-with-even-xor-parity
'''


class Solution:
  def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
    n = len(values)
    g = [[] for _ in range(n)]
    INF = float("inf")

    for u, v, w in edges:
      g[u].append((v, w))
      g[v].append((u, w))

    ans = INF

    def dfs(u: int, p: int) -> list:
      nonlocal ans

      b = values[u].bit_count() & 1 # bit_count_odd_flag
      f = [INF, INF] # [even_bit_wt, odd_bit_wt]
      f[b] = 0

      for v, w in g[u]:
        if v == p:
          continue

        sub = dfs(v, u)
        ans = min(ans, f[0]+sub[0]+w, f[1]+sub[1]+w)
        f[b] = min(f[b], sub[0]+w)     # even+b -> b
        f[1-b] = min(f[1-b], sub[1]+w) #  odd+b -> 1-b

      return f

    dfs(0, -1)
    return ans if ans < INF else -1
        