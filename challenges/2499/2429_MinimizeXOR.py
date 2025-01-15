'''
2429. Minimize XOR

Given two positive integers num1 and num2, find the integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

Constraints:

1 <= num1, num2 <= 10^9
'''

from typing import List


class Solution:
  def minimizeXor(self, num1: int, num2: int) -> int:
    s1, s2 = bin(num1)[2:], bin(num2)[2:]
    cnt = s2.count('1')
    n1 = len(s1)
    # print('init:', s1, s2, cnt)

    def convert(bits: List) -> int:
      res = 0
      if not bits:
        return res

      mask = 1

      while bits:
        if bits.pop() == 1:
          res |= mask

        mask <<= 1

      return res

    if cnt >= n1:
      return convert([1]*cnt)

    bits = [0]*n1

    for i in range(n1):
      if cnt == 0:
        break

      if s1[i] == '1':
        bits[i] = 1
        cnt -= 1

    for i in range(n1-1, -1, -1):
      if cnt == 0:
        break

      if s1[i] == '0':
        bits[i] = 1
        cnt -= 1

    return convert(bits)
        
  def minimizeXor(self, num1: int, num2: int) -> int:
    c0 = bin(num2)[2:].count('1') 
    if c0 == 0:
      return num1
    
    rep1 = bin(num1)[2:]
    digits = list(rep1)
    c1 = digits.count('1')
    # print(c0, c1, digits)
    
    if c0 == c1:
      return num1
    
    if c0 < c1:
      for i in range(len(digits)):
        if digits[i] == '0':
          continue
        
        if c0 > 0:
          c0 -= 1
          continue
          
        digits[i] = '0'
      
    else:
      c0 -= c1
      for i in range(len(digits)-1, -1, -1):
        if digits[i] == '0' and c0 > 0:
          c0 -= 1
          digits[i] = '1'
      
      if c0 > 0:
        digits = ['1'] * c0 + digits
      
    res = 0
    # print(digits, c0)
    
    for d in digits:
      res = (res << 1) | (1 if d == '1' else 0)

    return res
