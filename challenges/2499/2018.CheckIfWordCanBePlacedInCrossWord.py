'''
You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.

A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:

It does not occupy a cell containing the character '#'.
The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.

Example 1:

Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
Output: true
Explanation: The word "abc" can be placed as shown above (top to bottom).

Example 2:

Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
Output: false
Explanation: It is impossible to place the word because there will always be a space/letter above or below it.

Example 3:

Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
Output: true
Explanation: The word "ca" can be placed as shown above (right to left). 
 

Constraints:

m == board.length
n == board[i].length
1 <= m * n <= 2 * 10^5
board[i][j] will be ' ', '#', or a lowercase English letter.
1 <= word.length <= max(m, n)
word will contain only lowercase English letters.
'''


from typing import List


class Solution:
  def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
    size = len(word)
    m, n = len(board), len(board[0])
    v_seen = set()
    h_seen = set()
      
    def check(i: int, j: int, v: bool) -> bool:
      nonlocal m, n, size
      
      if v:
        v_seen.add((i, j))
      else:
        h_seen.add((i, j))
      
      os = (1, 0) if v else (0, 1)
      si, sj = i, j
      ei, ej = i, j
      l, r = 0, 0      
      
      while si >= 0 and sj >= 0 and board[si][sj] != '#':
        if v:
          v_seen.add((si, sj))
        else:
          h_seen.add((si, sj))
          
        si -= os[0]
        sj -= os[1]
        l += 1
      
      while ei < m and ej < n and board[ei][ej] != '#':
        if v:
          v_seen.add((ei, ej))
        else:
          h_seen.add((ei, ej))
          
        ei += os[0]
        ej += os[1]
        r += 1
        
      # print(i, j, v, l, r)
        
      if l+r-1 != size:
        return False
          
      order = True
      rev_order = True
        
      si += os[0]
      sj += os[1]
      ei -= os[0]
      ej -= os[1]
      
      # print(i, j, (si, sj), (ei, ej))
      
      for k in range(size):
        if order:
          x, y = (si+k, j) if v else (i, sj+k)
          order = board[x][y] == ' ' or board[x][y] == word[k]
          
        if rev_order:
          x, y = (ei-k, j) if v else (i, ej-k)
          rev_order = board[x][y] == ' ' or board[x][y] == word[k]
      
        if not order and not rev_order:
          break
      
      return order or rev_order
    
    for i in range(m):
      for j in range(n):
        if board[i][j] == '#':
          continue
          
        # check verticl
        if (i, j) not in v_seen and check(i, j, True):
          return True
        
        # check horizontal
        if (i, j) not in h_seen and check(i, j, False):
          return True
        
    return False
      