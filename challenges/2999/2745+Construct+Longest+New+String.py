'''
2745. Construct the Longest New String

You are given three integers x, y, and z.

You have x strings equal to "AA", y strings equal to "BB", and z strings equal to "AB". You want to choose some (possibly all or none) of these strings and concatenate them in some order to form a new string. This new string must not contain "AAA" or "BBB" as a substring.

Return the maximum possible length of the new string.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:

Input: x = 2, y = 5, z = 1
Output: 12
Explanation: We can concactenate the strings "BB", "AA", "BB", "AA", "BB", and "AB" in that order. Then, our new string is "BBAABBAABBAB". 
That string has length 12, and we can show that it is impossible to construct a string of longer length.
Example 2:

Input: x = 3, y = 2, z = 2
Output: 14
Explanation: We can concactenate the strings "AB", "AB", "AA", "BB", "AA", "BB", and "AA" in that order. Then, our new string is "ABABAABBAABBAA". 
That string has length 14, and we can show that it is impossible to construct a string of longer length.

Constraints:

1 <= x, y, z <= 50
'''

from functools import lru_cache

class Solution:
  def longestString(self, x: int, y: int, z: int) -> int:
    @lru_cache(None)
    def build(x: int, y: int, z: int, last: str) -> int:
      rem = x+y+z
      if rem == 0:
        return 0
      
      if rem == 1:
        if (x == 1 or z == 1) and last != 'A':
          return 2
        
        if y == 1 and last != 'B':
          return 2
          
        return 0
      
      if last == 'A':
        # use 'BB'
        return 0 if y == 0 else 2+build(x, y-1, z, 'B')
      
      c0 = 0
      c1 = 0

      # use 'AA'
      if x > 0:
        c0 = 2+build(x-1, y, z, 'A')
        
      if z > 0:
        c1 = 2+build(x, y, z-1, 'B')
          
      return max(c0, c1)
        
    c0 = build(x, y, z, 'A')
    c1 = build(x, y, z, 'B')
    # print('end:', c0, c1)
    
    return max(c0, c1)
        