'''
2718. Sum of Matrix After Queries

You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].

Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:

if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
Return the sum of integers in the matrix after all queries are applied.

Example 1:


Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
Output: 23
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23. 
Example 2:

Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
Output: 17
Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 17.

Constraints:

1 <= n <= 104
1 <= queries.length <= 5 * 10^4
queries[i].length == 3
0 <= typei <= 1
0 <= indexi < n
0 <= vali <= 10^5
'''

from typing import List


class Solution:
  def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
    rows = set()
    cols = set()
    total = 0
    
    for t, idx, val in queries[::-1]:
      # already set, skip
      if (t == 0 and idx in rows) or (t == 1 and idx in cols):
        continue
        
      s0 = 0
      if t == 0:
        rows.add(idx)
        s0 = (n-len(cols)) * val
      else:
        cols.add(idx)
        s0 = (n-len(rows)) *val
        
      # print((t,idx,val), s0)
      total += s0
      
    return total
        