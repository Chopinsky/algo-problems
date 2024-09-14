'''
3288. Length of the Longest Increasing Path

Test cases:
[[3,1],[2,2],[4,1],[0,0],[5,3]]
1
[[2,1],[7,0],[5,6]]
2
[[5,0],[9,3],[9,8]]
0
[[313980967,13888427],[473620925,693757796],[407503949,713002778],[833031297,798864094],[672541157,478829491],[885972706,982962973],[547347833,726188327],[975269668,853554872],[393978782,293882769],[506907326,462657319],[114562239,221757642]]
1
'''

from typing import List
from collections import defaultdict

class Solution:
  '''
  use sweep-line as the out-most loop, where we check each (x, y) in a sorted manner
  and (x < point_x and y < point_y) or (x > point_x and y > point_y); for each point
  use a segment tree to store the max path length if the path ended at (y0 < y), and
  we can extend the max path with this (x, y) by adding length by 1; then the final
  answer is the max path length to the left plus the max path length to the right of
  the point (point_x, point_y)
  '''
  def maxPathLength(self, coord: List[List[int]], k: int) -> int:
    x, y = coord[k]
    coord.sort()
    left = defaultdict(list)
    right = defaultdict(list)
    
    for x0, y0 in coord:
      if x0 < x and y0 < y:
        left[x0].append(y0)
        
      if x0 > x and y0 > y:
        right[x0].append(y0)
    
    # print('init:', left, right)
    tree = [None]*30*len(coord)
    ptr = 0
    
    def update(node: List, idx: int, val: int):
      nonlocal ptr
      
      # print('update:', node, idx, val)
      l, r, _, ldx, rdx = node
      if idx < l or idx > r:
        return
      
      node[2] = max(node[2], val)
      if l == r:
        return
      
      mid = (l + r) // 2
      if idx <= mid:
        if ldx < 0:
          tree[ptr] = [l, mid, 0, -1, -1]
          ldx = ptr
          node[3] = ptr
          ptr += 1

        child = tree[ldx]
        
      else:
        if rdx < 0:
          tree[ptr] = [mid+1, r, 0, -1, -1]
          rdx = ptr
          node[4] = ptr
          ptr += 1
          
        child = tree[rdx]
        
      update(child, idx, val)
    
    def query(node: List, idx: int) -> int:
      l, r, val, ldx, rdx = node
      if r < idx:
        return val
      
      if l == r or idx <= l:
        return 0
      
      mid = (l + r) // 2
      ll = query(tree[ldx], idx) if ldx >= 0 else 0
      rr = query(tree[rdx], idx) if rdx >= 0 and idx > mid+1 else 0
        
      return max(ll, rr)
    
    def calc(src):
      nonlocal ptr
      
      if not src:
        return 0
      
      long = 1
      rng = max([max(row) for row in src.values()])
      tree[0] = [0, rng, 0, -1, -1]
      ptr += 1
      nxt = []
      
      for x0 in sorted(src):
        nxt.clear()  
        for y0 in src[x0]:
          ln = query(tree[0], y0)
          long = max(long, 1+ln)
          nxt.append((y0, 1+ln))
        
        for y0, ln in nxt:
          update(tree[0], y0, ln)
      
      return long
    
    left_long = calc(left)
    right_long = calc(right)
    
    return left_long + right_long + 1
        