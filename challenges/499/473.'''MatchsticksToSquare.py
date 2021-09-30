'''
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

Constraints:

1 <= matchsticks.length <= 15
0 <= matchsticks[i] <= 10 ** 9
'''

from typing import List
from collections import defaultdict

class Solution:
  def makesquare0(self, m: List[int]) -> bool:
    n = len(m)
    if n < 4:
      return False

    total = 0
    longest = 0
    md = defaultdict(int)
    
    for match in m:
      total += match
      longest = max(longest, match)
      md[match] += 1
    
    side = sum(m) // 4
    
    if side * 4 != total:
      return False
    
    if longest > side:
      return False
    
    if n == 4:
      return min(m) == side
    
    sides = 4 - md[side]
    del md[side]
    
    matches = []
    for ml, cnt in md.items():
      matches += [ml] * cnt
    
    done = set()
    matches.sort(reverse=True)
    
    def dfs(idx: int, rem: int) -> bool:
      if idx >= len(matches):
        return False
      
      if idx in done:
        return dfs(idx+1, rem)
      
      if matches[idx] == rem:
        done.add(idx)
        return True
      
      if matches[idx] < rem:
        done.add(idx)
        if dfs(idx+1, rem-matches[idx]):
          return True
        
        done.remove(idx)
        return dfs(idx+1, rem)
        
      return dfs(idx+1, rem)
      
    # print(sides, side, matches)
    
    for _ in range(sides):
      if not dfs(0, side):
        return False
      
    return True
  
  def makesquare(self, A: List[int]) -> bool:
    sm = sum(A)
    n = len(A)
    
    if sm % 4 != 0: 
      return False
    
    A.sort(reverse=True)
    side = sm // 4
    done = set()

    def dfs(i, rem):
      nonlocal side
      
      # the match can't fit into any side, fail
      if A[i] > side:
        return False

      # has more to finish the side but we've run
      # out of matches to finish it, incomplete
      if i == n: 
        return False

      # match already used, done, move on to the
      # next match
      if i in done: 
        return dfs(i + 1, rem)

      # this match will finish the side just fine,
      # move on to the next side
      if A[i] == rem: 
        done.add(i)
        return True

      # add the match to the side, try and see; if
      # it's not going to work out, backtrack
      if A[i] < rem: 
        done.add(i)
        if dfs(i+1, rem-A[i]):
          return True
        
        # don't use the match for this side
        done.remove(i)
        return dfs(i+1, rem)

      # match is too long to fit into the remainder requirements,
      # must move on
      return dfs(i+1, rem)

    # run for all 4 sides
    for _ in range(4):
      # if either of the side can't be formed from 
      # the (remaining) matches, it's not going to 
      # work
      if not dfs(0, side): 
        return False
        
    return True
      
  def makesquare1(self, m: List[int]) -> bool:
    n = len(m)
    if n < 4:
      return False

    total = 0
    longest = 0
    md = defaultdict(int)
    
    for match in m:
      total += match
      longest = max(longest, match)
      md[match] += 1
    
    side = sum(m) // 4
    
    if side * 4 != total:
      return False
    
    if longest > side:
      return False
    
    if n == 4:
      return min(m) == side
    
    sides = 4 - md[side]
    del md[side]
    
    matches = []
    side_len = [0] * sides
    
    for ml, cnt in md.items():
      matches += [ml] * cnt
          
    matches.sort(reverse=True)
    # print(total, side, sides, md)
    # print(matches, side_len)
    
    def iterate(idx: int) -> bool:
      if idx >= len(matches):
        return True
      
      l = matches[idx]
      
      for i in range(sides):
        if side_len[i] + l > side:
          continue
          
        side_len[i] += l
        if iterate(idx+1):
          return True
        
        side_len[i] -= l
          
      return False
    
    return iterate(0)
  