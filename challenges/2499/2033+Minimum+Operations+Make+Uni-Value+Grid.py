'''
2033. Minimum Operations to Make a Uni-Value Grid

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:

Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:


Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
1 <= x, grid[i][j] <= 10^4
'''

from typing import List
from collections import defaultdict


class Solution:
  def minOperations(self, grid: List[List[int]], x: int) -> int:
    c = defaultdict(int)
    rem = grid[0][0] % x
    
    for r in grid:
      for val in r:
        if val % x != rem:
          return -1
        
        c[val] += 1
          
    arr = sorted(c.items())
    n = len(arr)
    if n <= 1:
      return 0
    
    lc, left = 0, 0
    rc = sum(v[1] for v in arr)
    right = sum(v[1] * ((v[0]-arr[0][0]) // x) for v in arr)
    ops = right
    idx = 0
    # print('init:', arr, rc, right)
    
    for val in range(arr[0][0], arr[-1][0]+x+1, x):
      if val > arr[0][0]:
        right -= rc
        left += lc
        
      ops = min(ops, left+right)
      # print('iter:', val, (left, lc), (right, rc))
      
      if idx < len(arr) and val == arr[idx][0]:
        lc += arr[idx][1]
        rc -= arr[idx][1]
        idx += 1
    
    return ops
        