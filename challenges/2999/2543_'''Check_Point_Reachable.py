'''
2543. Check if Point Is Reachable

There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point (targetX, targetY) using a finite number of steps.

In one step, you can move from point (x, y) to any one of the following points:

(x, y - x)
(x - y, y)
(2 * x, y)
(x, 2 * y)
Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.

Example 1:

Input: targetX = 6, targetY = 9
Output: false
Explanation: It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned.
Example 2:

Input: targetX = 4, targetY = 7
Output: true
Explanation: You can follow the path (1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7).

Constraints:

1 <= targetX, targetY <= 10^9
'''

from collections import deque
from functools import lru_cache
from math import gcd


class Solution:
  """
  idea is if we can go from (tx, ty) back to (1, 1), i.e., the problem is reversible; 
  technically speaking, we want to reduce the coordinate as fast as possible -- that
  is to say: 1) val --> val // 2 repeat until val is odd; 2) (x, y) -> (x+y) // 2 if
  both x and y are odd numbers, and repeat; 3) relacing the larger number with (x+y)//2
  in the (x, y) pair, and continue.
  """
  def isReachable(self, tx: int, ty: int) -> bool:
    @lru_cache(None)
    def reduce(val: int) -> int:
      while val % 2 == 0:
        val //= 2
        
      return val
    
    stack = deque([(reduce(tx), reduce(ty))])
    seen = set(stack)
    
    while stack:
      x0, y0 = stack.popleft()
      if x0 == 1 or y0 == 1:
        return True
      
      if x0 == y0:
        continue
      
      v0 = reduce(x0 + y0)
      if v0 == 1:
        return True
      
      if v0 == x0 or v0 == y0:
        continue
        
      if x0 < y0 and (x0, v0) not in seen:
        stack.append((x0, v0))
        seen.add((x0, v0))
        
      if x0 > y0 and (v0, y0) not in seen:
        stack.append((v0, y0))
        seen.add((v0, y0))
        
    return False
    
    
  def isReachable0(self, tx: int, ty: int) -> bool:
    @lru_cache(None)
    def is_two_power(val):
      return bin(val)[2:].count('1') == 1
    
    if is_two_power(tx) or is_two_power(ty):
      return True
    
    v = gcd(tx, ty)
    while v % 2 == 0:
      v //= 2
      
    return v == 1
    