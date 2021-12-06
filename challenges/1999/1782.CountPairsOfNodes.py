'''
You are given an undirected graph defined by an integer n, the number of nodes, and a 2D integer array edges, the edges in the graph, where edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.

Let incident(a, b) be defined as the number of edges that are connected to either node a or b.

The answer to the jth query is the number of pairs of nodes (a, b) that satisfy both of the following conditions:

a < b
incident(a, b) > queries[j]
Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.

Note that there can be multiple edges between the same two nodes.

Example 1:

Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
Output: [6,5]
Explanation: The calculations for incident(a, b) are shown in the table above.
The answers for each of the queries are as follows:
- answers[0] = 6. All the pairs have an incident(a, b) value greater than 2.
- answers[1] = 5. All the pairs except (3, 4) have an incident(a, b) value greater than 3.

Example 2:

Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
Output: [10,10,9,8,6]

Constraints:

2 <= n <= 2 * 104
1 <= edges.length <= 105
1 <= ui, vi <= n
ui != vi
1 <= queries.length <= 20
0 <= queries[j] < edges.length
'''


from typing import List



class Solution:
  def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
    freq, edge_freq = [0] * (n+1), defaultdict(int)
    for x, y in edges:
      freq[x] += 1
      freq[y] += 1
      edge_freq[(min(x, y), max(x, y))] += 1
    
    # we only cares about how many times the node appears, not the
    # id of the node, and pad the cnter with nodes that are not connected
    # to the graph
    degree = sorted(freq)
    ans = []
    # print(freq, edge_freq)
    
    for q in queries:
      l, r = 1, n
      cnt = 0
      
      while l < r:
        # the total degree is higher than the threshold, adding all
        # pairs (i, r) where l <= i < r
        if degree[l] + degree[r] > q:
          cnt += r - l
          r -= 1
        else:
          l += 1
          
      for (u, v), shared_cnt in edge_freq.items():
        # the (u, v) pair is counted, however, the shared edges will bring
        # down the total count below the query threshold, remove it
        if q < freq[u] + freq[v] <= q + shared_cnt:
          cnt -= 1
      
      ans.append(cnt)
      
    return ans
        
