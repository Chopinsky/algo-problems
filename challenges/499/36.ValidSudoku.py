'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
'''


from typing import List


class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    if len(board) != 9 or len(board[0]) != 9:
      return False
    
    store = set()
    
    # check rows
    for r in range(9):
      store.clear()
      for c in range(9):
        if board[r][c] == '.':
          continue
          
        if board[r][c] in store:
          # print(0, r, c)
          return False
        
        store.add(board[r][c])
        
    for c in range(9):
      store.clear()
      for r in range(9):
        if board[r][c] == '.':
          continue
          
        if board[r][c] in store:
          # print(1, r, c)
          return False
        
        store.add(board[r][c])

    base = [0, 3, 6, 9]
    for i in range(3):
      r0, r1 = base[i], base[i+1]
      for j in range(3):
        c0, c1 = base[j], base[j+1]
        
        # print(r0, r1, c0, c1)
        store.clear()
        
        for r in range(r0, r1):
          for c in range(c0, c1):
            if board[r][c] == '.':
              continue
              
            if board[r][c] in store:
              # print(2, r, c)
              return False
            
            store.add(board[r][c])
    
    return True
  

  def isValidSudoku(self, board: List[List[str]]) -> bool:
    blocks = [set() for _ in range(9)]
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    o0 = ord('0')
    
    def get_block_num(i: int, j: int) -> int:
      r = i // 3
      c = j // 3
      
      return r*3 + c
    
    for i in range(9):
      for j in range(9):
        if board[i][j] == '.':
          continue
          
        val = ord(board[i][j]) - o0
        b = get_block_num(i, j)
        
        if val in rows[i] or val in cols[j] or val in blocks[b]:
          return False
        
        rows[i].add(val)
        cols[j].add(val)
        blocks[b].add(val)
        
    return True
    