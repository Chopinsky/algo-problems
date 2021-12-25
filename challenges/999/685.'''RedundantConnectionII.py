'''
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
'''


from typing import List


class Solution:
  '''
  tricky graph question: essentially the given DAG can be broken in 2 ways (or the mix 
  of the 2) -- 1) a vertex has 2 parents, or 2) a cycle is formed by adding the edge.

  so we save the edges that cause the 2 parents problem and the one that causes the cycle.
  if all 3 exists (the most complex case), we check which parent lead to the real root
  (i.e. the one that's never have a "from" vertex), keep it and remove the other
  '''
  def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
    n = len(edges)
    parent = [i for i in range(n+1)]
    roots = set([i+1 for i in range(n)])
    p1, p2, cycle = None, None, None
    
    def find(u: int) -> int:
      while u != parent[u]:
        u = parent[u]
        
      return u
    
    for u, v in edges:
      roots.discard(v)
      ru, rv = find(u), find(v)
      # print(u, v, ru, rv)
      
      # found 2 parents
      if parent[v] != v:
        p1 = [parent[v], v]
        p2 = [u, v]
      
      # found a cycle
      if ru == rv:
        cycle = [u, v]
      
      # only add the edge if: 1) it's not a cycle and 2) it's not
      # causing 2 parents, i.e. it's new to the network
      if ru != rv and parent[v] == v:
        parent[v] = u
    
    # print(p1, p2, cycle)
    if cycle:
      # no dual-parents, remove the cycle edge since it's the one 
      # added the last to form the cycle
      if not p1 and not p2:
        return cycle
      
      # we have a cycle that's linking 1 of the 2 parents to itself
      # when adding such edge; we remove the parent-edge that's leading
      # to the false root (i.e. the cycle edge will connect this parent to
      # itself if added). note: we can't check p2's parent root, since we
      # didn't add it to the network
      parent_root = find(p1[0])
      return p2 if (parent_root in roots) else p1
    
    # no cycle, a node has 2 paths to the same node, remove the one formed
    # from the later edge addition
    return p2
    