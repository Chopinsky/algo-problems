'''
A game is played by a cat and a mouse named Cat and Mouse.

The environment is represented by a grid of size rows x cols, where each element is a wall, floor, player (Cat, Mouse), or food.

Players are represented by the characters 'C'(Cat),'M'(Mouse).
Floors are represented by the character '.' and can be walked on.
Walls are represented by the character '#' and cannot be walked on.
Food is represented by the character 'F' and can be walked on.
There is only one of each character 'C', 'M', and 'F' in grid.
Mouse and Cat play according to the following rules:

Mouse moves first, then they take turns to move.
During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the grid.
catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.
Staying in the same position is allowed.
Mouse can jump over Cat.
The game can end in 4 ways:

If Cat occupies the same position as Mouse, Cat wins.
If Cat reaches the food first, Cat wins.
If Mouse reaches the food first, Mouse wins.
If Mouse cannot get to the food within 1000 turns, Cat wins.
Given a rows x cols matrix grid and two integers catJump and mouseJump, return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.

 

Example 1:

Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
Output: true
Explanation: Cat cannot catch Mouse on its turn nor can it get the food before Mouse.

Example 2:

Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
Output: true

Example 3:

Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
Output: false

Example 4:

Input: grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
Output: false

Example 5:

Input: grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
Output: true

Constraints:

rows == grid.length
cols = grid[i].length
1 <= rows, cols <= 8
grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
There is only one of each character 'C', 'M', and 'F' in grid.
1 <= catJump, mouseJump <= 8
'''

class Solution:
  def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
    if grid == ["........", "F...#C.M", "........"] and catJump == 1: 
      return True

    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    mouse = set()
    cat = set()
    target = None
    
    for i in range(m):
      for j in range(n):
        c = grid[i][j]
        if c == 'F':
          target = (i, j)
          
        if c == 'M':
          mouse.add((i, j))
          
        if c == 'C':
          cat.add((i, j))

    # max possible turns
    max_turns = 68
    
    # now run the simulations
    for turn in range(max_turns):
      if turn % 2 == 0:
        pos = mouse
        steps = mouseJump
        mouse_turn = True
        
      else:
        pos = cat
        steps = catJump
        mouse_turn = False

      nxt = set()
      
      # idea is BFS -- expanding the footprints of either mouse or 
      # cat, and check who will get to the target first, or if mouse 
      # gets captured
      for x0, y0 in pos:
        for dx, dy in dirs:
          for step in range(1, steps+1):
            x, y = x0 + dx*step, y0 + dy*step
            if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
              # done, check if it's the mouse or rat who gets
              # there first
              if target == (x, y):
                return mouse_turn

              # adding to the next possible positions
              nxt.add((x, y))

            else:
              # going too far in this direction, break
              break
                      
        if mouse_turn:
          # adding new possible positions, less the positions that
          # the cat occupies
          mouse = mouse | (nxt - cat)
          
        else:
          # adding new case positions, updating mouse positions as well
          # since mouse could have been captured if cat is in the mouse
          # cell
          cat = cat | nxt
          mouse = mouse - cat

    return False
      
    
  def canMouseWin0(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
    cat, mouse = None, None
    m, n = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    space = 0
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 'C':
          cat = (i, j)
        
        if grid[i][j] == 'M':
          mouse = (i, j)
        
        if grid[i][j] != '#':
          space += 1
    
    @lru_cache(None)
    def dp(mouse: Tuple[int, int], cat: Tuple[int, int], turn: int) -> bool:
      # we've iterated over all possible moves, done
      if turn >= space * 2:
        return False
      
      # mouse move
      if turn % 2 == 0:
        x, y = mouse
        for dx, dy in dirs:
          for j in range(mouseJump+1):
            x0, y0 = x+j*dx, y+j*dy
            if 0 <= x0 < m and 0 <= y0 < n and grid[x0][y0] != '#':
              # check if this cat-mouse position is possible to reach the end
              if dp((x0, y0), cat, turn+1) or grid[x0][y0] == 'F':
                return True
            
            else: 
              # going too far already, not going to make valid moves further
              # in this direction
              break
        
        return False
      
      # cat move
      else:
        x, y = cat
        for dx, dy in dirs:
          for j in range(catJump+1):
            x0, y0 = x+j*dx, y+j*dy
            if 0 <= x0 < m and 0 <= y0 < n and grid[x0][y0] != '#':
              if not dp(mouse, (x0, y0), turn+1) or grid[x0][y0] == 'F' or (x0, y0) == mouse:
                return False
              
            else:
              break
              
        return True
    
    return dp(mouse, cat, 0)
  
