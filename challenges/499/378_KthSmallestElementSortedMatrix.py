'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n^2

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
'''

from typing import List
from heapq import heappop, heappush


class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    if k == 1 or n == 1:
      return matrix[0][0]
    
    cand = [(matrix[i][0], i, 0) for i in range(n-1, 0, -1)]
    stack = [(matrix[0][1], 0, 1)]
    cnt = 1
    last = matrix[0][0]
    
    while cnt < k and (stack or cand):
      if not stack:
        last, i, j = cand.pop()
      elif not cand:
        last, i, j = heappop(stack)
      else:
        if cand[-1][0] <= stack[0][0]:
          last, i, j = cand.pop()
        else:
          last, i, j = heappop(stack)
        
      cnt += 1
      if j+1 < n:
        heappush(stack, (matrix[i][j+1], i, j+1))
      
    return last
    