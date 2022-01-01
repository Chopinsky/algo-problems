'''
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

Example 1:

Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

Example 2:

Input: n = 2, edges = [[1,2]]
Output: [1]

Example 3:

Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]

Constraints:

2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
All pairs (ui, vi) are distinct.
'''


from typing import List
from collections import defaultdict


class Solution:
  '''
  calc the depth of the subtrees, and the longest dist in this subtree is either 
  depth0 + depth1 + 1 (i.e. the deepest longth from the 2 deepest subtrees + self), or 
  max(dist0, dist1), which is the max distance between nodes in this subtree
  '''
  def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
    adj = [[] for i in range(n)]
    for u, v in edges:
      adj[u-1].append(v-1)
      adj[v-1].append(u-1)

    memo = [[[] for _ in range(len(adj[i]))] for i in range(n)] 
    
    # find subtrees with node-i as root, `parent` as the parent node,
    # and idx-th neighbor of node-i
    def find(i, parent, idx):
      if idx == len(adj[i]):
        return [(0, 0)]
      
      if memo[i][idx]:
        return memo[i][idx]
      
      if adj[i][idx] == parent:
        return find(i, parent, idx+1)
      
      r = []
      for depth, dist in find(i, parent, idx+1):
        r.append((depth, dist))
        for depth0, dist0 in find(adj[i][idx], i, 0):
          r.append((max(depth, depth0+1), max(dist, dist0, depth0+1+depth)))
            
      if idx == 0:
        memo[i][idx] = r
        
      return r
          
    # find the distance from the tree, which is rooted @ i
    # and the tree root's parent is `parent`
    def graph(i, parent):
      yield from find(i, parent, 0)

      for j in adj[i]:
        if j != parent:
          yield from graph(j, i)

    ans = [0] * (n-1)
    for _, dist in graph(0, -1):
      if dist > 0:
        ans[dist-1] += 1
        
    return ans
      
      
  def countSubgraphsForEachDiameter0(self, n: int, edges: List[List[int]]) -> List[int]:
    en = defaultdict(int)
    tree_dist = defaultdict(int)
    
    for u, v in edges:
      en[u] |= 1 << v
      en[v] |= 1 << u
    
    def find_max_dist(i: int):
      dist = 0
      seen = set([1<<i])
      stack, nxt = set([1<<i]), set()
      
      while stack:
        dist += 1
        # print('iter:', i, dist, stack)
        
        for j in range(1, n+1):
          for tree in stack:
            if tree & (1<<j):
              continue
              
            if tree & en[j] == 0:
              continue
              
            nxt_tree = tree | (1<<j)
            if nxt_tree in seen:
              continue
              
            nxt.add(nxt_tree)
            seen.add(nxt_tree)
            tree_dist[nxt_tree] = max(tree_dist[nxt_tree], dist)
          
        combo, nxt_combo = nxt.copy(), set()
        base = nxt.copy()
        
        while combo:
          for tree in combo:
            for base_tree in base:
              nxt_tree = tree | base_tree
              if nxt_tree == tree or nxt_tree in seen:
                continue
                
              nxt.add(nxt_tree)
              seen.add(nxt_tree)
              nxt_combo.add(nxt_tree)
              tree_dist[nxt_tree] = max(tree_dist[nxt_tree], dist)
                
          combo, nxt_combo = nxt_combo, combo
          nxt_combo.clear()
        
        stack, nxt = nxt, stack
        nxt.clear()
    
    for i in range(1, n+1):
      find_max_dist(i)
    
    # for tree in tree_dist:
    #   print(format(tree, '004b'), tree_dist[tree])
    
    ans = [0] * (n-1)
    for dist in tree_dist.values():
      ans[dist-1] += 1
    
    return ans
  