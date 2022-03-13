'''
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.

Example 1:


Input: n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
Output: 9
Explanation:
The above figure represents the input graph.
The blue edges represent one of the subgraphs that yield the optimal answer.
Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible to get a subgraph with less weight satisfying all the constraints.
Example 2:


Input: n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
Output: -1
Explanation:
The above figure represents the input graph.
It can be seen that there does not exist any path from node 1 to node 2, hence there are no subgraphs satisfying all the constraints.
 

Constraints:

3 <= n <= 10^5
0 <= edges.length <= 10^5
edges[i].length == 3
0 <= fromi, toi, src1, src2, dest <= n - 1
fromi != toi
src1, src2, and dest are pairwise distinct.
1 <= weight[i] <= 10^5
'''


from typing import List, Dict
from collections import defaultdict
from heapq import heappop, heappush
import math


class Solution:
  def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    back = defaultdict(dict)
    forward = defaultdict(dict)
    
    for f, t, w in edges:
      back[t][f] = min(back[t].get(f, math.inf), w)
      forward[f][t] = min(forward[f].get(t, math.inf), w)
      
    # print(back, forward)
    
    # calculate the shortest distance between node-d and any other
    # reachable nodes in the graph
    def calc_node_dist(d: int, src: Dict) -> List[int]:
      scores = [math.inf] * n
      stack = [(0, d)]

      while stack:
        score, i = heappop(stack)
        if score >= scores[i]:
          continue

        scores[i] = score
        for j in src[i]:
          nxt_score = score + src[i][j]
          if nxt_score >= scores[j]:
            continue

          heappush(stack, (nxt_score, j))
          
      return scores

    # s0 has the distance *from* reachable nodes to `dest`
    s0 = calc_node_dist(dest, back)
    # print(s0)
    
    # either src1 or src2 is unreachable
    if s0[src1] == math.inf or s0[src2] == math.inf:
      return -1

    # s1 and s2 has the distance from `src1/2` *to* reachable
    # nodes in the graph
    s1 = calc_node_dist(src1, forward)
    s2 = calc_node_dist(src2, forward)
    weight = math.inf
    # print(s1, s2)
    
    # assuming the shortest path converge at node-i
    for i in range(n):
      # print(i, weight, s1[i], s2[i], s0[i])
      weight = min(weight, s1[i]+s2[i]+s0[i])
    
    return weight
        