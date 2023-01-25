'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

Example 1:


Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:

Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.

Constraints:

n == edges.length
2 <= n <= 10^5
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n
'''

from typing import List
import math


class Solution:
  def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
    n = len(edges)
    
    def calc_dist(src: int) -> List[int]:
      d = [math.inf] * n
      if src < 0 or src >= n:
        return d
      
      curr = src
      step = 0
      
      while 0 <= curr < n and d[curr] > step:
        d[curr] = step
        curr = edges[curr]
        step += 1
      
      return d
    
    d1 = calc_dist(node1)
    d2 = calc_dist(node2)
    dist = math.inf
    idx = -1
    # print(d1, d2)
    
    for i in range(n):
      d0 = max(d1[i], d2[i])
      if d0 < dist:
        dist = d0
        idx = i
    
    return idx
    
    
  def closestMeetingNode(self, edges: List[int], n1: int, n2: int) -> int:
    d0 = {}
    curr, c0 = n1, 0

    while curr not in d0 and curr >= 0:
      d0[curr] = c0
      curr = edges[curr]
      c0 += 1

    d1 = {}
    curr, c1 = n2, 0

    while curr not in d1 and curr >= 0:
      d1[curr] = c1
      curr = edges[curr]
      c1 += 1
      
    ans = -1
    min_dist = math.inf
    # print(d0, d1)
    
    for i in range(len(edges)):
      # if the node can be reached from both n1 and n2, and the 
      # max distance between the target and n1/n2 is smaller
      # than the one on record, update the result
      if i in d0 and i in d1 and max(d0[i], d1[i]) < min_dist:
        min_dist = max(d0[i], d1[i])
        ans = i
        
    return ans
    