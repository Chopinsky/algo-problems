'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5
All the values of routes[i] are unique.
sum(routes[i].length) <= 10^5
0 <= routes[i][j] < 10^6
0 <= source, target < 10^6
'''

from typing import List
from collections import defaultdict, deque


class Solution:
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    buses = set()
    b = []
    s = defaultdict(set)
    n = len(routes)
    
    for i, r in enumerate(routes):
      b.append(set(r))
      for s0 in r:
        s[s0].add(i)
        
    # print(b, s)
    curr, nxt = set([source]), set()
    stations = set()
    buses = set()
    cand = set()
    taken = 0
    
    while curr and target not in curr:
      stations |= curr
      
      for s0 in curr:
        cand |= s[s0] - buses
        
      for b0 in cand:
        nxt |= b[b0] - stations
      
      curr, nxt = nxt, curr
      nxt.clear()
      cand.clear()
      taken += 1
    
    return taken if target in curr else -1
        
        
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    if source == target:
      return 0
    
    stops = defaultdict(list)
    bus_stop = {}
    
    for i, route in enumerate(routes):
      bus_stop[i] = set(route)
      
      for r in route:
        stops[r].append(i)
        
    visited = set([source])
    taken = set(i for i in stops[source])
    stack = deque([(i, 1) for i in stops[source]])
    
    while stack:
      bus, num = stack.popleft()
      if target in bus_stop[bus]:
        return num
      
      for stop in bus_stop[bus]:
        if stop in visited:
          continue
          
        visited.add(stop)
        for b in stops[stop]:
          if b in taken:
            continue
            
          taken.add(b)
          stack.append((b, num+1))
      
    return -1
  