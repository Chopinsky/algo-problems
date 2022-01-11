'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''


class Solution:
  def calculate(self, s: str) -> int:
    stack = []
    val = 0
    op = ''
    
    for ch in s:
      # print(ch, stack, val, op)
      if ch == ' ':
        continue
        
      if ch == '+' or ch == '-' or ch == '*' or ch == '/':
        if (not stack) or (stack[-1][1] == '+' or stack[-1][1] == '-'):
          stack.append((val, ch))
        else:
          last, lop = stack.pop()
          stack.append((last * val if lop == '*' else last // val, ch))
          
        val = 0
        op = ''
        continue
        
      val = 10 * val + ord(ch) - ord('0')
        
    if stack and (stack[-1][1] == '*' or stack[-1][1] == '/'):
      last, op = stack.pop()
      stack.append((last * val if op == '*' else last // val, ''))
    else:
      stack.append((val, ''))
      
    val, op = stack[0]
    for i in range(1, len(stack)):
      val = val + stack[i][0] if op == '+' else val - stack[i][0]
      op = stack[i][1]
        
    return val
  