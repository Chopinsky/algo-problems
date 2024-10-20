'''
Return the result of evaluating a given boolean expression, represented as a string.

An expression can either be:

"t", evaluating to True;
"f", evaluating to False;
"!(expr)", evaluating to the logical NOT of the inner expression expr;
"&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
"|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...
 

Example 1:

Input: expression = "!(f)"
Output: true
Example 2:

Input: expression = "|(f,t)"
Output: true
Example 3:

Input: expression = "&(t,f)"
Output: false
Example 4:

Input: expression = "|(&(t,f,t),!(t))"
Output: false
 

Constraints:

1 <= expression.length <= 20000
expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
expression is a valid expression representing a boolean, as given in the description.
'''

from typing import List


class Solution:
  def parseBoolExpr(self, e: str) -> bool:
    n = len(e)
    stack = []
    paren = {}
    seg = {}
    
    for i in range(n):
      ch = e[i]
      if ch == '(' or ch == ',':
        stack.append((i, ch))
        continue
        
      if ch == ')':
        while stack and stack[-1][1] == ',':
          r, _ = stack.pop()
          if stack:
            l = stack[-1][0]
            seg[l+1] = r-1
            # print('add seg:', e[l+1:r])
            
        if stack and stack[-1][1] == '(':
          l, _ = stack.pop()
          paren[l] = i
          # print('add paren:', e[l:i+1])
        
    # print('init:', paren, seg)
    
    def eval_arr(arr: List, is_and: bool) -> bool:
      res = arr[0]
      for val in arr[1:]:
        if is_and:
          res = res and val
        else:
          res = res or val
          
      return res
          
    def parse(i: int, j: int) -> List[bool]:
      if i >= j:
        return [e[i] == 't']
      
      idx = i
      res = []
      # print('parse:', e[i:j+1])
      
      while idx <= j:
        ch = e[idx]
        # print('check:', (ch, idx))
        
        if ch == '!':
          l = idx+1
          r = paren[l]
          arr = parse(l+1, r-1)
          res.append(not arr[0])
          idx = r+1
          continue
          
        if ch == '&' or ch == '|':
          l = idx+1
          r = paren[l]
          arr = parse(l+1, r-1)
          res.append(eval_arr(arr, ch == '&'))
          idx = r+1
          continue
          
        if ch != ',':
          res.append(e[idx] == 't')
          
        idx += 1
          
      # print('done:', res)
      return res
      
    res = parse(0, n-1)
    
    return res[0]
        
  def parseBoolExpr(self, expr: str) -> bool:
    stack = []
    ops = []
    curr = []
    
    for ch in expr:
      if ch == ',':
        continue
        
      # push into the operator stack
      if ch == '!' or ch == '|' or ch == '&':
        ops.append(ch)
        continue
        
      # start a new stack
      if ch == '(':
        stack.append(curr)
        curr = []
        continue
        
      if ch == ')':
        op = ops.pop()
        res = False
        
        if op == '!':
          res = not curr[0]
        elif op == '|':
          res = any(val == True for val in curr)
        elif op == '&':
          res = all(val == True for val in curr)
        
        # print('pop', op, curr, res, stack)
        curr = stack.pop() if stack else []
        curr.append(res)
        
        continue
        
      curr.append(True if ch == 't' else False)
        
    # print('done', curr, stack, ops)
    return curr[0] if curr else False
  