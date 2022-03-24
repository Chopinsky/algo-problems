'''
You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.

 

Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 10^6
1 <= k <= m * n
'''


from typing import List
from heapq import heappush, heappushpop


class Solution:
  def kthLargestValue(self, mat: List[List[int]], k: int) -> int:
    m, n = len(mat), len(mat[0])
    h = []
    xor = [[0] * n for _ in range(m)]
    
    for i in range(m):
      row = 0
      for j in range(n):
        row ^= mat[i][j]
        val = (row if i == 0 else row^xor[i-1][j])
        xor[i][j] = val
        # print(i, j, mat[i][j], row, 0 if i == 0 else xor[i-1][j], val)
        
        if len(h) < k:
          heappush(h, val)
        else:
          heappushpop(h, val)
    
    return h[0]
    