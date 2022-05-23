'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop
import math


class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    dist = [math.inf] * n
    e = defaultdict(list)
    
    for u, v, w in times:
      e[u-1].append((v-1, w))
    
    stack = [(0, k-1)]
    dist[k-1] = 0
    
    while stack:
      t, u = heappop(stack)
      if t > dist[u]:
        continue
        
      for v, w in e[u]:
        if t+w >= dist[v]:
          continue
          
        dist[v] = t + w
        heappush(stack, (t+w, v))
    
    max_dist = max(dist)
    # print(dist)
    
    return -1 if max_dist == math.inf else max_dist
    