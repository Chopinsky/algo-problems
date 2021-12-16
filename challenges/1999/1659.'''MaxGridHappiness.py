'''
You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts. There are introvertsCount introverts and extrovertsCount extroverts.

You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you do not have to have all the people living in the grid.

The happiness of each person is calculated as follows:

Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.

Example 1:

Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
Output: 240
Explanation: Assume the grid is 1-indexed with coordinates (row, column).
We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
- Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
- Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
- Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
The grid happiness is 120 + 60 + 60 = 240.
The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.

Example 2:

Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
Output: 260
Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
- Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
- Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
- Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
The grid happiness is 90 + 80 + 90 = 260.

Example 3:

Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
Output: 240

Constraints:

1 <= m, n <= 5
0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
'''


from functools import lru_cache
from collections import defaultdict


class Solution:
  '''
  the  trick is that we only care about the last `n` cells, and we only keep the states of 
  (last_n_cell_state, intro_count, extro_count)
  '''
  # bottom-up
  def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
    if m > n:
      m, n = n, m
      
    @lru_cache(None)
    def test(i, intro, extro, prevRow):
      if i == m*n or (not intro and not extro):
        return 0

      # get (u, v) coord of the cell
      u, v = divmod(i, n)

      # if not assign a person at this cell (u, v)
      best_score = test(i+1, intro, extro, prevRow[1:] + (0, ))
      
      # set the upper and left neighbors for easier iteration
      neighbors = [prevRow[0] if u else -1, prevRow[-1] if v else -1]

      # if assign an intro person to this cell
      if intro:
        score = 120 + sum(lookup[(1, nei)] for nei in neighbors if nei > 0)
        best_score = max(
          best_score, 
          score + test(i+1, intro-1, extro, prevRow[1:] + (1, ))
        )

      # if assign an extro person to this cell
      if extro:
        score = 40 + sum(lookup[(2, nei)] for nei in neighbors if nei > 0)
        best_score = max(
          best_score, 
          score + test(i+1, intro, extro-1, prevRow[1:] + (2, ))
        )

      return best_score

    #1:introvert, 2: extrovert, 0: no neighbor
    lookup = { 
      (1, 1): -30-30, 
      (1, 2): -30+20, 
      (2, 1): 20-30, 
      (2, 2): 20+20, 
    }

    return test(0, introvertsCount, extrovertsCount, tuple([0] * n))

  # top-down
  def getMaxGridHappiness0(self, m: int, n: int, intro: int, extro: int) -> int:
    if m > n:
      m, n = n, m
      
    if not intro and not extro:
      return 0
    
    if m == 1 and n == 1:
      if intro:
        return 120
      
      return 40 if extro else 0
    
    curr, nxt = defaultdict(dict), defaultdict(dict)
    mask = (1 << n) - 1
    best_score = 0
    
    # populate the init states
    for i in range(n):
      if i == 0:
        curr['_'] = { (intro, extro): 0, }

        if intro > 0:
          curr['i'] = { (intro-1, extro): 120, }
          best_score = 120

        if extro > 0:
          curr['e'] = { (intro, extro-1): 40, } 
          best_score = max(best_score, 40)

        continue

      for state in curr:
        for (ic, ec), val in curr[state].items():
          if not ic and not ec:
            continue
            
          # if i-th column is empty
          nxt_state = state + '_'
          nxt[nxt_state][ic, ec] = max(nxt[nxt_state].get((ic, ec), 0), val)
          best_score = max(best_score, nxt[nxt_state][ic, ec])
          
            # if i-th column is an introvert
          if ic > 0:
            nxt_state = state + 'i'
            
            if state[-1] != '_':
              # the last cell has a person 
              nxt_val = val + 90 + (-30 if state[-1] == 'i' else 20)
            else:
              # the last cell doesn't have a person 
              nxt_val = val + 120
              
            nxt[nxt_state][ic-1, ec] = max(nxt[nxt_state].get((ic-1, ec), 0), nxt_val)
            best_score = max(best_score, nxt[nxt_state][ic-1, ec])
            
          # if this person is an extrovert
          if ec > 0:
            nxt_state = state + 'e'
            
            if state[-1] != '_':
              # the last cell has a person 
              nxt_val = val + 60 + (-30 if state[-1] == 'i' else 20)
            else:
              # the last cell doesn't have a person 
              nxt_val = val + 40
              
            nxt[nxt_state][ic, ec-1] = max(nxt[nxt_state].get((ic, ec-1), 0), nxt_val)
            best_score = max(best_score, nxt[nxt_state][ic, ec-1])
            
      curr, nxt = nxt, curr
      nxt.clear()
      
    # print(curr)
    
    for _ in range(1, m):
      for i in range(n):
        for state in curr:
          for (ic, ec), val in curr[state].items():
            # no more people to put on the board
            if not ic and not ec:
              continue
              
            nxt_state = state[1:] + '_'
            nxt[nxt_state][ic, ec] = max(nxt[nxt_state].get((ic, ec), 0), val)
            best_score = max(best_score, nxt[nxt_state][ic, ec])
            
            # if an intro person is placed here
            if ic > 0:
              nxt_state = state[1:] + 'i'
              offset = 0 if state[0] == '_' else -30
              
              # person above
              if state[0] == 'i':
                offset += -30
              elif state[0] == 'e':
                offset += 20
                
              # person to the left
              if i > 0 and state[-1] != '_':
                offset += -30 # from the person
                offset += -30 if state[-1] == 'i' else 20 # from  person-to-the left
                
              nxt_val = val + 120 + offset
              nxt[nxt_state][ic-1, ec] = max(nxt[nxt_state].get((ic-1, ec), 0), nxt_val)
              best_score = max(best_score, nxt[nxt_state][ic-1, ec])
              
            if ec > 0:
              nxt_state = state[1:] + 'e'
              offset = 0 if state[0] == '_' else 20
              
              if state[0] == 'i':
                offset += -30
              elif state[0] == 'e':
                offset += 20
                
              if i > 0 and state[-1] != '_':
                offset += 20
                offset += -30 if state[-1] == 'i' else 20
                
              nxt_val = val + 40 + offset
              nxt[nxt_state][ic, ec-1] = max(nxt[nxt_state].get((ic, ec-1), 0), nxt_val)
              best_score = max(best_score, nxt[nxt_state][ic, ec-1])
          
        curr, nxt = nxt, curr
        nxt.clear()
    
    return best_score
        