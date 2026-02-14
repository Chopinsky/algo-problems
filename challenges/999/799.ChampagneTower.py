'''
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

Example 1:

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
Example 2:

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
Example 3:

Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
 

Constraints:

0 <= poured <= 10^9
0 <= query_glass <= query_row < 100
'''

from typing import List


class Solution:
  def champagneTower(self, poured: int, r: int, c: int) -> float:
    def pour(curr: List) -> float:
      n = len(curr)
      if n-1 == r:
        return min(1.0, curr[c])

      nxt = [0.0]*(n+1)

      for i in range(n):
        # no spill
        if curr[i] <= 1.0:
          continue

        spill = (curr[i] - 1.0) / 2.0
        nxt[i] += spill
        nxt[i+1] += spill

      return pour(nxt)

    return pour([poured])
        
        
  def champagneTower(self, poured: int, r: int, c: int) -> float:
    if r == 0:
      return min(1, poured)
    
    curr = [poured]
    idx = 0
    
    while idx < r:
      idx += 1
      nxt = [0] * (idx+1)
      
      for i in range(idx):
        overflow = max(0, curr[i]-1) / 2.0
        nxt[i] += overflow
        nxt[i+1] += overflow
      
      curr = nxt
      
    return min(1, curr[c])
        
        
  def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    if not query_row:
      return poured if poured <= 1 else 1
      
    curr = [poured]
    row = 0
    
    while row < query_row:
      row += 1
      nxt_row = [0] * (row+1)
      overflow = False
      
      for i, vol in enumerate(curr):
        if vol > 1:
          nxt_row[i] += (vol-1) / 2.0
          nxt_row[i+1] += (vol-1) / 2.0
          overflow = True

      curr = nxt_row
      if row == query_row:
        return 1 if curr[query_glass] >= 1 else curr[query_glass]
      
      if not overflow:
        break
      
    return 0
      