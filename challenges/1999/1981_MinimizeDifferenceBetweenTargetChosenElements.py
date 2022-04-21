'''
You are given an m x n integer matrix mat and an integer target.

Choose one integer from each row in the matrix such that the absolute difference between target and the sum of the chosen elements is minimized.

Return the minimum absolute difference.

The absolute difference between two numbers a and b is the absolute value of a - b.

 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0
Explanation: One possible choice is to:
- Choose 1 from the first row.
- Choose 5 from the second row.
- Choose 7 from the third row.
The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.
Example 2:

Input: mat = [[1],[2],[3]], target = 100
Output: 94
Explanation: The best possible choice is to:
- Choose 1 from the first row.
- Choose 2 from the second row.
- Choose 3 from the third row.
The sum of the chosen elements is 6, and the absolute difference is 94.
Example 3:

Input: mat = [[1,2,9,8,7]], target = 6
Output: 1
Explanation: The best choice is to choose 7 from the first row.
The absolute difference is 1.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 70
1 <= mat[i][j] <= 70
1 <= target <= 800
'''

from typing import List


class Solution:
  def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
    m, n = len(mat), len(mat[0])
    vals, nxt = set(mat[0]), set()
    diff_cap = abs(target - sum([min(mat[i]) for i in range(m)]))
    # print(diff_cap)
    
    for i in range(1, m):
      nxt.clear()
      
      for v1 in vals:
        for v0 in mat[i]:
          if v0+v1 >= target and v0+v1-target >= diff_cap:
            continue
            
          nxt.add(v0+v1)
      
      vals, nxt = nxt, vals
      
    # print(vals)
    return min([abs(v-target) for v in vals]) if vals else diff_cap
    