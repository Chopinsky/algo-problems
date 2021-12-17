'''
You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", then there are one or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let expression is the value of the expression expr.
An add expression takes the form "(add e1 e2)" where add is always the string "add", there are always two expressions e1, e2 and the result is the addition of the evaluation of e1 and the evaluation of e2.
A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", there are always two expressions e1, e2 and the result is the multiplication of the evaluation of e1 and the evaluation of e2.
For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names "add", "let", and "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.

Example 1:

Input: expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.
Example 2:

Input: expression = "(let x 3 x 2 x)"
Output: 2
Explanation: Assignment in let statements is processed sequentially.
Example 3:

Input: expression = "(let x 1 y 2 x (add x y) (add x y))"
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

Constraints:

1 <= expression.length <= 2000
There are no leading or trailing spaces in exprssion.
All tokens are separated by a single space in expressoin.
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
The expression is guaranteed to be legal and evaluate to an integer.
'''


from typing import Tuple
from collections import defaultdict


class Solution:
  def evaluate(self, expression: str) -> int:
    var_table = defaultdict(list)
    
    def calc(op: str, src: str) -> Tuple[int, int]:
      # print('calc', op, src)
      var_name = ''
      value = None
      vals = []
      idx = 5 if op == 'm' else 4
      
      while idx < len(src) and src[idx] != ')':
        if src[idx] == ' ':
          if value:
            vals.append(value[0] * value[1])
            value = None
            
          elif var_name:
            if (var_name in var_table) and var_table[var_name]:
              vals.append(var_table[var_name][-1])
            else:
              raise ValueError('incorrect var_name', var_name, var_table, op, src)
            
            var_name = ''
          
        elif src[idx] == '(':
          val, offset = eval_expr(src[idx:])
          if offset <= 0:
            raise ValueError('incorrect recursion:', src, idx)
            
          vals.append(val)
          idx += offset
          
        elif (not var_name) and (src[idx] == '-' or src[idx].isnumeric()):
          if not value:
            value = [-1 if src[idx] == '-' else 1, 0]
            
          if src[idx] != '-':
            value[1] = 10 * value[1] + int(src[idx])
          
        else:
          var_name += src[idx]
        
        idx += 1
        
      if value:
        vals.append(value[0] * value[1])
      elif var_name and (var_name in var_table) and var_table[var_name]:
        vals.append(var_table[var_name][-1])
        
      # print('calc fin:', vals, var_name)
      return (vals[0] * vals[1] if op == 'm' else vals[0] + vals[1], idx)
      
    
    def eval_expr(src: str) -> Tuple[int, int]:
      if not src:
        return 0
      
      if src[0] != '(':
        raise ValueError('Incorrect string:', src)
      
      if (len(src) > 5 and src[1:5] == 'mult'):
        return calc('m', src)
      
      if (len(src) > 4 and src[1:4] == 'add'):
        return calc('a', src)
      
      # let expression      
      idx = 4
      tokens = set()
      var_name = ''
      last_var_name = ''
      var_val = None
      # print('run:', src)
      
      while idx < len(src) and src[idx] != ')':
        # print('eval', idx, src[idx])
        
        if src[idx] == '(':
          val, offset = eval_expr(src[idx:])
          if offset <= 0:
            raise ValueError('irregular recursion:', src, idx, offset)
            
          idx += offset
          var_val = [1, val]
          # print('assign', val, src[idx:])
          
        elif src[idx] == ' ':
          if last_var_name:
            if var_val:
              val = var_val[0] * var_val[1]
            elif var_name:
              val = var_table[var_name][-1]
            else:
              raise ValueError('Incorrect assignment', last_var_name, var_name, var_val)
            
            if last_var_name in tokens:
              var_table[last_var_name][-1] = val
            else:
              var_table[last_var_name].append(val)
              
            tokens.add(last_var_name)
            last_var_name = ''
            
          else:
            last_var_name = var_name
            
          var_name = ''
          var_val = None
            
        elif (not var_name) and (src[idx] == '-' or src[idx].isnumeric()):
          if not var_val:
            var_val = [-1 if src[idx] == '-' else 1, 0]
            
          if src[idx] != '-':
            var_val[1] = 10 * var_val[1] + int(src[idx])

        else:
          var_name += src[idx]
        
        idx += 1

      # print('done', src, var_val, var_name)
      if var_name and var_name in var_table:
        res = var_table[var_name][-1]
      elif var_val:
        res = var_val[0] * var_val[1]
      else:
        raise ValueError('Incorrect result:', src, var_name, var_val, tokens)
        
      # popping scoped variables
      for var_name in tokens:
        var_table[var_name].pop()
        if not var_table[var_name]:
          var_table.pop(var_name, None)
        
      return (res, idx)
      
    res, _ = eval_expr(expression)
    return res
  