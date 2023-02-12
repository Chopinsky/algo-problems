'''
2477. Minimum Fuel Cost to Report to the Capital

There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.

Example 1:


Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation: 
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum. 
It can be proven that 3 is the minimum number of liters of fuel needed.
Example 2:

Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
Output: 7
Explanation: 
- Representative2 goes directly to city 3 with 1 liter of fuel.
- Representative2 and representative3 go together to city 1 with 1 liter of fuel.
- Representative2 and representative3 go together to the capital with 1 liter of fuel.
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative5 goes directly to the capital with 1 liter of fuel.
- Representative6 goes directly to city 4 with 1 liter of fuel.
- Representative4 and representative6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum. 
It can be proven that 7 is the minimum number of liters of fuel needed.
Example 3:

Input: roads = [], seats = 1
Output: 0
Explanation: No representatives need to travel to the capital city.

Constraints:

1 <= n <= 10^5
roads.length == n - 1
roads[i].length == 2
0 <= ai, bi < n
ai != bi
roads represents a valid tree.
1 <= seats <= 10^5
'''


from collections import defaultdict
from typing import List
from heapq import heappush, heappop
from math import ceil


class Solution:
  def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
    e = defaultdict(set)
    for u, v in roads:
      e[u].add(v)
      e[v].add(u)
      
    cand = []
    n = len(roads) + 1
    count = [1] * n
    costs = 0
    
    for u in e:
      if u != 0 and len(e[u]) == 1:
        cand.append(u)
        
    # print(cand)
    
    while cand:
      u = cand.pop()
      # print('check:', u)
      
      for v in e[u]:
        count[v] += count[u]
        costs += ceil(count[u] / seats)
        e[v].discard(u)
        
        if len(e[v]) == 1 and v != 0:
          # print(f'move: {u} ({count[u]}) -> {v}')
          cand.append(v)
    
    return costs
  

  def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
    edges = defaultdict(list)
    n = len(roads)+1
    cand = set()
    
    for u, v in roads:
      edges[u].append(v)
      edges[v].append(u)
      
    dist = [0] * n
    parent = [-1] * n
    cnt = [1] * n
    curr, nxt = [0], []
    d = 0
    seen = {0}
    
    while curr:
      d += 1
      for u in curr:
        if len(edges[u]) == 1:
          cand.add(u)
          
        for v in edges[u]:
          if v in seen:
            continue
            
          dist[v] = d
          parent[v] = u
          
          nxt.append(v)
          seen.add(v)
          
      curr, nxt = nxt, curr
      nxt.clear()
      
    # print(dist, cand)
    q = []
    
    for u in cand:
      if u != 0:
        heappush(q, (-dist[u], u))
    
    cost = 0
    seen.clear()
    
    while q:
      _, u = heappop(q)
      # print(u)
      
      v = parent[u]
      cost += (cnt[u] // seats) + (0 if cnt[u] % seats == 0 else 1)
      
      if v > 0:
        cnt[v] += cnt[u]
        if v not in seen:
          heappush(q, (-dist[v], v))
          seen.add(v)
    
    return cost
    