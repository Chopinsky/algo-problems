'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
'''

from typing import List
from collections import defaultdict


class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    root = {}
    
    def find(x):
      if x not in root:
        root[x] = (x, 1)
      
      coeff = 1
      while root[x][0] != x:
        coeff *= root[x][1]
        x = root[x][0]
        
      return x, coeff
    
    def union(x, y, c):
      rx, cx = find(x)
      ry, cy = find(y)
      
      if rx < ry:
        root[ry] = (rx, cx/(cy*c))
      elif ry < rx:
        root[rx] = (ry, (cy*c)/cx)
        
    for [u, v], c in zip(equations, values):
      union(u, v, c)
        
    # print(root)
    ans = []  
      
    for x, y in queries:
      if x not in root or y not in root:
        ans.append(-1.0)
        continue
        
      rx, cx = find(x)
      ry, cy = find(y)
      
      if rx != ry:
        ans.append(-1.0)
      else:
        ans.append(cx/cy)
      
    return ans
      
      
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    e = defaultdict(dict)
    
    for i in range(len(equations)):
      a, b = equations[i]
      val = values[i]
      e[a][b] = val
      e[b][a] = 1.0 / val
      
    # print(e)
    ans = [-1] * len(queries)
    
    def find(x, y, seen):
      if x == y:
        return 1.0
      
      for z in e[x]:
        if z in seen:
          continue
          
        seen.add(z)
        val = e[x][z]
        res = find(z, y, seen)
        
        if res > 0:
          return val * res
        
      return -1
    
    seen = set()
    for i, [a, b] in enumerate(queries):
      if a not in e or b not in e:
        continue
        
      seen.clear()
      seen.add(a)
      
      ans[i] = find(a, b, seen)
    
    return ans
        