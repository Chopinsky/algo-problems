'''
1621. Number of Sets of K Non-Overlapping Line Segments

Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

Example 1:

Input: n = 4, k = 2
Output: 5
Explanation: The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.

Constraints:

2 <= n <= 1000
1 <= k <= n-1
'''

from functools import lru_cache


class Solution:
  '''
  for each point in the plane, consider the states: (idx_of_the_point, num_of_lines_to_finish, if_a_line_started),
  so we can calculate the sets of lines based on `if_a_line_started`: 1) if in a line, count = <line_ends_here> + 
  <line_continues>; 2) if not in a line, count = <line_starts_here> + <line_not_starts_here>
  '''
  def numberOfSets(self, n: int, k: int) -> int:
    mod = 10**9+7
    
    @lru_cache(None)
    def dp(i: int, rem: int, line: bool) -> int:
      if rem == 1:
        ln = n-i
        return ln if line else (ln * (ln-1) // 2) % mod
      
      if line:
        if n-i-1 <= rem-1:
          return 1 if n-i-1 == rem-1 else 0
        
        # end @ i
        c0 = dp(i, rem-1, False)
        
        # don't end @ i
        c1 = dp(i+1, rem, True)
        
        # print('started', i, c0, c1)
        return (c0 + c1) % mod
      
      if n-i-1 <= rem:
        return 1 if n-i-1 == rem else 0
        
      # start @ i
      c0 = dp(i+1, rem, True)
      
      # don't start @ i
      c1 = dp(i+1, rem, False)
        
      # print('not started', i, c0, c1)
      return (c0 + c1) % mod
      
    return dp(0, k, False)
    