'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: left = 5, right = 7
Output: 4

Example 2:

Input: left = 0, right = 0
Output: 0

Example 3:

Input: left = 1, right = 2147483647
Output: 0

Constraints:

0 <= left <= right <= 2^31 - 1
'''


class Solution:
  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    if left == 0 or left == right:
      return left
    
    ans = 0
    mask = 1
    
    while (mask<<1) <= right:
      mask <<= 1
      
    # print(left, right, mask)
    
    while mask > 0:
      tl, tr = mask & left, mask & right
      if tl != tr:
        break
        
      if tl:
        ans |= mask
        
      mask >>= 1
    
    return ans
    