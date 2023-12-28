'''
2973. Find Number of Coins to Place in Tree Nodes

You are given an undirected tree with n nodes labeled from 0 to n - 1, and rooted at node 0. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array cost of length n, where cost[i] is the cost assigned to the ith node.

You need to place some coins on every node of the tree. The number of coins to be placed at node i can be calculated as:

If size of the subtree of node i is less than 3, place 1 coin.
Otherwise, place an amount of coins equal to the maximum product of cost values assigned to 3 distinct nodes in the subtree of node i. If this product is negative, place 0 coins.
Return an array coin of size n such that coin[i] is the number of coins placed at node i.

Example 1:


Input: edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]
Output: [120,1,1,1,1,1]
Explanation: For node 0 place 6 * 5 * 4 = 120 coins. All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
Example 2:

Input: edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]
Output: [280,140,32,1,1,1,1,1,1]
Explanation: The coins placed on each node are:
- Place 8 * 7 * 5 = 280 coins on node 0.
- Place 7 * 5 * 4 = 140 coins on node 1.
- Place 8 * 2 * 2 = 32 coins on node 2.
- All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
Example 3:

Input: edges = [[0,1],[0,2]], cost = [1,2,-2]
Output: [0,1,1]
Explanation: Node 1 and 2 are leaves with subtree of size 1, place 1 coin on each of them. For node 0 the only possible product of cost is 2 * 1 * -2 = -4. Hence place 0 coins on node 0.

Constraints:

2 <= n <= 2 * 10^4
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
cost.length == n
1 <= |cost[i]| <= 10^4
The input is generated such that edges represents a valid tree.
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
  def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
    n = len(cost)
    ans = [0]*n
    p = [0]*n
    d = [0]*n
    s = [0]*n
    idx = 0
    
    e = defaultdict(list)
    hp = defaultdict(list)
    hn = defaultdict(list)
    cand = set([i for i in range(n)])
    stack = [0]
    
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)

    while idx < len(stack):
      u = stack[idx]    
      for v in e[u]:
        if v == p[u]:
          continue
          
        p[v] = u
        d[u] += 1
        stack.append(v)
        cand.discard(u)
      
      idx += 1
        
    # print(e)
    # print(p, cand, d)
    
    def add(u: int, val: int):
      if val == 0:
        return
      
      if val > 0:
        heappush(hp[u], val)
        if len(hp[u]) > 3:
          heappop(hp[u])
          
      else:
        heappush(hn[u], -val)
        if len(hn[u]) > 2:
          heappop(hn[u])
    
    def update(u: int):
      if s[u] < 3:
        ans[u] = 1
        return
      
      if len(hp[u]) >= 3:
        ans[u] = max(ans[u], hp[u][0]*hp[u][1]*hp[u][2])
        
      if len(hn[u]) >= 2 and len(hp[u]) >= 1:
        ans[u] = max(ans[u], hn[u][0]*hn[u][1]*max(hp[u]))
      
    while cand:
      u = cand.pop()
      s[u] += 1
      add(u, cost[u])
      
      for v in e[u]:
        if u > 0 and v == p[u]:
          continue
        
        for pv in hp[v]:
          add(u, pv)
          
        for nv in hn[v]:
          add(u, -nv)
      
      update(u)
      if u == 0:
        continue

      pu = p[u]
      s[pu] += s[u]
      d[pu] -= 1
      # print('end:', u, pu, s[u], s[pu])

      if not d[pu]:
        cand.add(pu)
    
    # print('size:', s)
    return ans
  