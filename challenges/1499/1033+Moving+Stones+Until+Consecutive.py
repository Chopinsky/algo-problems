'''
1033. Moving Stones Until Consecutive

There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.

In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

Return an integer array answer of length 2 where:

answer[0] is the minimum number of moves you can play, and
answer[1] is the maximum number of moves you can play.

Example 1:

Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
Example 2:

Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.
Example 3:

Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.

Constraints:

1 <= a, b, c <= 100
a, b, and c have different values.
'''

from typing import List

class Solution:
  def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    arr = sorted([a, b, c])
    d0 = arr[1] - arr[0] - 1
    d1 = arr[2] - arr[1] - 1
    # print(arr, d0, d1)
    
    if d0 == 0 and d1 == 0:
      return [0, 0]
    
    if d0 == 0:
      return [1, d1]
    
    if d1 == 0:
      return [1, d0]
      
    ans = []
    if d0 == 1 or d1 == 1:
      ans.append(1)
    else:
      ans.append(2)
    
    ans.append(d0+d1)
    
    return ans
  
    
        