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
    dp = {0:0}
    
    for h in rods:
      # if we don't use the rods, nothing is changed, so we
      # keep all the previous calculations
      nxt = dp.copy()
      
      # diff is the height difference between the tall/short legs,
      # and curr is the current height of the shorter leg, loop to
      # find the tallest short leg for a given diff between the 
      # short/tall legs
      for diff, short in dp.items():
        # put the rod on the taller leg
        nxt[diff+h] = max(
          nxt.get(diff+h, 0),
          short,
        )
        
        # put the rod on the shorter leg
        nxt[abs(diff-h)] = max(
          nxt.get(abs(diff-h), 0),
          # if h <= diff, short leg remain short, i.e. `short+h`, otherwise, 
          # switch, long leg's height is not affected and remains `short+diff`
          # but it becomes the short leg of the pair
          short + min(h, diff),
        )
      
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
  