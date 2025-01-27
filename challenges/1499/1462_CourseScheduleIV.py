'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
Example 3:

Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

Constraints:

2 <= numCourses <= 100
0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
prerequisites[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 10^4
0 <= ui, vi <= n - 1
ui != vi
'''

from typing import List
from collections import defaultdict


class Solution:
  def checkIfPrerequisite(self, n: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
    ans = []
    e = defaultdict(list)
    cnt = defaultdict(int)
    pre_courses = defaultdict(set)
    cand = set([i for i in range(n)])

    for u, v in pre:
      e[u].append(v)
      cnt[v] += 1
      cand.discard(v)

    # print('init:', e, cnt, cand)
    cand = list(cand)
    
    while cand:
      u = cand.pop()
      for v in e[u]:
        pre_courses[v].add(u)
        pre_courses[v] |= pre_courses[u]
        cnt[v] -= 1
        if not cnt[v]:
          cand.append(v)

    for u, v in queries:
      ans.append(u in pre_courses[v])

    return ans
        
  def checkIfPrerequisite(self, n: int, req: List[List[int]], q: List[List[int]]) -> List[bool]:
    e = defaultdict(list)
    dep = defaultdict(int)
    roots = set([i for i in range(n)])
    
    for u, v in req:
      e[u].append(v)
      dep[v] += 1
      roots.discard(v)
      
    # print(roots)
    ranks = [set() for i in range(n)]
    stack, nxt = list(roots), []
    d = 1
    
    while stack:
      for u in stack:
        for v in e[u]:
          ranks[v] |= ranks[u] | {u}
          dep[v] -= 1
          
          if not dep[v]:
            nxt.append(v)
      
      stack, nxt = nxt, stack
      nxt.clear() 
      d += 1
    
    ans = [True] * len(q)
    # print(ranks)
    
    for i in range(len(q)):
      u, v = q[i]
      ans[i] = u in ranks[v]
    
    return ans
        