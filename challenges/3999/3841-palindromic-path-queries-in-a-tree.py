'''
3841-palindromic-path-queries-in-a-tree
'''


class Solution:
  def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
    g = [[] for _ in range(n)]
    for u, v in edges:
      g[u].append(v)
      g[v].append(u)

    bit_bound = 18
    parent = [[-1]*n for _ in range(bit_bound)]
    depth = [0]*n
    tin = [0]*n
    tout = [0]*n
    timer = 0

    def dfs(u: int, p: int):
      nonlocal timer
      tin[u] = timer
      timer += 1
      parent[0][u] = p

      for nbr in g[u]:
        if nbr == p:
          continue

        depth[nbr] = depth[u] + 1
        dfs(nbr, u)

      tout[u] = timer-1

    # set up the tree structure
    dfs(0, -1)

    # build thebinary lifting table
    for k in range(1, bit_bound):
      for i in range(n):
        p = parent[k-1][i]
        if p != -1:
          parent[k][i] = parent[k-1][p]

    # lowest common ancestor via binary lifting
    def lca(u: int, v: int) -> int:
      if depth[u] < depth[v]:
        u, v = v, u

      diff = depth[u] - depth[v]

      # lift u to the same depth of v
      for k in range(bit_bound):
        if diff & (1<<k):
          u = parent[k][u]

      # on the same path
      if u == v:
        return u

      # uplift if both node's parent is not a common grandparent
      for k in reversed(range(bit_bound)):
        # only move up the tree by 2^k steps if the parents are 
        # different -- otherwise, the k-grandparent is above the lca.
        if parent[k][u] != parent[k][v]:
          u = parent[k][u]
          v = parent[k][v]

      return parent[0][u]

    size = n
    fenwick = [0]*(n+1)

    def update(i: int, val: int):
      if i == 0:
        fenwick[i] ^= val
        return

      while i <= size:
        fenwick[i] ^= val
        i += i & -i

    def query(i: int) -> int:
      res = fenwick[0]
      while i > 0:
        res ^= fenwick[i]
        i -= i & -i

      return res

    def mask(ch: str) -> int:
      return 1 << (ord(ch) - ord('a'))

    labels = list(s)
    answer = []

    for u, ch in enumerate(labels):
      m = mask(ch)
      update(tin[u], m)
      update(tout[u]+1, m)

    for q in queries:
      parts = q.split()
      if parts[0] == "update":
        u = int(parts[1])
        ch = parts[2]

        delta = mask(labels[u]) ^ mask(ch)
        labels[u] = ch

        update(tin[u], delta)
        update(tout[u]+1, delta)

      else:
        u, v = int(parts[1]), int(parts[2])
        w = lca(u, v)

        # <prefix path to u> ^ 
        #   <prefix path to v> ^ 
        #   <mask value of w because it's cancelled out in the prefix xor>
        path = query(tin[u]) ^ query(tin[v]) ^ mask(labels[w])

        # all char count are even, or at most 1 char is not
        answer.append(path == 0 or (path & (path-1)) == 0)

    return answer