'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

Example 1:

Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
Example 2:

Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.

Constraints:

n == parent.length == s.length
1 <= n <= 10^5
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.
'''

from typing import List
from collections import defaultdict
from bisect import insort


class Solution:
  def longestPath(self, parent: List[int], s: str) -> int:
    n = len(parent)
    subtree = defaultdict(list)
    cand = set([i for i in range(n)])
    count = defaultdict(int)
    ans = 1
    
    for p in parent:
      if p >= 0:
        count[p] += 1
        cand.discard(p)
        
    cand = list(cand)
    # print('init:', cand)
    
    # use topological sort to move from down-side-up
    while cand:
      # get the current node and update the answer
      u = cand.pop()
      # print('visit:', u, subtree[u])
      
      if len(subtree[u]) >= 2:
        ans = max(ans, sum(subtree[u][-2:]) - 1)
        
      elif len(subtree[u]) > 0:
        ans = max(ans, subtree[u][-1])
      
      # get and update the parent info
      p = parent[u]
      count[p] -= 1
      
      # all children of this parent node is visited,
      # push the parent node to the candidate queue
      if not count[p]:
        cand.append(p)
      
      # same char, chain break
      if s[u] == s[p]:
        continue
        
      # different char, update the chain length
      chain_len = 1 + (subtree[u][-1] if subtree[u] else 1)
      insort(subtree[p], chain_len)
      
      # only keep top 2 nodes
      if len(subtree[p]) > 2:
        subtree[p] = subtree[p][-2:]
      
    return ans
    

  def longestPath(self, parent: List[int], s: str) -> int:
    chain = {}
    e = defaultdict(list)
    n = len(parent)
    
    for i in range(1, n):
      p = parent[i]
      e[i].append(p)
      e[p].append(i)
      
    long = 1
    # print(e)
    
    def update_chain_ln(u: int, v: int, ln: int):
      if ln >= chain[u][0][0]:
        chain[u][1] = chain[u][0]
        chain[u][0] = (ln, v)

      elif ln > chain[u][1][0]:
        chain[u][1] = (ln, v)
    
    def init(u: int, p: int) -> int:
      chain[u] = [(0, -1), (0, -1)]
      for v in e[u]:
        if v == p or s[u] == s[v]:
          continue
          
        ln = init(v, u)
        update_chain_ln(u, v, ln)
          
      # print('init', u, chain[u])
      return 1 + chain[u][0][0]
      
    def update(u: int, p: int):
      nonlocal long
      if p >= 0:
        # check the parent's chain length
        ln = 1 + (chain[p][1][0] if chain[p][0][1] == u else chain[p][0][0])
          
        # update the long chain store
        update_chain_ln(u, p, ln)

      for v in e[u]:
        if v == p or s[u] == s[v]:
          continue
          
        update(v, u)
      
      long = max(long, 1+chain[u][0][0]+chain[u][1][0])
      
    for i in range(n):
      # already visited
      if i in chain:
        continue
        
      # update chain lengths in the subtree
      init(i, -1)
      update(i, -1)
    
    # print(chain)
    return long
    