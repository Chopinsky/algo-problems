'''
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]

Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 10^5
-10^5 <= nums[i], ui, vi <= 10^5
There exists some nums that has adjacentPairs as its pairs.
'''

from typing import List
from collections import defaultdict


class Solution:
  def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    e = defaultdict(list)
    for u, v in adjacentPairs:
      e[u].append(v)
      e[v].append(u)
    
    curr, last = None, None
    for u, neig in e.items():
      if len(neig) == 1:
        curr = u
        break
        
    arr = []
    # print(curr, e)
    
    while curr is not None:
      arr.append(curr)
      cand = e[curr]
      tmp = curr
      
      if cand[0] != last:
        curr = cand[0]
      elif len(cand) > 1:
        curr = cand[1]
      else:
        curr = None
        
      last = tmp

    return arr
        
        
  def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
    edges = defaultdict(list)
    for u, v in adjacentPairs:
      edges[u].append(v)
      edges[v].append(u)
      
    res = []
    curr = -1
    seen = set()
    
    for u, neig in edges.items():
      if len(neig) == 1:
        curr = neig[0]
        res.append(u)
        res.append(curr)
        seen.add(u)
        seen.add(curr)
        break
        
    while len(edges[curr]) > 1:
      for v in edges[curr]:
        if v in seen:
          continue
          
        curr = v
        break
      
      seen.add(curr)
      res.append(curr)
      
    return res
  