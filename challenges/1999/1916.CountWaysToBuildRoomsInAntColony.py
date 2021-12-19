'''
You are an ant tasked with adding n new rooms numbered 0 to n-1 to your colony. You are given the expansion plan as a 0-indexed integer array of length n, prevRoom, where prevRoom[i] indicates that you must build room prevRoom[i] before building room i, and these two rooms must be connected directly. Room 0 is already built, so prevRoom[0] = -1. The expansion plan is given such that once all the rooms are built, every room will be reachable from room 0.

You can only build one room at a time, and you can travel freely between rooms you have already built only if they are connected. You can choose to build any room as long as its previous room is already built.

Return the number of different orders you can build all the rooms in. Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input: prevRoom = [-1,0,1]
Output: 1
Explanation: There is only one way to build the additional rooms: 0 → 1 → 2

Example 2:

Input: prevRoom = [-1,0,0,1,2]
Output: 6
Explanation:
The 6 ways are:
0 → 1 → 3 → 2 → 4
0 → 2 → 4 → 1 → 3
0 → 1 → 2 → 3 → 4
0 → 1 → 2 → 4 → 3
0 → 2 → 1 → 3 → 4
0 → 2 → 1 → 4 → 3

Constraints:

n == prevRoom.length
2 <= n <= 10^5
prevRoom[0] == -1
0 <= prevRoom[i] < n for all 1 <= i < n
Every room is reachable from room 0 once all the rooms are built.
'''


from typing import List
from collections import defaultdict
from functools import lru_cache
import math


class Solution:
  def waysToBuildRooms(self, p: List[int]) -> int:
    n = len(p)
    mod = 1_000_000_007
    edges = [[] for i in range(n)] 
    
    # get all edges
    for i in range(1, len(p)):
      edges[p[i]].append(i)

    # the number of rooms below the i-th room
    counts = [1 for _ in range(n)]
    
    # count the number of rooms in the subtree
    def dfs(u: int) -> int: 
      for v in edges[u]:
        counts[u] += dfs(v)

      return counts[u]

    dfs(0)
    factor, base = 1, 1
    
    # calc the total ways to arrange the rooms
    for i in range(n):
      factor = (factor * (i+1)) % mod
      base = (base * counts[i]) % mod
      
    # answer: n! / prod_of_all_counts
    return (factor * pow(base, -1, mod)) % mod
      
    
  def waysToBuildRooms0(self, prevRoom: List[int]) -> int:
    e = defaultdict(list)
    mod = 1_000_000_007
    
    for v, u in enumerate(prevRoom):
      if v == 0:
        continue
      
      e[u].append(v)
      
    @lru_cache(None)
    def count_rooms(u: int) -> int:
      cnt = 1
      for v in e[u]:
        cnt += count_rooms(v)
        
      return cnt
      
    def build(u: int) -> int:
      if not e[u]:
        return 1
      
      if len(e[u]) == 1:
        return build(e[u][0])
      
      base = 1
      sub_rooms = count_rooms(u)-1
      
      for v in e[u]:
        # print(v, sub_rooms, build(v))
        rc = count_rooms(v)
        cnt = (build(v) * math.comb(sub_rooms, rc)) % mod
        base = (base * cnt) % mod
        sub_rooms -= rc
      
      return base
    
    return build(0)
  