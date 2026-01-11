'''
3786-total-sum-of-interaction-cost-in-tree-groups
'''

from collections import Counter, defaultdict
from typing import List


class Solution:
  def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
    e = defaultdict(list)
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)

    tcnt = Counter(group)
    ans = [0]

    def dfs(u: int, p: int):
      ucnt = Counter()
      ucnt[group[u]] = 1

      for v in e[u]:
        if v == p:
          continue

        vcnt = dfs(v, u)
        for g, c in vcnt.items():
          # edge contribution equals:
          # <cnt of nodes from subtree> * <cnt of nodes from rest of tree>
          ans[0] += c * (tcnt[g]-c)

        # optimize for merge back
        if len(vcnt) > len(ucnt):
          ucnt, vcnt = vcnt, ucnt

        # merge back
        ucnt.update(vcnt)

      return ucnt

    dfs(0, -1)

    return ans[0]