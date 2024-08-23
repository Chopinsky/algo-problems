'''
592. Fraction Addition and Subtraction

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"

Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
'''

from math import gcd

class Solution:
  def fractionAddition(self, expression: str) -> str:
    t0, b0 = 0, 1
    val = ''
    stack = []
    
    def parse(val: str) -> tuple:
      sign = 1
      if val[0] == '+':
        val = val[1:]
        
      if val[0] == '-':
        sign = -1
        val = val[1:]
        
      parts = val.split('/')
      
      return (sign, int(parts[0]), int(parts[1]))
      
    for ch in expression:
      if (ch == '-' or ch == '+') and len(val) > 0:
        stack.append(parse(val))
        val = ch
      else:
        val += ch
      
    if val:
      stack.append(parse(val))
      
    # print(stack)
    for sign, t1, b1 in stack:
      b2 = (b0 * b1) // gcd(b0, b1)
      f0 = b2 // b0
      f1 = b2 // b1
      t0 = f0*t0 + sign*f1*t1
      b0 = b2
    
    # print('done:', t0, b0)
    if t0 == 0:
      return "0/1"
    
    g = gcd(t0, b0)
    t0 //= g
    b0 //= g
    
    return str(t0) + "/" + str(b0)
        
  def fractionAddition(self, expr: str) -> str:
    parts = []
    n = len(expr)
    last = 0
    
    for i in range(1, n):
      if expr[i] == '+' or expr[i] == '-':
        parts.append(expr[last:i])
        last = i
        
    parts.append(expr[last:])
    # print(parts)
    
    if len(parts) == 1:
      return parts[0]
    
    def div(s: str):
      res = s.split('/')
      return int(res[0]), int(res[1])
    
    t0, b0 = div(parts[0])
    # print('init:', t0, b0)
    
    for s in parts[1:]:
      t1, b1 = div(s)
      if b1 == b0:
        t0 += t1
        
      else:
        t0 = t0*b1 + t1*b0
        b0 *= b1
        # print('post', s, b0, t0)
        
      if t0 == 0:
        b0 = 1

      else:
        g = gcd(t0, b0)
        t0 //= g
        b0 //= g
        
      # print(s, (t1, b1), (t0, b0))
    
    return f'{t0}/{b0}'
  