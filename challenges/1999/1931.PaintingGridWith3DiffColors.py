'''
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.

Example 2:

Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.

Example 3:

Input: m = 5, n = 5
Output: 580986

Constraints:

1 <= m <= 5
1 <= n <= 1000
'''


from collections import defaultdict
from functools import lru_cache
from typing import Dict


class Solution:
  def colorTheGrid(self, m: int, n: int) -> int:
    mod = 1_000_000_007
    colors, nxt = defaultdict(int), defaultdict(int)
    colors[' ' * m] = 1
    
    @lru_cache(None)
    def build(last: str, curr: str) -> Dict:
      idx = len(curr)
      res = defaultdict(int)
      
      for ch in ['r', 'g', 'b']:
        if last[idx] == ch or (curr and curr[-1] == ch):
          continue

        if idx == m-1:
          res[ch] = 1
          continue
          
        nxt = build(last, curr+ch)
        for row in nxt:
          res[ch+row] += nxt[row]
            
      return res
    
    for i in range(n):
      for last_row, cnt in colors.items():
        rows = build(last_row, '')
        for r, cnt0 in rows.items():
          nxt[r] = (nxt[r] + cnt * cnt0) % mod
        
      colors, nxt = nxt, colors
      nxt.clear()
        
    return sum(colors.values()) % mod
  