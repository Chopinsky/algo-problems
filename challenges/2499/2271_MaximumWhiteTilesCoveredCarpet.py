'''
You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.

Example 1:


Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
Output: 9
Explanation: Place the carpet starting on tile 10. 
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.
Example 2:

Input: tiles = [[10,11],[1,1]], carpetLen = 2
Output: 2
Explanation: Place the carpet starting on tile 10. 
It covers 2 white tiles, so we return 2.
 

Constraints:

1 <= tiles.length <= 5 * 10^4
tiles[i].length == 2
1 <= li <= ri <= 10^9
1 <= carpetLen <= 10^9
The tiles are non-overlapping.
'''

from typing import List
from bisect import bisect_right


class Solution:
  def maximumWhiteTiles(self, tiles: List[List[int]], carpet_len: int) -> int:
    tiles.sort()
    t = []
    
    for l, r in tiles:
      if t and l-1 <= t[-1][1]:
        t[-1][1] = r
      else:
        t.append([l, r])
        
    # print(t)
    start, prefix = [], []
    covered = 0
    
    for l, r in t:
      prefix.append((r-l+1) + (prefix[-1] if prefix else 0))
      start.append(l)
      
      if r-l+1 >= carpet_len:
        covered = carpet_len
        break
      
      l0 = r - carpet_len + 1
      if start and l0 > 0 and l0 > start[0]:
        idx = bisect_right(start, l0) - 1
        r0 = t[idx][1]
        cnt = (prefix[-1]-prefix[idx]) + (r0-l0+1 if r0 >= l0 else 0)
        
        # print(l, r, idx, l0, r0, prefix, cnt)
        covered = max(covered, cnt)

      else:
        covered = max(covered, prefix[-1])
    
    return covered
  