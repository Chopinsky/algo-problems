'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 
Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
'''


from typing import List


class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    g = [i for i in range(len(edges)+1)]

    def find(u: int):
      while g[u] != u:
        u = g[u]

      return u

    for u, v in edges:
      ru, rv = find(u), find(v)
      if ru == rv:
        return [u, v]

      if ru < rv:
        g[rv] = ru
      else:
        g[ru] = rv

    return [-1, -1]

  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    n = len(edges)
    node = [i for i in range(n)]
    
    def union(i: int, j: int):
      bi, bj = find(i), find(j)
      
      if bi <= bj:
        node[bj] = bi
      else:
        node[bi] = bj
      
      return
    
    def find(i: int):
      while node[i] != i:
        i = node[i]
        
      return i
    
    for [a, b] in edges:
      ra, rb = find(a-1), find(b-1)
      if ra == rb:
        return [a, b]
      
      # union(a-1, b-1)
      if ra <= rb:
        node[rb] = ra
      else:
        node[ra] = rb
              
    return edges[-1]
    