'''
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.

Example 1:

Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.

Example 2:

Input: ring = "godding", key = "godding"
Output: 13

Constraints:

1 <= ring.length, key.length <= 100
ring and key consist of only lower case English letters.
It is guaranteed that key could always be spelled by rotating ring.
'''

from functools import lru_cache
from collections import defaultdict
from typing import Dict

class Solution:
  def findRotateSteps(self, ring: str, key: str) -> int:
    pos = defaultdict(list)
    n = len(ring)

    for i, ch in enumerate(ring):
      pos[ch].append(i)

    curr, nxt = {0:0}, {}
    # print(pos, curr)

    @lru_cache(None)
    def dist(f: int, t: int) -> int:
      return min(abs(f-t), abs(f+n-t), abs(t+n-f))

    def update(i: int, s: int, nxt_ch: str, nxt: Dict):
      for j in pos[ch]:
        nxt[j] = min(nxt.get(j, float('inf')), 1+s+dist(i, j))

    for ch in key:
      for i, s in curr.items():
        update(i, s, ch, nxt)

      curr, nxt = nxt, curr
      nxt.clear()
      # print(ch, curr)

    return min(curr.values())
        
  def findRotateSteps(self, ring: str, key: str) -> int:
    pos = defaultdict(list)
    for i, c in enumerate(ring):
      pos[c].append(i)
      
    dp = [(1, p) for p in pos[key[-1]]]
    nxt = []
    n = len(ring)
    # print(dp)
    
    for i in range(len(key)-2, -1, -1):
      for p0 in pos[key[i]]:
        dist = float('inf')
        
        # note: a speed up exists here -- instead of looping over all
        # points in dp, we actually cares about the p1 positions to the
        # left and right of p0, so we can replace the for-loop with a 
        # bisect_left, then determine the left and right positions; this
        # will reduce time complexity to `n^2 * ln(n)`
        for cnt, p1 in dp:
          if p0 == p1:
            dist = min(dist, cnt)
          else:
            l, r = min(p0, p1), max(p0, p1)
            dist = min(dist, cnt+r-l, cnt+n+l-r)
        
        # click char at p0, then rotate ring with `dist` 
        # steps to p1
        nxt.append((dist+1, p0))
        
      dp, nxt = nxt, dp
      nxt.clear()

    # print(dp)
    
    dist = float('inf')
    for cnt, p in dp:
      if p == 0:
        dist = min(dist, cnt)
      else:
        l, r = min(0, p), max(0, p)
        dist = min(dist, cnt+r-l, cnt+n+l-r)
    
    return dist
  