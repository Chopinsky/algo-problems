'''
3812-minimum-edge-toggles-on-a-tree
'''


class Solution:
  def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
    g = defaultdict(list)
    for i, [u, v] in enumerate(edges):
      g[u].append((v, i))
      g[v].append((u, i))

    s = [int(ch) for ch in start]
    t = [int(ch) for ch in target]
    sol = []
    # print('init:', g, s, t)

    def dfs(u: int, p: int, e0: int):
      for v, e1 in g[u]:
        if v == p:
          continue

        # solve leaf nodes first
        dfs(v, u, e1)

      if e0 < 0 or p < 0:
        return

      # greedy: flip parent edge
      if s[u] != t[u]:
        sol.append(e0)
        s[u] ^= 1
        s[p] ^= 1

    dfs(0, -1, -1)

    return [-1] if s[0] != t[0] else sorted(sol)
        