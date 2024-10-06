'''
1017. Convert to Base -2

Given an integer n, return a binary string representing its representation in base -2.

Note that the returned string should not have leading zeros unless the string is "0".

Example 1:

Input: n = 2
Output: "110"
Explantion: (-2)2 + (-2)1 = 2
Example 2:

Input: n = 3
Output: "111"
Explantion: (-2)2 + (-2)1 + (-2)0 = 3
Example 3:

Input: n = 4
Output: "100"
Explantion: (-2)2 = 4

Constraints:

0 <= n <= 10^9
'''

class Solution:
  '''
  the idea is to compensate the odd digits with additional +mask
  '''
  def baseNeg2(self, n: int) -> str:
    if n == 0:
      return '0'
    
    s = ''
    pos = 0
    mask = 1
    
    while mask <= n:
      bit = '1' if mask&n > 0 else '0'
      s = bit + s
      
      if pos%2 == 1 and mask&n > 0:
        n += mask
        
      mask <<= 1
      pos += 1
    
    return s
        