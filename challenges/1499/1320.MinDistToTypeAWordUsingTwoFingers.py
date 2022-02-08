'''

You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
Given the string word, return the minimum total distance to type such string using only two fingers.

The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

Example 1:

Input: word = "CAKE"
Output: 3
Explanation: Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3
Example 2:

Input: word = "HAPPY"
Output: 6
Explanation: Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6

Constraints:

2 <= word.length <= 300
word consists of uppercase English letters.
'''


from typing import Tuple
from functools import lru_cache


class Solution:
  def minimumDistance(self, word: str) -> int:
    @lru_cache(None)
    def key_pos(k: str) -> Tuple:
      idx = ord(k) - ord('A')
      return idx//6, idx%6
    
    @lru_cache(None)
    def key_dist(a: str, b: str) -> int:
      if a == b or not a or not b:
        return 0
      
      xa, ya = key_pos(a)
      xb, yb = key_pos(b)
      
      return abs(xa-xb) + abs(ya-yb)
    
    @lru_cache(None)
    def dp(idx: int, l: str, r: str) -> int:
      if idx == len(word):
        return 0
      
      key = word[idx]
      
      # if move left finger to the idx-key
      s0 = dp(idx+1, min(key, r), max(key, r)) + key_dist(min(key, l), max(key, l))
      
      # if move right finger to the idx-key
      s1 = dp(idx+1, min(key, l), max(key, l)) + key_dist(min(key, r), max(key, r))
      
      # take the min move as the result
      return min(s0, s1)
      
    return dp(0, '', '')
    