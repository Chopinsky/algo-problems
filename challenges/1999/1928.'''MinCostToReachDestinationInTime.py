'''
There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.

In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.

Example 1:

Input: maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: 11
Explanation: The path to take is 0 -> 1 -> 2 -> 5, which takes 30 minutes and has $11 worth of passing fees.

Example 2:

Input: maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: 48
Explanation: The path to take is 0 -> 3 -> 4 -> 5, which takes 26 minutes and has $48 worth of passing fees.
You cannot take path 0 -> 1 -> 2 -> 5 since it would take too long.

Example 3:

Input: maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: -1
Explanation: There is no way to reach city 5 from city 0 within 25 minutes.

Constraints:

1 <= maxTime <= 1000
n == passingFees.length
2 <= n <= 1000
n - 1 <= edges.length <= 1000
0 <= xi, yi <= n - 1
1 <= timei <= 1000
1 <= passingFees[j] <= 1000 
The graph may contain multiple edges between two nodes.
The graph does not contain self loops.
'''


from typing import List
from collections import defaultdict
from heapq import heappush, heappop
import math


class Solution:
  def minCost(self, maxTime: int, edges: List[List[int]], fees: List[int]) -> int:
    n = len(fees)
    g = [[] for i in range(n)]
    
    for u, v, w in edges:
      g[u].append((v, w))
      g[v].append((u, w))

    times = {}
    q = [(fees[0], 0, 0)]

    while q:
      cost, u, time = heappop(q)
      if time > maxTime:
        continue

      if u == n-1:
        return cost

      if u not in times or time < times[u]:
        times[u] = time
        for v, w in g[u]:
          heappush(q, (cost+fees[v], v, time+w))

    return -1
        
  def minCost(self, maxTime: int, edges: List[List[int]], fees: List[int]) -> int:
    conn = {}
    for u, v, t in edges:
      a, b = min(u, v), max(u, v)
      
      if (a, b) in conn:
        conn[a, b] = min(conn[a, b], t)
      else:
        conn[a, b] = t
        
    roads = defaultdict(list)
    n = len(fees)
    
    for u, v in conn:
      t = conn[u, v]
      if v and u < n-1:
        roads[u].append((v, t))
        
      if u and v < n-1:
        roads[v].append((u, t))
    
    # print(roads)
    stack = [(fees[0], 0, 0, -1)]
    times = [math.inf] * n
    
    while stack:
      c0, t0, u, src = heappop(stack)
      if t0 > maxTime:
        continue
        
      if u == n-1:
        return c0
      
      # a better solution can be found with less time
      # (and potentially higher fee, but lower fee tours
      # may not reach the end in maxTime)
      if times[u] > t0:
        # update the better solution
        times[u] = t0

        # go to neighboring cities
        for v, tt in roads[u]:
          # don't circle back
          if v == src:
            continue
          
          # only push states with allowed time; can't return here
          # if v == n-1, because better solutions can exist in
          # the stack and not checked yet
          if (t0+tt < maxTime) or (t0+tt == maxTime and v == n-1):
            heappush(stack, (c0+fees[v], t0+tt, v))
          
    # print(costs)
    return -1
  