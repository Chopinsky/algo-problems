'''
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-10 ** 5 <= k <= 10 ** 5

Follow up: What if the number of rows is much larger than the number of columns?
'''

import bisect
import math
from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class Solution:
  def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    m, n = len(matrix), len(matrix[0])
    prefix = [[val for val in matrix[i]] for i in range(m)]
    
    for i in range(m):
      for j in range(1, n):
        prefix[i][j] += prefix[i][j-1]
        
    # print(prefix)
    max_val = -math.inf
    lst = SortedList()
    
    def calc_sums(col: int, ln: int) -> int:
      lst.clear()
      max_sum = -math.inf
      curr = 0
      
      for i in range(m):
        if col == ln-1:
          s = prefix[i][col]
        else:
          s = prefix[i][col] - prefix[i][col-ln]
          
        if s <= k:
          max_sum = max(max_sum, s)

        curr += s
        if curr <= k:
          max_sum = max(max_sum, curr)
        
        if lst:
          idx = lst.bisect_left(curr-k)
          if idx < len(lst):
            max_sum = max(max_sum, curr-lst[idx])
          
        lst.add(curr)
      
      # print(col, ln, max_sum)
      return max_sum
    
    for ln in range(1, n+1):
      for j in range(ln-1, n):
        max_val = max(max_val, calc_sums(j, ln))
        if max_val == k:
          return k
    
    return max_val
    

class Solution0:
  def maxSumSubmatrix0(self, matrix: List[List[int]], k: int) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    stacks = defaultdict(list)
    s = -math.inf
    
    for i in range(m):
      row = 0
      
      for j in range(n):
        if matrix[i][j] == k:
          return k

        row += matrix[i][j]
        dp[i][j] = row
        
        if i > 0:
          dp[i][j] += dp[i-1][j]
          
        if dp[i][j] == k:
          return k
        
        for l in range(j):
          rect = dp[i][j] - dp[i][l]
          if rect == k:
            return k
          
          if rect < k and rect > s:
            s = rect
          
          target = k - rect
          
          if len(stacks[(j, l)]) > 0:
            idx = bisect.bisect_left(stacks[(j, l)], target)
            if idx >= 0 and idx < len(stacks[(j, l)]):
              sub_rect = rect - stacks[(j, l)][idx]
              if sub_rect == k:
                return k
              
              if sub_rect < k and sub_rect > s:
                s = sub_rect
          
          bisect.insort(stacks[(j, l)], rect)
        
    # print(dp)
    
    return s
    
  def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    row_size, col_size = len(matrix), len(matrix[0])

    if any(k in row for row in matrix):
      return k

    ans = -math.inf

    for y1 in range(col_size):
      prefix_sums = [0] * row_size

      for y2 in range(y1, col_size):
        for row in range(row_size):
          prefix_sums[row] += matrix[row][y2]

        result_big = -math.inf
        result_small = math.inf

        cur_big_sum = 0
        cur_small_sum = 0

        for x in prefix_sums:
          if cur_big_sum < 0:
            cur_big_sum = x
          else:
            cur_big_sum += x

          if cur_big_sum > result_big:
            result_big = cur_big_sum

          if cur_small_sum > 0:
            cur_small_sum = x
          else:
            cur_small_sum += x

          if cur_small_sum < result_small:
            result_small = cur_small_sum

          if result_big <= k:
            ans = max(ans, result_big)
            if ans == k:
              return k

            continue

          if result_small > k:
            continue

          cur, my_arr, local_res = 0, [0], ans
          for x in prefix_sums:
            cur += x
            if my_arr[-1] >= cur-k:
              local_res = max(local_res, cur - my_arr[bisect.bisect_left(my_arr, cur - k)])

            bisect.insort(my_arr, cur)

          ans = local_res
          if ans == k:
            return k

    return ans
  