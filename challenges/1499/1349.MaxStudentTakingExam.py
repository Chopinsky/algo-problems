'''
Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.

Example 1:

Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 

Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats. 

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.

Constraints:

seats contains only characters '.' and'#'.
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8
'''


from typing import List, Dict
from collections import defaultdict


class Solution:
  def maxStudents(self, seats: List[List[str]]) -> int:
    m, n = len(seats), len(seats[0])
    
    #todo: optimize out the needs of the `list` as the intermediate data
    #      structure, just use the `dict` for `curr` and `last`
    def place_student(last_row: int, base_cnt: int, allowed: List[int], settings: Dict[int, int]):
      curr_row = [(0, base_cnt)]
      settings[0] = max(settings[0], base_cnt)
      
      for i in allowed:
        nxt = []
        for mask, cnt in curr_row:
          idx = 1 << i
          
          # student can cheat at this position
          if (mask<<1) & idx > 0:
            continue

          if last_row >= 0 and ((last_row<<1 & idx) > 0 or (last_row>>1 & idx) > 0):
            continue
            
          nxt_mask = mask | idx
          nxt.append((nxt_mask, cnt+1))
          settings[nxt_mask] = max(settings[nxt_mask], cnt+1)
      
        curr_row.extend(nxt)

    allowed = [i for i in range(n) if seats[0][i] == '.']
    settings = defaultdict(int)

    place_student(-1, 0, allowed, settings)
    curr, last = [], []

    for mask, cnt in settings.items():
      last.append((mask, cnt))

    # print(allowed, last)
    if m == 1:
      return max(last, key=lambda x: x[1])[1]
    
    for row in seats[1:]:
      settings = defaultdict(int)
      allowed = [i for i in range(n) if row[i] == '.']
      
      if not allowed:
        max_last_cnt = max(last, key=lambda x: x[1])[1]
        last = [(0, max_last_cnt)]
        continue
      
      for mask, cnt in last:
        place_student(mask, cnt, allowed, settings)
      
      for mask, cnt in settings.items():
        curr.append((mask, cnt))
      
      # print(row, curr)
      last, curr = curr, last
      curr.clear()
      
    # print('done', last)
    return max(last, key=lambda x: x[1])[1]
        