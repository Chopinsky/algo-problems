'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''

from typing import List
from collections import defaultdict


class Solution:
  def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    cand = []
    m = len(board)
    n = len(board[0])
    cols = defaultdict(set)
    rows = defaultdict(set)
    blocks = defaultdict(set) 

    for x in range(m):
      for y in range(n):
        if board[x][y] == '.':
          cand.append((x, y))
        else:
          val = int(board[x][y])
          rows[x].add(val)
          cols[y].add(val)
          blocks[x//3, y//3].add(val)

    # print('init:', cand, rows, cols, blocks)
    def check(x: int, y: int, val: int):
      if val in rows[x]:
        return False

      if val in cols[y]:
        return False

      if val in blocks[x//3, y//3]:
        return False

      return True

    def guess(i: int) -> bool:
      if i >= len(cand):
        return True

      x, y = cand[i]
      for val in range(1, 10):
        if not check(x, y, val):
          continue

        # use val
        rows[x].add(val)
        cols[y].add(val)
        blocks[x//3, y//3].add(val)

        if guess(i+1):
          board[x][y] = str(val)
          return True

        rows[x].discard(val)
        cols[y].discard(val)
        blocks[x//3, y//3].discard(val)

      return False

    guess(0)
        
  def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    
    blocks = [set() for _ in range(9)]
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    base = set([i for i in range(1, 10)])
    stack = []
    o0 = ord('0')
    
    def get_block_num(i: int, j: int) -> int:
      r = i // 3
      c = j // 3
      
      return r*3 + c
    
    for i in range(9):
      for j in range(9):
        if board[i][j] == '.':
          stack.append((i, j))
          continue
        
        val = ord(board[i][j]) - o0
        b = get_block_num(i, j)
        
        blocks[b].add(val)
        rows[i].add(val)
        cols[j].add(val)
    
    # print(blocks, rows, cols)
    # print(stack)
    # print(base-blocks[0]-rows[0]-cols[2])
    
    # the grid is already filled
    if not stack or len(stack) == 0:
      return
    
    def iterate(idx: int) -> bool:      
      x, y = stack[idx]
      b = get_block_num(x, y)
      nums = list(base - blocks[b] - rows[x] - cols[y])
      if not nums or len(nums) == 0:
        return False
      
      for curr in nums:
        blocks[b].add(curr)
        rows[x].add(curr)
        cols[y].add(curr)
        board[x][y] = chr(curr + o0)
        
        if idx == len(stack)-1:
          return True
        
        if iterate(idx+1):
          return True

        blocks[b].remove(curr)
        rows[x].remove(curr)
        cols[y].remove(curr)
        board[x][y] = '.'
      
      return False
    
    iterate(0)
    print(rows)
    
    return
        