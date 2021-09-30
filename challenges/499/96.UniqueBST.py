'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:

Input: n = 3
Output: 5

Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 19
'''


from functools import lru_cache


class Solution:
  def numTrees(self, n: int) -> int:
    @lru_cache(None)
    def find(i: int, j: int) -> int:
      if i == j:
        return 1
      
      if j-i == 1:
        return 2
      
      if j-i == 2:
        return 5
      
      count = 0
      for k in range(i, j+1):
        l, r = 1, 1
        
        if k > i:
          l = find(i, k-1)
          
        if k < j:
          r = find(k+1, j)
          
        count += l * r
      
      return count
    
    return find(1, n)
  