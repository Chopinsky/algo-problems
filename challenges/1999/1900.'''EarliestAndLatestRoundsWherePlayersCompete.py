'''
There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

For example, if the row consists of players 1, 2, 4, 6, 7
Player 1 competes against player 7.
Player 2 competes against player 6.
Player 4 automatically advances to the next round.
After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.

Example 1:

Input: n = 11, firstPlayer = 2, secondPlayer = 4
Output: [3,4]
Explanation:
One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4

Example 2:

Input: n = 5, firstPlayer = 1, secondPlayer = 5
Output: [1,1]
Explanation: The players numbered 1 and 5 compete in the first round.
There is no way to make them compete in any other round.
 

Constraints:

2 <= n <= 28
1 <= firstPlayer < secondPlayer <= n
'''


from functools import lru_cache
from typing import List, Tuple
import math


class Solution:
  def earliestAndLatest(self, n: int, first: int, second: int) -> List[int]:
    @lru_cache
    def solve(n, f, s):
      if f > n+1-s:
        return solve(n, n+1-s, n+1-f)
      
      if f == n+1-s:
        return (1, 1)

      ans_mn, ans_mx = math.inf, -math.inf
      
      for i in range(1, f+1):
        must_lose = max(0, s-1-(n-1)//2)
        must_win = max(0, must_lose-1 + (n%2))
        
        for j in range(i+must_win+1, i+s-f-must_lose+1):
          mn, mx = solve((n+1)//2, i, j)
          ans_mn = min(ans_mn, mn)
          ans_mx = max(ans_mx, mx)
          
      return (ans_mn+1, ans_mx+1)

    return list(solve(n, first, second))
    
    
  def earliestAndLatest0(self, n: int, first: int, second: int) -> List[int]:
    if (n == 2) or (first == 1 and second == n): 
      return [1, 1]
    
    first -= 1
    second -= 1
    target = (1<<first) | (1<<second)
    
    @lru_cache(None)
    def count_rounds(state: int) -> Tuple:
      if state == target:
        return (1, 1)
      
      states, nxt = set([0]), set()
      l, r = 0, n-1
      
      while l <= r:
        left_only, right_only = False, False
        
        while state & (1<<l) == 0:
          l += 1

        while state & (1<<r) == 0:
          r -= 1
          
        if l > r:
          break
          
        # the two players meet
        if l == first and r == second:
          return (1, 1)
          
        if (l == first) or (l == second) or l == r:
          # left player always wins
          left_only = True
        elif (r == first) or (r == second):
          # right player always wins
          right_only = True

        # if format(state, '#012b') == '0b0010010100':
        #   print('l, r:', l, r, left_only, right_only)
          
        if not right_only:
          for s in states:
            nxt.add(s | (1<<l))

        if not left_only:
          for s in states:
            nxt.add(s | (1<<r))

        states, nxt = nxt, states
        nxt.clear()
          
        l += 1
        r -= 1
      
      least, most = math.inf, 0
      for s in states:
        l0, m0 = count_rounds(s)

        # if format(state, '#012b') == '0b11111111111':
        #   print(format(state, '#012b'), format(s, '#012b'), l0, m0)
          
        most = max(most, m0)
        least = min(least, l0)
        
      # print(format(state, '#012b'), least+1, most+1)
      return (least+1, most+1)
      
    return list(count_rounds((1<<n)-1))
    