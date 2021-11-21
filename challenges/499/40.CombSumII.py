'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''


from typing import List
from functools import lru_cache


class Solution:
  def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
    cand.sort()
    comb, results = [], []
    n = len(cand)
    
    def backtrack(curr: int, remain: int):
      if remain == 0:
        # make a deep copy of the resulted combination
        results.append(list(comb))
        return

      for i in range(curr, n):
        # skip duplicate starters
        if i > curr and cand[i] == cand[i-1]:
          continue

        # optimization: skip the rest of elements starting from 'curr' index
        if remain - cand[i] < 0:
          break

        comb.append(cand[i])
        backtrack(i+1, remain-cand[i])
        comb.pop()
    
    backtrack(0, target)
    return results
      
      
  def combinationSum20(self, cand: List[int], target: int) -> List[List[int]]:
    cand.sort()
    n = len(cand)
      
    @lru_cache(None)
    def dfs(curr: int, t: int):
      if curr >= n or t < 0:
        return []
      
      res = set()
      for i in range(curr, n):
        if cand[i] >= t:
          if cand[i] == t:
            res.add(tuple([t]))
            
          break
          
        # use cand[i], check cand[i+1:] with target of t-cand[i]
        for nxt in dfs(i+1, t-cand[i]):
          res.add(tuple([cand[i]] + list(nxt)))
      
      return list(res)
    
    return dfs(0, target)
  