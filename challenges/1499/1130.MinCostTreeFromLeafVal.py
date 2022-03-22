'''
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.

Example 1:


Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
Example 2:


Input: arr = [4,11]
Output: 44

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 231).
'''

import math
from typing import List
from functools import lru_cache


class Solution:
  def mctFromLeafValues(self, arr: List[int]) -> int:
    @lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i == j:
        return 0 #arr[i]
      
      if i+1 == j:
        return arr[i]*arr[j]
      
      res = math.inf
      left = 0
      right = []
      
      for k in range(j, i, -1):
        if not right or arr[k] > right[-1][0]:
          right.append((arr[k], k))
      
      for k in range(i, j):
        left = max(left, arr[k])
        while right and right[-1][1] <= k:
          right.pop()
          
        res = min(res, left * right[-1][0] + dp(i, k) + dp(k+1, j))
      
      return res
    
    return dp(0, len(arr)-1)
  