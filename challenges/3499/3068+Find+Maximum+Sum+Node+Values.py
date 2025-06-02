'''
3068. Find the Maximum Sum of Node Values

There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Bogdan wants the sum of values of tree nodes to be maximum, for which Bogdan can perform the following operation any number of times (including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Bogdan can achieve by performing the operation any number of times.

Example 1:

Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]
Output: 6
Explanation: Bogdan can achieve the maximum sum of 6 using a single operation:
- Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
The total sum of values is 2 + 2 + 2 = 6.
It can be shown that 6 is the maximum achievable sum of values.

Example 2:

Input: nums = [2,3], k = 7, edges = [[0,1]]
Output: 9
Explanation: Bogdan can achieve the maximum sum of 9 using a single operation:
- Choose the edge [0,1]. nums[0] becomes: 2 XOR 7 = 5 and nums[1] become: 3 XOR 7 = 4, and the array nums becomes: [2,3] -> [5,4].
The total sum of values is 5 + 4 = 9.
It can be shown that 9 is the maximum achievable sum of values.

Example 3:

Input: nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
Output: 42
Explanation: The maximum achievable sum is 42 which can be achieved by Bogdan performing no operations.

Constraints:

2 <= n == nums.length <= 2 * 10^4
1 <= k <= 10^9
0 <= nums[i] <= 10^9
edges.length == n - 1
edges[i].length == 2
0 <= edges[i][0], edges[i][1] <= n - 1
The input is generated such that edges represent a valid tree.

[1,2,1]
3
[[0,1],[0,2]]

[2,3]
7
[[0,1]]

[7,7,7,7,7,7]
3
[[0,1],[0,2],[0,3],[0,4],[0,5]]

[0,92,56,3,34,23,56]
7
[[2,6],[4,1],[5,0],[1,0],[3,1],[6,3]]
'''

from typing import List
from collections import defaultdict
from functools import lru_cache, cache


class Solution:
  def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
    e = defaultdict(list)
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)

    @cache
    def dp(u: int, p: int, xor: bool) -> int:
      val = nums[u]
      c = 1 if xor else 0
      s = 0
      change = None

      for v in e[u]:
        if v == p:
          continue

        v0 = dp(v, u, True)  # flip
        v1 = dp(v, u, False) # no-flip

        if v0 > v1:
          c += 1
          s += v0
        else:
          s += v1


        if change is None or change > abs(v0-v1):
          change = abs(v0-v1)

      res0 = s + (val if c%2 == 0 else val^k)
      res1 = 0
      if change is not None:
        c += 1
        res1 = max(res1, s-change+(val if c%2 == 0 else val^k))
      
      return max(res0, res1)

    return dp(0, -1, False)
        
  def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
    n = len(nums)
    e = defaultdict(set)
    p = [i for i in range(n)]
    
    for u, v in edges:
      e[u].add(v)
      e[v].add(u)
      
    curr, nxt = [0], []
    
    while curr:
      for u in curr:
        for v in e[u]:
          if v == 0 or p[v] != v:
            continue
          
          p[v] = u
          e[v].discard(u)
          nxt.append(v)
      
      curr, nxt = nxt, curr
      nxt.clear()
      
    # print(e)
    
    @lru_cache(None)
    def dp(u: int, c: bool) -> int:
      cand = float('inf')
      ops = 1 if c else 0
      s0 = 0
      
      for v in e[u]:
        s1 = dp(v, True)
        s2 = dp(v, False)
        if s1 >= s2:
          s0 += s1
          ops += 1
        else:
          s0 += s2
        
        cand = min(cand, abs(s1-s2))
      
      val = nums[u] if ops%2 == 0 else (nums[u]^k)
      s0 += val
      
      # assume we flip one op to choose the alt result
      if cand < float('inf'):
        s1 = s0 - cand - val + (val ^ k)
        s0 = max(s0, s1)
      
      return s0
    
    return dp(0, 0)
        
  '''
  the idea is to create a dp, where dp[u][parent_toggle_boolean] is the max-sums that we can get for
  the subtree rooted at index-u, and if the edge connecting index-u and the parent node is toggled;

  then we can iterate all dp[v][_] on children nodes, and choose the bigger sum for that subtree:
  max(dp[v][0], dp[v][1]), and if we choose dp[v][1] over dp[v][0], the root at index-u is flipped
  one more times

  note that we can flip the value at index-u one more (or less) time, which will change the current
  value at index-u: val -> val^k, and we need to substract the minimum change to the sums based on this
  flip (minimum change can be found while iterating the dp[v][_]); if val^k - min_sums_change > val, we
  choose to flip one more (or less) time, and this will be the largest sum we can get for dp[u][0/1];

  the final answer is then dp[0][0];
  '''
  def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
    n = len(nums)
    e = defaultdict(set)
    p = [-1 for i in range(n)]
    
    # build the tree rooted at 0
    for u, v in edges:
      e[u].add(v)
      e[v].add(u)
      
    curr, nxt = [0], []
    count = [0]*n
    stack = []
    
    while curr:
      for u in curr:
        e[u].discard(p[u])
        count[u] = len(e[u])
        
        if not e[u]:
          stack.append(u)
          continue
        
        for v in e[u]:
          p[v] = u
          nxt.append(v)
          
      curr, nxt = nxt, curr
      nxt.clear()
    
    # print('init:', p, e, stack)
    
    # use dfs to calculate the largest sums in this tree
    dp = {}
      
    def calc(u: int, c: int):
      s0 = 0
      diff = float('inf')
      
      for v in e[u]:
        diff = min(diff, abs(dp[v][0]-dp[v][1]))
        if dp[v][0] >= dp[v][1]:
          s0 += dp[v][0]
        else:
          s0 += dp[v][1]
          c += 1
      
      v0 = nums[u] if c%2 == 0 else nums[u]^k
      v1 = (v0^k) - diff
      
      return s0 + max(v0, v1)
    
    def update_stack(u: int):
      pu = p[u]
      if pu >= 0:
        count[pu] -= 1
        if not count[pu]:
          stack.append(pu)
    
    def update_sums(u):
      if not e[u]:
        dp[u] = [nums[u], nums[u]^k]
      else:
        dp[u] = [calc(u, 0), calc(u, 1)]
      
    # use dfs to calc dp from bottom up
    while stack:
      u = stack.pop()
      update_stack(u)
      update_sums(u)
    
    return dp[0][0]
        