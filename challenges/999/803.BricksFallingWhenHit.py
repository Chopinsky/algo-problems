'''
You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

It is directly connected to the top of the grid, or
At least one other brick in its four adjacent cells is stable.
You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

 

Example 1:

Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
Output: [2]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,1,0]]
We erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,1,1,0]]
The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
[[1,0,0,0],
 [0,0,0,0]]
Hence the result is [2].
Example 2:

Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
Output: [0,0]
Explanation: Starting with the grid:
[[1,0,0,0],
 [1,1,0,0]]
We erase the underlined brick at (1,1), resulting in the grid:
[[1,0,0,0],
 [1,0,0,0]]
All remaining bricks are still stable, so no bricks fall. The grid remains the same:
[[1,0,0,0],
 [1,0,0,0]]
Next, we erase the underlined brick at (1,0), resulting in the grid:
[[1,0,0,0],
 [0,0,0,0]]
Once again, all remaining bricks are still stable, so no bricks fall.
Hence the result is [0,0].

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is 0 or 1.
1 <= hits.length <= 4 * 104
hits[i].length == 2
0 <= xi <= m - 1
0 <= yi <= n - 1
All (xi, yi) are unique.
'''


from collections import defaultdict


class Solution:
  '''
  the idea is to treat brick hits as a reverse factor -- instead of making bricks 
  fall, we look backwards (i.e. from the end) and making bricks sticking together,
  merging isolating and "falling" groups into stable groups, updating the counters,
  and return the numbers of bricks becoming stable with the "glue/hit" brick.
  '''
  def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
    # removing hit bricks, make them the glues instead, note we shall skip
    # the hit brick if it appears later in the array, as it's no-op
    for i, [x, y] in enumerate(hits):
      if not grid[x][y]:
        hits[i] = None
      else:
        grid[x][y] = 0
      
    m, n = len(grid), len(grid[0])
    keys = [i for i in range(m*n)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def to_key(x: int, y: int) -> int:
      return x*n + y
    
    def find(k: int) -> int:
      while k != keys[k]:
        k = keys[k]  
      
      return k
    
    def union(a: int, b: int) -> int:
      ai, bi = find(a), find(b)
      if ai <= bi:
        keys[bi] = ai
        return ai
      
      keys[ai] = bi
      return bi
    
    # forming local groups withou the glue bricks
    for x in range(m):
      for y in range(n):
        if not grid[x][y]:
          continue
          
        k = to_key(x, y)
        for dx, dy in dirs:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or not grid[x0][y0]:
            continue
            
          k0 = find(to_key(x0, y0))
          union(k, k0)
            
    # keep counts of how many bricks are in each group
    group_count = defaultdict(int)
    for x in range(m):
      for y in range(n):
        if not grid[x][y]:
          continue
          
        root = find(to_key(x, y))
        group_count[root] += 1
        
    # print(group_count, keys)
    ans = [0] * len(hits)
    
    # iterate from the back of the hit bricks, adding them back as if
    # they are glues that bring up to 4 previously isolated groups together,
    # and count the bricks in the groups that are unstable previously, that's 
    # the amount of the bricks will fall without the glue brick
    for i in range(len(hits)-1, -1, -1):
      # a later hit, bricks have already fallen, skip
      if not hits[i]:
        continue
        
      x, y = hits[i]
      k = to_key(x, y)
      
      # the brick has already been patched up, skip
      if grid[x][y]:
        continue
      
      grid[x][y] = 1
      top = set()
      fallen = set()
      count = 0
      group_total = 1
      
      # this is a top brick
      if k < n:
        top.add(k)
        
      # this is a glue brick
      else:
        fallen.add(k)
      
      # look around and connect groups
      for dx, dy in dirs:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or not grid[x0][y0]:
          continue
          
        k0 = find(to_key(x0, y0))
        if k0 < n:
          top.add(k0)
        elif k0 not in fallen:
          fallen.add(k0)
          count += group_count[k0]
      
      # this brick will connect the group to the top, update the counters
      if top:
        ans[i] = count 
        root = min(top)
        
        for t in top:
          if t != root:
            group_total += group_count.pop(t, 0)
            union(root, t)
            
        for f in fallen:
          group_total += group_count.pop(f, 0)
          union(root, f)
          
      # this brick won't connect the group to the top, not going to work
      else:
        root = min(fallen)
        
        for f in fallen:
          group_total += group_count.pop(f, 0)
          union(root, f)
          
      group_count[root] = group_total
      # print(top, fallen, root, count, group_total, group_count, keys)
      # print(grid)
    
    return ans
  
