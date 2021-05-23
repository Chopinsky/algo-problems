'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

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

from typing import List

class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    if n == 1:
      return [['Q']]

    ans = []
    stack = []
    cols = set()
    d1 = set()
    d2 = set()

    def find(row: int):
      for i in range(n):
        if i in cols:
          continue

        if (row-i in d1) or (row+i in d2):
          continue

        if row == n-1:
          # print results and save it to the ans
          a = []
          for j in range(n-1):
            r = ""
            for col in range(n):
              r += "Q" if col == stack[j] else "."

            a.append(r)

          r = ""
          for col in range(n):
            r += "Q" if col == i else "."

          a.append(r)
          ans.append(a)

          return

        # add queen to cell (row, i)
        stack.append(i)
        cols.add(i)
        d1.add(row-i)
        d2.add(row+i)

        find(row+1)

        # backtrack
        stack.pop()
        cols.remove(i)
        d1.remove(row-i)
        d2.remove(row+i)

    find(0)

    return ans
