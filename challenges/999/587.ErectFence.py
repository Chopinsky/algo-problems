'''
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

Example 1:

Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:

Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]

Constraints:

1 <= points.length <= 3000
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.
'''


from typing import List
from collections import defaultdict


class Solution:
  def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
    bounds = {}
    dots = defaultdict(list)
    l, r = 101, 0
    t, b = 0, 101
    
    for c in trees:
      x, y = c[0], c[1]
      dots[x].append(c)
      
      if x not in bounds:
        bounds[x] = [y, y]
      else:
        bounds[x][0] = min(bounds[x][0], y)
        bounds[x][1] = max(bounds[x][1], y)
            
      t = max(t, y)
      b = min(b, y)
      l = min(l, x)
      r = max(r, x)
        
    # print(l, r, t, b)
    base = set()
    high = []
    low = []
    
    def calc(a: List[int], b: List[int]) -> float:
      return (b[1] - a[1]) / (b[0] - a[0])
    
    for x in sorted(bounds.keys()):
      # print(x, bounds[x], dots[x])
      
      # update high lines
      coord = [x, bounds[x][1]]
      while len(high) > 1:
        src = calc(high[-2], high[-1])
        curr = calc(high[-2], coord)
        if src >= curr:
          break
          
        high.pop()

      high.append(coord)
        
      # update low lines
      coord = [x, bounds[x][0]]
      while len(low) > 1: 
        src = calc(low[-2], low[-1])
        curr = calc(low[-2], coord)
        if src <= curr:
          break
          
        low.pop()
      
      low.append(coord)
      
    for x, y in high+low+dots[l]+dots[r]:
      base.add((x, y))
    
    ans = []
    for x, y in base:
      ans.append([x, y])
    
    return ans
  