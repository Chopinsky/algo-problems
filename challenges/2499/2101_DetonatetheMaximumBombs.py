'''
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Example 1:

Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:

Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
Example 3:

Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.

Constraints:

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 10^5
'''

from typing import List
from collections import defaultdict
from math import sqrt


class Solution:
  def maximumDetonation(self, bombs: List[List[int]]) -> int:
    g = defaultdict(set)
    n = len(bombs)
    
    for i in range(n):
      x, y, r = bombs[i]
      
      for j in range(n):
        if i == j:
          continue
          
        x0, y0, _ = bombs[j]
        d = sqrt((x-x0)**2 + (y-y0)**2)
        
        if d <= r:
          g[i].add(j)
          
    # print(g)
    seen = set()
    count = 1
    
    def dfs(i: int) -> int:
      if i in seen:
        return 0
      
      seen.add(i)
      for j in g[i]:
        dfs(j)
      
    for i in range(n):
      seen.clear()
      dfs(i)
      count = max(count, len(seen))
      # print(i, seen)
    
    return count
        

  def maximumDetonation(self, bombs: List[List[int]]) -> int:
    n = len(bombs)
    seen = set()
    max_count = 1
    g = defaultdict(list)

    for i in range(n-1):
      for j in range(i+1, n):
        x0, y0, d0 = bombs[i]
        x1, y1, d1 = bombs[j]
        dist = (x0-x1)**2 + (y0-y1)**2
        
        if dist <= d0*d0:
          g[i].append(j)
          
        if dist <= d1*d1:
          g[j].append(i)
        
    # print(g)
    
    def detonate(i):
      nonlocal seen
      
      count = 1
      if i in seen:
        return count
      
      stack, nxt = [i], []
      visited = set(stack)
      
      while stack:
        for u in stack:
          for v in g[u]:
            if v in visited:
              continue
              
            nxt.append(v)
            visited.add(v)
            count += 1
        
        stack, nxt = nxt, stack
        nxt.clear()
      
      seen |= visited
      return count
    
    for i in range(n):
      max_count = max(max_count, detonate(i))
      
    return max_count
      