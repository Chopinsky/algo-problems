'''
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8

Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6

Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
'''

from typing import List, Dict

class Solution:
  '''
  The idea is to build a graph between points of interests -- locks, keys, etc.
  Then we traverse between these points of interests to find the solution.

  Must optimize the iterations: 1) if we've the same key at the same point, but
  with more steps, we're not going to do better, skip; 2) if we an answer has
  already been found, and we take more steps to get here, skip; 3) if we're at
  a key that we already have (i.e. circled back), skip.
  '''
  def shortestPathAllKeys(self, grid: List[str]) -> int:
    h, w = len(grid), len(grid[0])
    m = {}
    d = {}
    dirs = [-1, 0, 1, 0, -1]
    key_count = 0

    for i, r in enumerate(grid):
      for j, c in enumerate(r):
        if c != '.' and c != '#':
          m[c] = (i, j)

          if c <= 'z' and c >= 'a':
            key_count += 1

    if key_count == 0:
      return 0

    key_target = (1 << key_count) - 1

    def calc_dist(key, coord) -> Dict[str, int]:
      steps = 1
      stack = [coord]
      temp = []
      seen = set(stack)
      ans = {}

      while len(stack) > 0:
        for (x, y) in stack:
          for i in range(4):
            x0, y0 = x+dirs[i], y+dirs[i+1]
            if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w or grid[x0][y0] == '#':
              continue

            if (x0, y0) in seen:
              continue

            cell = grid[x0][y0]
            seen.add((x0, y0))

            # print(key, cell)

            if cell != key and cell != '.':
              ans[cell] = steps

            if cell <= 'Z' and cell >= 'A':
              continue

            temp.append((x0, y0))
            seen.add((x0, y0))

        steps += 1
        stack, temp = temp, stack
        temp.clear()

      return ans

    for k, v in m.items():
      d[k] = calc_dist(k, v)

    # print(d)

    stack = [(0, '@', 0)]
    temp = []
    ans = -1
    key_steps = {}

    while len(stack) > 0:
      for (steps, pos, key) in stack:
        if pos not in d or len(d[pos]) == 0:
          continue

        for np, step in d[pos].items():
          # no need to get back to the start
          if np == '@':
            continue

          # met a lock, but don't have the key
          if np <= 'Z' and np >= 'A':
            offset = ord(np) - ord('A')
            if (1 << offset) & key == 0:
              continue

          curr_key = key
          curr_step = steps + step
          if ans >= 0 and curr_step >= ans:
            continue

          # check if we encounter a new key, it's not yet in the key chain
          if np <= 'z' and np >= 'a':
            offset = ord(np) - ord('a')
            if curr_key & (1 << offset) > 0:
              continue

            curr_key |= 1 << offset

          # already got all keys, done
          if curr_key == key_target:
            if ans < 0 or curr_step < ans:
              ans = curr_step

            continue

          # rounding around, not getting better answers from here
          kk = np + str(curr_key)
          if (kk in key_steps) and curr_step >= key_steps[kk]:
            continue

          # set the current position as the next round iterations
          key_steps[kk] = curr_step
          temp.append((curr_step, np, curr_key))

      stack, temp = temp, stack
      temp.clear()

    return ans
