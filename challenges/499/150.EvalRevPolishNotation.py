'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

from typing import List

class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    signs = {'+', '-', '*', '/'}
    
    def get_sign(val: int):
      return 1 if val >= 0 else -1
    
    for token in tokens:
      if token not in signs:
        stack.append(int(token))
        continue
        
      b = stack.pop()
      a = stack.pop()
        
      if token == '+':
        stack.append(a+b)
      
      if token == '-':
        stack.append(a-b)
        
      if token == '*':
        stack.append(a*b)
        
      if token == '/':
        sign = get_sign(a) * get_sign(b)
        stack.append(sign*(abs(a)//abs(b)))
        
      # print(token, stack[-1])
        
    return stack.pop()
  
  
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    op = set(['+', '-', '*', '/'])
    
    for s in tokens:
      if s in op:
        b = stack.pop()
        a = stack.pop()
        
        if s == '-':
          stack.append(a-b)
        elif s == '*':
          stack.append(a*b)
        elif s == '/':
          stack.append(int(a/b))
        else:
          stack.append(a+b)
          
      else:
        stack.append(int(s))
      
      # print(s, stack)
      
    return stack[0]

    
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []

    for t in tokens:
      if t == '+' or t == '-' or t == '*' or t == '/':
        l, r = stack.pop(), stack.pop()
        if t == '+':
          stack.append(r+l)
        elif t == '-':
          stack.append(r-l)
        elif t == '*':
          stack.append(r*l)
        elif t == '/':
          stack.append(int(r/l))

        # print(r, l, t)
      else:
        stack.append(int(t))

    return stack[0]
