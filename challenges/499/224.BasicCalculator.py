'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:

1 <= s.length <= 3 * 10 ** 5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation.
'-' could be used as a unary operation but it has to be inside parentheses.
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''


class Solution:
  def calculate(self, s: str) -> int:
    stack = []
    curr = []
    val = ''
    
    def calc(arr, val):
      if val:
        arr.append(int(val))
        val = ''

      base = arr[0]
      # print('calc:', base, arr)

      for i in range(1, len(arr), 2):
        if arr[i] == '+':
          base += arr[i+1]

        else:
          base -= arr[i+1]
      
      return base
    
    for ch in s:
      if ch == ' ':
        if val:
          curr.append(int(val))
          val = ''
        
        continue
        
      if ch == '(':
        stack.append(curr)
        curr = []
        continue
        
      if ch == ')':
        base = calc(curr, val)
        val = ''
        curr = stack.pop()
        curr.append(base)
        
        continue
        
      if ch == '-' or ch == '+':
        if val:
          curr.append(int(val))
          val = ''
          
        if ch == '-' and not curr:
          curr.append(0)
          
        curr.append(ch)
        continue
        
      val += ch
    
    # print(stack, curr)
    return calc(curr, val)
  

  def calculate(self, s: str) -> int:
    def calc(expr) -> int:
      base = 0
      op = 1
      
      for e in expr:
        if e == '+':
          op = 1
        elif e == '-':
          op = -1
        else:
          base += op * e
      
      # print("calc:", expr, base)
      return base
    
    stack = [[]]
    i = 0
    ans = 0
    o = ord('0')
    
    while i < len(s):
      # padding, skip
      if s[i] == ' ':
        i += 1
        continue
        
      # starting a branch
      if s[i] == '(':
        stack.append([])
        i += 1
        continue
        
      # evaluate a closed branch
      if s[i] == ')':
        val = calc(stack.pop())
        stack[-1].append(val)
        i += 1
        # print("end:", stack)
        continue
        
      # append the operator
      if s[i] == '+' or s[i] == '-':
        stack[-1].append(s[i])
        i += 1
        continue
        
      # parse the int, add it to the branch stack
      val = 0
      sign = 1
      
      if s[i] == '-':
        sign = -1
        i += 1
      
      while i < len(s) and '0' <= s[i] <= '9':
        val = 10*val + (ord(s[i]) - o)
        i += 1
        
      stack[-1].append(sign*val)
    
    # print(stack)
    if stack:
      ans = calc(stack.pop())
    
    return ans
