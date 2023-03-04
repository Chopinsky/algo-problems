'''
2581. Count Number of Possible Root Nodes

Alice has an undirected tree with n nodes labeled from 0 to n - 1. The tree is represented as a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Alice wants Bob to find the root of the tree. She allows Bob to make several guesses about her tree. In one guess, he does the following:

Chooses two distinct integers u and v such that there exists an edge [u, v] in the tree.
He tells Alice that u is the parent of v in the tree.
Bob's guesses are represented by a 2D integer array guesses where guesses[j] = [uj, vj] indicates Bob guessed uj to be the parent of vj.

Alice being lazy, does not reply to each of Bob's guesses, but just says that at least k of his guesses are true.

Given the 2D integer arrays edges, guesses and the integer k, return the number of possible nodes that can be the root of Alice's tree. If there is no such tree, return 0.

 

Example 1:



Input: edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3
Output: 3
Explanation: 
Root = 0, correct guesses = [1,3], [0,1], [2,4]
Root = 1, correct guesses = [1,3], [1,0], [2,4]
Root = 2, correct guesses = [1,3], [1,0], [2,4]
Root = 3, correct guesses = [1,0], [2,4]
Root = 4, correct guesses = [1,3], [1,0]
Considering 0, 1, or 2 as root node leads to 3 correct guesses.

Example 2:

Input: edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1
Output: 5
Explanation: 
Root = 0, correct guesses = [3,4]
Root = 1, correct guesses = [1,0], [3,4]
Root = 2, correct guesses = [1,0], [2,1], [3,4]
Root = 3, correct guesses = [1,0], [2,1], [3,2], [3,4]
Root = 4, correct guesses = [1,0], [2,1], [3,2]
Considering any node as root will give at least 1 correct guess. 

Constraints:

edges.length == n - 1
2 <= n <= 10^5
1 <= guesses.length <= 10^5
0 <= ai, bi, uj, vj <= n - 1
ai != bi
uj != vj
edges represents a valid tree.
guesses[j] is an edge of the tree.
guesses is unique.
0 <= k <= guesses.length

Test cases:

[[0,1],[1,2],[1,3],[4,2]]
[[1,3],[0,1],[1,0],[2,4]]
3

[[0,1],[1,2],[2,3],[3,4]]
[[1,0],[3,4],[2,1],[3,2]]
1

[[0,1],[2,0],[0,3],[4,2],[3,5],[6,0],[1,7],[2,8],[2,9],[4,10],[9,11],[3,12],[13,8],[14,9],[15,9],[10,16]]
[[8,2],[12,3],[0,1],[16,10]]
2
'''

from typing import List
from collections import defaultdict


class Solution:
  """
  this is a classic 'update all nodes in the graph from both directions' type of problem, 
  and one way to do it, is to go from leaves to the central root, and then reverse update,
  i.e. go from the central root back to leaves and update nodes along the way.

  part-1: moving to the center
  use the idea of topological sort, we can construct a bfs algo that update the "parent" node,
  and only add the parent node to the candidate list if it has only 1 edge left -- that it becomes
  the leafy node for the remaining graph; then there are 2 edge cases for determining the "central"
  node: if there are only 1 node left in the candidate list, then it is the root; if there are 2
  nodes left, then we can randomly pick one as the root, update it with the "leafy" node, aka the
  other one in the list.

  part-2: moving to the leaves
  from here on, we can propagate from central (singular) node back to the actual leafy nodes: 
  we calculate the count of the valid guesses from the "formal parent" node (total - from_curr),
  and add it to the current node's valid guesses count -- this information is to complete the missing
  count from part-1, where we have the counts for all "formal children" nodes except the count from
  the "formal parent" node, and now we have it.

  part-3: count criteria
  once the counter is updated in part-2, we have the total count of valid guesses under the current 
  node as the root of the tree, if this count is greater than or equal to the threshold, we add 1
  to the possible root count.
  """
  def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
    e = defaultdict(set)
    ec = defaultdict(int)
    
    for u, v in edges:
      e[u].add(v)
      ec[u] += 1
      
      e[v].add(u)
      ec[v] += 1
    
    guesses = set((u, v) for u, v in guesses)
    n, count = len(e), 0
    curr, nxt = set(), set()
    
    for u in e:
      if ec[u] == 1:
        curr.add(u)
        
    gc0 = [0]*n
    visited = curr.copy()
    adding = set()
    
    def add(v, u):
      return 1 if (v, u) in guesses else 0
    
    while len(curr) >= 2:
      if len(curr) == 2 and len(visited) == n:
        break
        
      # print('round 1:', curr, gc0)
      for u in curr:
        for v in e[u]:
          if (v in visited) and (v not in curr):
            continue

          # add the next node to visit
          ec[v] -= 1
          if ec[v] == 1:
            adding.add(v)
            nxt.add(v)
          
          # update correct guess count
          gc0[v] += gc0[u] + add(v, u)
          
      curr, nxt = nxt, curr
      nxt.clear()
      
      visited |= adding
      adding.clear()

    # choose the root for the next bfs round
    if len(curr) == 2:
      # take v as the root
      u, r = curr.pop(), curr.pop()
      gc0[r] += gc0[u] + add(r, u)
      
    else:
      # the only node as the root
      r = curr.pop()      
    
    # root node meet the requirements
    if gc0[r] >= k:
      count += 1
    
    # update and prepare for round-2
    visited = set([r])
    # print('done 1:', r, gc0)
    
    # add init round-2 nodes
    for u in e[r]:
      curr.add(u)
      visited.add(u)
      
      # update subtree correct guesses count
      gc0[u] += gc0[r] - gc0[u] - add(r, u) + add(u, r)
      if gc0[u] >= k:
        count += 1
      
    while curr:
      # print('round 2:', curr, gc0)
      for u in curr:
        for v in e[u]:
          if v in visited:
            continue
            
          # spread to v
          nxt.add(v)
          visited.add(v)
          
          # update subtree correct guesses count
          gc0[v] += gc0[u] - gc0[v] - add(u, v) + add(v, u)
          if gc0[v] >= k:
            count += 1
        
      curr, nxt = nxt, curr
      nxt.clear()
    
    # print('done 2:', gc0)
    return count
  