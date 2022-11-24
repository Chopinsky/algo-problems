'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''


from typing import List
from collections import Counter, defaultdict


class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    c = Counter(word)
    
    base = defaultdict(int)
    for x in range(m):
      for y in range(n):
        base[board[x][y]] += 1
        
    for ch, cnt in c.items():
      if cnt > base[ch]:
        return False
    
    k = len(word)
    seen = set()
    
    # @lru_cache(None)
    def search(x: int, y: int, i: int):
      if i >= k:
        return True
      
      if board[x][y] != word[i]:
        return False
      
      if i == k-1:
        return True
      
      seen.add((x, y))
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        xx, yy = x+dx, y+dy
        if xx < 0 or xx >= m or yy < 0 or yy >= n or (xx, yy) in seen:
          continue
          
        if search(xx, yy, i+1):
          return True
      
      seen.discard((x, y))
      return False
    
    for x in range(m):
      for y in range(n):
        if search(x, y, 0):
          return True
        
    return False
          

  def exist(self, board: List[List[str]], word: str) -> bool:
    seen = set()
    m, n = len(board), len(board[0])
    
    if m*n < len(word):
      return False
    
    c = Counter(word)
    d = defaultdict(int)
    
    for i in range(m):
      for j in range(n):
        d[board[i][j]] += 1
        
    for ch, cnt in c.items():
      if d[ch] < cnt:
        return False
    
    seen = set()
    size = len(word)
    
    def dfs(x: int, y: int, i: int) -> bool:
      if board[x][y] != word[i]:
        return False
      
      if i == size - 1:
        # print(seen, x, y, i, size)
        return True
      
      seen.add((x, y))
      for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or (x0, y0) in seen:
          continue
        
        if dfs(x0, y0, i+1):
          return True
        
      seen.discard((x, y))
      return False
    
    # print('checking:', word)
    for i in range(m):
      for j in range(n):
        # print('cell', i, j)
        seen.clear()
        
        if dfs(i, j, 0):
        # if check(i, j):
          return True
        
    return False