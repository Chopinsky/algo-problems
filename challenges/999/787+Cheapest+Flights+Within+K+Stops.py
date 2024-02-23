'''
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 10^4
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop
import math

class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    if src == dst:
      return 0
    
    e = defaultdict(list)
    for u, v, p in flights:
      e[u].append((v, p))
      
    # print(e)
    visited = {src:0}
    curr, nxt = [(src, 0)], []
    stops = 0
    cost = float('inf')
    
    while curr and stops <= k:
      # print(stops, curr)
      for u, p0 in curr:
        for v, p1 in e[u]:
          p2 = p0+p1
          if v in visited and p2 >= visited[v]:
            continue
            
          visited[v] = p2
          nxt.append((v, p2))
          
          if v == dst:
            cost = min(cost, p2)
      
      curr, nxt = nxt, curr
      nxt.clear()
      stops += 1
      
    return cost if cost < float('inf') else -1
        
        
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    e = defaultdict(list)
    for u, v, p in flights:
      e[u].append((v, p))
      
    stack = [(0, src, k)]
    visit = {}
    curr_low = math.inf
    
    while stack:
      cost, u, stops = heappop(stack)
      if u == dst:
        curr_low = min(curr_low, cost)
        continue
        
      for v, p in e[u]:
        if v not in visit:
          visit[v] = {}
        
        # no more stops to make in the route
        if stops == 0 and v != dst:
          continue
          
        nxt_cost = cost + p
        if nxt_cost >= visit[v].get(stops-1, math.inf) or nxt_cost >= curr_low:
          continue
        
        visit[v][stops-1] = nxt_cost
        heappush(stack, (nxt_cost, v, stops-1))
    
    return -1 if curr_low == math.inf else curr_low
    