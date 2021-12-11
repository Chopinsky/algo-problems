'''
You are playing a variation of the game Zuma.

In this variation of Zuma, there is a single row of colored balls on a board, where each ball can be colored red 'R', yellow 'Y', blue 'B', green 'G', or white 'W'. You also have several colored balls in your hand.

Your goal is to clear all of the balls from the board. On each turn:

Pick any ball from your hand and insert it in between two balls in the row or on either end of the row.
If there is a group of three or more consecutive balls of the same color, remove the group of balls from the board.
If this removal causes more groups of three or more of the same color to form, then continue removing each group until there are none left.
If there are no more balls on the board, then you win the game.
Repeat this process until you either win or do not have any more balls in your hand.
Given a string board, representing the row of balls on the board, and a string hand, representing the balls in your hand, return the minimum number of balls you have to insert to clear all the balls from the board. If you cannot clear all the balls from the board using the balls in your hand, return -1.

 

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: It is impossible to clear all the balls. The best you can do is:
- Insert 'R' so the board becomes WRRRBBW. WRRRBBW -> WBBW.
- Insert 'B' so the board becomes WBBBW. WBBBW -> WW.
There are still balls remaining on the board, and you are out of balls to insert.
Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: To make the board empty:
- Insert 'R' so the board becomes WWRRRBBWW. WWRRRBBWW -> WWBBWW.
- Insert 'B' so the board becomes WWBBBWW. WWBBBWW -> WWWW -> empty.
2 balls from your hand were needed to clear the board.
Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: To make the board empty:
- Insert 'G' so the board becomes GG.
- Insert 'G' so the board becomes GGG. GGG -> empty.
2 balls from your hand were needed to clear the board.
Example 4:

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: To make the board empty:
- Insert 'Y' so the board becomes RBYYYBBRRB. RBYYYBBRRB -> RBBBRRB -> RRRB -> B.
- Insert 'B' so the board becomes BB.
- Insert 'B' so the board becomes BBB. BBB -> empty.
3 balls from your hand were needed to clear the board.
 

Constraints:

1 <= board.length <= 16
1 <= hand.length <= 5
board and hand consist of the characters 'R', 'Y', 'B', 'G', and 'W'.
The initial row of balls on the board will not have any groups of three or more consecutive balls of the same color.
'''


from functools import lru_cache
from collections import Counter


class Solution:
  def findMinStep(self, board: str, hand: str) -> int:
    if not board:
      return 0
    
    @lru_cache(None)
    def reduce(left: str, right: str) -> str:
      if not left or not right or left[-1] != right[0]:
        return left + right
      
      char = right[0]
      i, j = len(left), -1
      cl, cr = 0, 0
      
      while i-1 >= 0 and left[i-1] == char:
        i -= 1
        cl += 1
        
      while j+1 < len(right) and right[j+1] == char:
        j += 1
        cr += 1
        
      # can't reduce from here
      if cl + cr < 3:
        return left + right
        
      # keep reducing
      return reduce(left[:i], right[j+1:])
    
    hand = Counter(hand)
    base = sorted(hand)
    cache = {}
    
    def strike(src: str, used: int) -> int:
      if not src:
        return used
      
      key = ''
      least = -1
      n = len(src)
      
      for char in base:
        if hand[char] > 0:
          key += f'{char}-{hand[char]};'
          
      # no more balls left in hand
      if src and not key:
        return -1
      
      if (src, key) in cache:
        return cache[src, key]
      
      for i in range(n+1):
        for char in base:
          if not hand[char]:
            continue
            
          left = src[:i]+char if i != n else src[:i]
          right = src[i:] if i != n else char
          nxt = reduce(left, right)
          
          hand[char] -= 1
          cnt = strike(nxt, used+1)
          
          if cnt > 0:
            least = cnt if least < 0 else min(least, cnt)
          
          hand[char] += 1
          
      cache[src, key] = least
      return least
      
    return strike(board, 0)
      