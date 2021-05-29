'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

Constraints:

1 <= n <= 9
'''

class Solution:
  def totalNQueens(self, n: int) -> int:
    count = [0]
    if n == 1:
      return 1

    d0 = set()
    d1 = set()
    col = set()

    def recur(i: int):
      if i >= n:
        # print("done")
        count[0] += 1
        return

      for j in range(n):
        if j in col:
          continue

        diag = i-j
        invDiag = i+j

        if diag in d0 or invDiag in d1:
          continue

        d0.add(diag)
        d1.add(invDiag)
        col.add(j)

        recur(i+1)

        d0.remove(diag)
        d1.remove(invDiag)
        col.remove(j)

    recur(0)

    return count[0]
