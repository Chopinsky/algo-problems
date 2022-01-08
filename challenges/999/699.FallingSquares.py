'''
There are several squares being dropped onto the X-axis of a 2D plane.

You are given a 2D integer array positions where positions[i] = [lefti, sideLengthi] represents the ith square with a side length of sideLengthi that is dropped with its left edge aligned with X-coordinate lefti.

Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands on the top side of another square or on the X-axis. A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved.

After each square is dropped, you must record the height of the current tallest stack of squares.

Return an integer array ans where ans[i] represents the height described above after dropping the ith square.

Example 1:

Input: positions = [[1,2],[2,3],[6,1]]
Output: [2,5,5]
Explanation:
After the first drop, the tallest stack is square 1 with a height of 2.
After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
Thus, we return an answer of [2, 5, 5].

Example 2:

Input: positions = [[100,100],[200,100]]
Output: [100,100]
Explanation:
After the first drop, the tallest stack is square 1 with a height of 100.
After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
Thus, we return an answer of [100, 100].
Note that square 2 only brushes the right side of square 1, which does not count as landing on it.
 

Constraints:

1 <= positions.length <= 1000
1 <= lefti <= 10^8
1 <= sideLengthi <= 10^6
'''


import math
from typing import List
from bisect import bisect_right


class Solution:
  def fallingSquares(self, positions: List[List[int]]) -> List[int]:
    blocks = []
    heights = [pos[1] for pos in positions]
    ans = []
    tall = 0
    
    for i, [left, side] in enumerate(positions):
      high, right = 0, left+side
      if not blocks or right <= blocks[0][0] or left >= blocks[-1][0]:
        if right <= blocks[0][0]:
          blocks = [(left, i), (right, i)] + blocks
        else:
          blocks.append((left, i))
          blocks.append((right, i))
          
        tall = max(tall, side)
        ans.append(tall)
        continue
        
      start = bisect_right(blocks, (left, math.inf))
      before = blocks[:start]
      after = []
      # print('start:', i, (left, side), start, before)

      # the previous section is open but not closed, add
      # the close to it
      if len(before) % 2 == 1:
        high = max(high, heights[before[-1][1]])
        if before[-1][0] == left:
          # complete under
          before.pop()
          start -= 1
        else:
          # partially under, add the ending to it
          before.append((left, before[-1][1]))
            
      for j in range(start, len(blocks)):
        if blocks[j][0] >= right:
          after = blocks[j:]
          break
        
        high = max(high, heights[blocks[j][1]])
        
      # the next section is closed but not opened, add an open to it
      if len(after) % 2 == 1:
        high = max(high, heights[after[0][1]])
        if after[0][0] == right:
          # completely under
          after = after[1:]
        else:
          # partially under, add the start to it
          after = [(right, after[0][1])] + after
        
      blocks = before + [(left, i), (right, i)] + after
      heights[i] = high + side
      tall = max(tall, heights[i])
      ans.append(tall)
      # print('end', blocks, heights)
      
    # print('fin', blocks, heights)
    return ans
