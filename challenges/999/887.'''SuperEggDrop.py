'''
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

Example 1:

Input: k = 1, n = 2
Output: 2
Explanation: 
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.

Example 2:

Input: k = 2, n = 6
Output: 3

Example 3:

Input: k = 3, n = 14
Output: 4

Constraints:

1 <= k <= 100
1 <= n <= 10^4
'''


from functools import lru_cache


class Solution:
  def superEggDrop(self, k: int, n: int) -> int:
    # steps for n-th floors if we have k' egg (init condition: k' == 1)
    last = [i for i in range(n+1)]
    # steps for n-th floors if we have 1 more egg to spare
    curr = []
    
    # try k eggs from 1 to k:
    # since the dp division only cares about (k-1, i-1) and (k, n-i),
    # we can only dp the last row and the current row of the dp states
    for _ in range(2, k+1):
      curr.append(0)
      floor = 1  # initial dividing point (aka the floor to drop the egg)
      
      # build the n-floors state 1 at a time
      for n in range(1, n+1):
        # if moving the dividing point, i.e. the floor to drop the egg,
        # we can obtain less steps, move the floor now. last[floor-1] means the numbers
        # of steps if the current egg break at `floor`, and curr[n-floor] is if the egg
        # does not break, we still have k' eggs
        while (floor < n) and (max(last[floor-1], curr[n-floor]) > max(last[floor], curr[n-floor-1])):
          floor += 1
      
        # drop from `floor`, and it takes:
        # 1 + most_steps_from_possible_scenarios(dp_break(floor-1, k-1), dp_not_break(n-floor, k))
        steps = 1 + max(last[floor-1], curr[n-floor])
        curr.append(steps)
        
      last, curr = curr, last
      curr.clear()
    
    return last[-1]
  
    
  def superEggDrop0(self, k: int, n: int) -> int:
    @lru_cache(None)
    def drop(k: int, n: int) -> int:
      if n <= 2:
        return n
      
      if k == 1:
        return n
      
      l, r = 1, n
      
      # try to find div position such that left-right counts
      # are the closest
      while l+1 < r:
        floor = (l + r) // 2
        l_cnt = drop(k-1, floor-1)
        r_cnt = drop(k, n-floor)
        
        if l_cnt < r_cnt:
          l = floor
        elif l_cnt > r_cnt:
          r = floor
        else:
          l = floor
          r = floor
          break
      
      return 1 + min(max(drop(k-1, floor-1), drop(k, n-floor)) for floor in (l, r))
    
    return drop(k, n)
    