'''
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:

Get the XOR of all the values of the nodes for each of the three components respectively.
The difference between the largest XOR value and the smallest XOR value is the score of the pair.
For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
Return the minimum score of any possible pair of edge removals on the given tree.

Example 1:

Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
Output: 9
Explanation: The diagram above shows a way to make a pair of removals.
- The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
- The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
- The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
It can be shown that no other pair of removals will obtain a smaller score than 9.

Example 2:

Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
Output: 0
Explanation: The diagram above shows a way to make a pair of removals.
- The 1st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
- The 2nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
- The 3rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
We cannot obtain a smaller score than 0.

Constraints:

n == nums.length
3 <= n <= 1000
1 <= nums[i] <= 10^8
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
'''

from typing import List
from collections import defaultdict
from functools import reduce
import math


class Solution:
  def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
    e = defaultdict(list)
    n = len(nums)
    cnt = [0] * n
    subtree_xor = [0] * n
    cand = []
    whole_tree_xor = reduce(lambda x, y: x^y, nums, 0)
    min_score = math.inf
    
    # build the topical-sort-ish candidates
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
      cnt[u] += 1
      cnt[v] += 1
      
    for i in range(n):
      if cnt[i] == 1:
        cand.append(i)
        
    # print(cand, whole_tree_xor)
    idx, s0 = 0, 0
    seen = set()
    
    def drill_down(u: int, p: int) -> int:
      nonlocal min_score, s0
      subtree_score = nums[u]
      
      for v in e[u]:
        if v == p:
          continue
          
        s1 = drill_down(v, u)
        s2 = whole_tree_xor ^ s0 ^ s1
        subtree_score ^= s1
        
        # print('visit:', p, u, v, s0, s1, s2, max(s0, s1, s2) - min(s0, s1, s2))
        min_score = min(min_score, max(s0, s1, s2) - min(s0, s1, s2))
        
      return subtree_score
    
    while idx < len(cand):
      u = cand[idx]
      p = -1
      subtree_xor[u] = nums[u]
      
      for v in e[u]:
        if v in seen:
          subtree_xor[u] ^= subtree_xor[v]
          
        else:
          p = v
          cnt[v] -= 1
          
          # add node to the candidate list
          if cnt[v] == 1:
            cand.append(v)
      
      # all nodes have been visited
      if p == -1:
        break
        
      # update paramenters and try to find the min score
      s0 = subtree_xor[u]
      drill_down(p, u)
      
      # done and move on
      seen.add(u)
      idx += 1
    
    return min_score
  