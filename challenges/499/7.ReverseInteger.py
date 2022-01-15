'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
'''


class Solution:
  def reverse(self, x: int) -> int:
    if not x:
      return x
    
    sign = 1
    if x < 0:
      sign = -1
      x = -x
      
    sx = ''.join(reversed(str(x)))
    bound = str((1<<31)-1) if sign > 0 else str(1<<31)
    # print(sx, str(x), bound)
    
    if len(sx) == len(bound) and sx > bound:
      return 0
    
    return int(sx) if sign > 0 else int('-' + sx)
      