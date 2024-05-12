'''
3149. Find the Minimum Cost Array Permutation

You are given an array nums which is a permutation of [0, 1, 2, ..., n - 1]. The score of any permutation of [0, 1, 2, ..., n - 1] named perm is defined as:

score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|

Return the permutation perm which has the minimum possible score. If multiple permutations exist with this score, return the one that is lexicographically smallest among them.

Example 1:

Input: nums = [1,0,2]

Output: [0,1,2]

Explanation:

The lexicographically smallest permutation with minimum cost is [0,1,2]. The cost of this permutation is |0 - 0| + |1 - 2| + |2 - 1| = 2.

Example 2:

Input: nums = [0,2,1]

Output: [0,2,1]

Explanation:

The lexicographically smallest permutation with minimum cost is [0,2,1]. The cost of this permutation is |0 - 1| + |2 - 2| + |1 - 0| = 2.

Constraints:

2 <= n == nums.length <= 14
nums is a permutation of [0, 1, 2, ..., n - 1].
'''

from typing import List
from functools import lru_cache

class Solution:
  '''
  this is a graph problem disguised as an array problem: the essense of the problem is to find
  out the route that visit all numbers [0, 1, .., n-1], and the score of each node is set as 
  `nums[i]`, and then we need the route to have the minimum total score with `sum(abs(u-nums[v]))`,
  where u is the current node, and v is the next node in the route

  so the problem is not turned into a backtrack, dfs problem with a graph where self-reference is 
  not allowed, nor visiting a node already exists in the route (except the last node that's also the
  first node).

  another trick is that the route is a sole cycle that contains all nodes, so it doesn't matter which
  node we shall start with (i.e., [0,1,2,3] and [1,2,3,0] all have the same score), so we fix the first
  node in our dfs with node-0, and the last node shall just add `abs(val-nums[0])` as the score.
  '''
  def findPermutation(self, nums: List[int]) -> List[int]:
    n = len(nums)
    
    @lru_cache(None)
    def score(val: int, mask: int):
      mask |= 1 << val
      if mask == (1<<n)-1:
        return abs(val-nums[0]), tuple([val])
      
      min_score = float('inf')
      perm = None
      
      for i in range(n):
        if mask & (1<<i) > 0:
          continue

        # align val in [perm] with num in [nums]
        nxt_score, nxt_perm = score(i, mask)
        nxt_score += abs(val-nums[i])
        # if val == 0:
        #   print('iter:', nxt_score, nxt_perm)
          
        if nxt_score < min_score:
          min_score = nxt_score
          perm = nxt_perm
      
      return min_score, tuple([val]) + perm
      
    _, perm = score(0, 1)
    
    return perm
        