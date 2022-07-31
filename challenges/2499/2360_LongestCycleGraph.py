'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

Example 1:

Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
Example 2:

Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.

Constraints:

n == edges.length
2 <= n <= 10^5
-1 <= edges[i] < n
edges[i] != i
'''

from typing import List


class Solution:
  '''
  the key to understand this problem is that at most one outbound edges from each node, meaning
  the node can be in at most 1 chain/cycle; so we can do dfs from all the nodes that have 0 or 1
  inbound edges as they may be the head of a chain/cycle; note that if we have a cycle without
  inbound chains, all nodes in the cycle have 1 inbound edge, so we have to include these cases 
  as well; 

  once we build the chain/cycle, then the length of the cycle equals the indexes where the node 
  appears twice in the dfs -- meaning we've routed back to the beginning of the cycle at this point;

  we visit each node at most once (since if a chain dfs extends to a visited node, then the cycle
  in this chain have already been found and calculated, we can skip the rest of the dfs process), hence
  the runtime is O(n).
  '''
  def longestCycle(self, edges: List[int]) -> int:
    n = len(edges)
    inbound = [0] * n
    
    for u in edges:
      if u >= 0:
        inbound[u] += 1
        
    max_len = -1
    cand = sorted([(i, c) for i, c in enumerate(inbound) if c <= 1], key=lambda x: x[1])
    seen = set()
    # print(cand)
    
    # build the chain that starts or go-through node-i
    def find_chain_len(i: int) -> int:
      if edges[i] < 0:
        seen.add(i)
        return -1
      
      idx = 0
      pos = {}
      
      while edges[i] >= 0:
        if i in pos:
          return idx - pos[i]
        
        if i in seen:
          break
          
        seen.add(i)
        pos[i] = idx
        idx += 1
        i = edges[i]
      
      return -1
      
    for i, c in cand:
      if c > 1:
        break
      
      if i in seen:
        continue
        
      max_len = max(max_len, find_chain_len(i))
    
    return max_len
    