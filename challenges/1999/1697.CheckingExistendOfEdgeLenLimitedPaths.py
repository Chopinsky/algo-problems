'''
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

Example 1:

Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.

Example 2:

Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.

Constraints:

2 <= n <= 10^5
1 <= edgeList.length, queries.length <= 10^5
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 10^9
There may be multiple edges between two nodes.
'''

from typing import List
from heapq import heappop
import math


class Solution:
  def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
    src = sorted([(e[2], min(e[0], e[1]), max(e[0], e[1])) for e in edges])
    q = sorted([l, u, v, i] for i, (u, v, l) in enumerate(queries))
    ans = [False] * len(q)
    g = [i for i in range(n)]
    
    def find(x):
      while g[x] != x:
        x = g[x]
        
      return x
    
    def union(x, y):
      rx, ry = find(x), find(y)
      if rx <= ry:
        g[ry] = rx
      else:
        g[rx] = ry
    
    # print(src, q)
    for limit, u, v, i in q:
      while src and src[0][0] < limit:
        _, x, y = heappop(src)
        union(x, y)
        
      ans[i] = find(u) == find(v)
    
    return ans
        

  def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
    nodes = [i for i in range(n)]
    
    def find(i: int) -> int:
      while nodes[i] != i:
        i = nodes[i]
        
      return i
    
    def union(i: int, j: int) -> int:
      ii, ji = find(i), find(j)
      if ii <= ji:
        nodes[ji] = ii
        return ii
      
      nodes[ii] = ji
      return ji
    
    e = {}
    e_lst = []
    
    for u, v, d in edges:
      a, b = min(u, v), max(u, v)
      e[a, b] = min(e.get((a, b), math.inf), d)
        
    for (u, v), d in e.items():
      e_lst.append((d, u, v))
      
    e_lst.sort()
    # print(e, e_lst)
    
    q = [(th, min(u, v), max(u, v), i) for i, [u, v, th] in enumerate(queries)]
    q.sort()
    # print(q)
    
    ans = [False] * len(q)
    edx = 0
    
    for th, u, v, idx in q:
      while edx < len(e_lst) and e_lst[edx][0] < th:
        d, u0, v0 = e_lst[edx]
        union(u0, v0)
        edx += 1
        
      ans[idx] = (find(u) == find(v))
    
    return ans
        