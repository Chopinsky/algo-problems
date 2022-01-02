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


class Solution:
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
  