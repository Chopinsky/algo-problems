'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''


from typing import List, Dict
from collections import defaultdict, Counter


class Trie:
  def __init__(self):
    self.is_word = False
    self.count = 0
    self.children = [None] * 26
    
  
  def add(self, word: str):
    curr = self
    idx = 0
    
    while idx < len(word):
      ch = ord(word[idx]) - ord('a')
      if not curr.children[ch]:
        curr.children[ch] = Trie()
        
      curr = curr.children[ch]
      curr.count += 1
      idx += 1
      
    curr.is_word = True
    
    
  def search(self, word: str) -> bool:
    curr = self
    idx = 0
    
    while idx < len(word):
      ch = ord(word[idx]) - ord('a')
      if not curr.children[ch]:
        return False
      
      curr = curr.children[ch]
      idx += 1
      
    return curr.is_word
  
  
  def remove(self, word: str):
    parent = None
    curr = self
    idx = 0
    
    while idx < len(word):
      ch = ord(word[idx]) - ord('a')
      if not curr.children[ch]:
        break
      
      parent = curr
      curr = curr.children[ch]
      curr.count -= 1
      
      if parent and not curr.count:
        parent.children[ch] = None
        break

  
  def next_node(self, ch: str):
    idx = ord(ch) - ord('a')
    return self.children[idx]


class Solution:
  def findWords(self, b: List[List[str]], words: List[str]) -> List[str]:
    m, n = len(b), len(b[0])
    chars = defaultdict(int)
    
    # create the char set to skip words that's not gonna happen
    for i in range(m):
      for j in range(n):
        chars[b[i][j]] += 1
        
    root = {}
    stop = '$'
    max_len = 0
    
    # build the in-place trie
    for w in words:
      c = Counter(w)
      for ch, cnt in c.items():
        if cnt > chars[ch]:
          continue
        
      curr = root
      for ch in w:
        if ch not in curr:
          curr[ch] = {}
          
        curr = curr[ch]
        
      # adding the 'stop' sign to indicate there's a word
      # ending at this node
      curr[stop] = stop
      max_len = max(max_len, len(w))
      
    # print(root)
    ans = []
    seen = [[False for _ in range(n)] for _ in range(m)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dp(x: int, y: int, w: str, node: Dict[str, any]):
      # there's a word to this node, mark it as seen and pop it
      if stop in node:
        ans.append(w)
        node.pop(stop, None)
        
      if seen[x][y] or len(w) >= max_len: 
        return
      
      seen[x][y] = True
      for dx, dy in dirs:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or seen[x0][y0]:
          continue
          
        ch = b[x0][y0]
        if ch not in node:
          continue
          
        dp(x0, y0, w+ch, node[ch])
        if not node[ch]:
          node.pop(ch, None)
      
      seen[x][y] = False
      return
    
    for i in range(m):
      for j in range(n):
        ch = b[i][j]
        if ch not in root:
          continue
          
        # print('start:', i, j, ch)
        dp(i, j, ch, root[ch])
        if not root[ch]:
          root.pop(ch, None)
        
    return ans
    
    
  def findWords0(self, board: List[List[str]], words: List[str]) -> List[str]:
    root = Trie()
    max_len = 0
    
    for w in words:
      if not w:
        continue
        
      root.add(w)
      max_len = max(max_len, len(w))
    
    m, n = len(board), len(board[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [[0, 0, ]]
    seen = [[False for _ in range(n)] for _ in range(m)]
    ans = set()
    
    def dp(x: int, y: int, w: str, node: Trie):
      if len(w) > max_len or not node or seen[x][y]:
        return
      
      seen[x][y] = True
      
      for i in range(4):
        x0, y0 = x+dirs[i][0], y+dirs[i][1]
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or seen[x0][y0]:
          continue
          
        ch = board[x0][y0]
        nxt = node.next_node(ch)
        
        if not nxt:
          continue
          
        dp(x0, y0, w+ch, nxt)
      
      seen[x][y] = False
      
      if node.is_word:
        ans.add(w)
        # root.remove(w)
        
      return
    
    for i in range(m):
      for j in range(n):
        node = root.next_node(board[i][j])
        if not node:
          continue
          
        dp(i, j, board[i][j], node)
    
    return list(ans)
  