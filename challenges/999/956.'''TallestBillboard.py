'''
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.

Constraints:

1 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods[i]) <= 5000
'''


from typing import List


class Solution:
  def tallestBillboard(self, rods: List[int]) -> int:
    n = len(rods)
    if n == 1:
      return 0
    
    dp = {0:0}
    for ln in rods:
      nxt = dp.copy()
      
      for diff, h in dp.items():
        # if placed on the taller side
        d0 = diff+ln 
        nxt[d0] = max(nxt.get(d0, 0), h)
        
        # if placed on the shorter side
        d1 = abs(diff-ln)
        nxt[d1] = max(nxt.get(d1, 0), h+min(ln, diff))
        
      dp = nxt
      
    return dp[0]
  
  
  def tallestBillboard0(self, rods: List[int]) -> int:
    n = len(rods)
    if n == 1:
      return 0
    
    if n == 2:
      return rods[0] if rods[0] == rods[1] else 0
    
    rods.sort(reverse=True)
    cap = sum(rods) // 2
    high = 0
    
    prefix = [val for val in rods]
    for i in range(n-2, -1, -1):
      prefix[i] += prefix[i+1]
      
    cache = set()
    def weld(i: int, l: int, r: int):
      nonlocal high
      
      # a match, update
      if l == r:
        high = max(high, l)
        
      if ((i, l, r) in cache) or ((i, r, l) in cache):
        return
      
      cache.add((i, l, r))

      # the remainder rods won't make up the diff, or we're
      # out of the rods to distribute
      if i >= n or abs(l-r) > prefix[i] or l > cap or r > cap:
        return
      
      # the high is in
      if (r+l+prefix[i]) // 2 <= high:
        return
      
      # trim the branches if we have the solution in hands
      if l == r+prefix[i] or r == l+prefix[i]:
        high = max(high, l, r)
        return
      
      # if skip this rod
      weld(i+1, l, r)
      
      # if use it for the left set
      weld(i+1, l+rods[i], r)
      
      # if use it for the right set
      weld(i+1, l, r+rods[i])
    
    weld(0, 0, 0)
    
    return high
  