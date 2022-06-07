'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]

Constraints:

1 <= n <= 9
'''

from typing import List, Set


class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    ans = []
    rows = []
    
    def dp(i: int, col: Set[int], d0: Set[int], d1: Set[int]):
      if i >= n:
        ans.append(rows.copy())
        return
      
      for j in range(n):
        if j in col or i-j in d0 or i+j in d1:
          continue
          
        col.add(j)
        d0.add(i-j)
        d1.add(i+j)
        rows.append('.'*j + 'Q' + '.'*(n-1-j))
        
        dp(i+1, col, d0, d1)
        
        col.discard(j)
        d0.discard(i-j)
        d1.discard(i+j)
        rows.pop()
    
    dp(0, set(), set(), set())
    
    return ans
    