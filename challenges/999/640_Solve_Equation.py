'''
640. Solve the Equation

Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

Example 1:

Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:

Input: equation = "x=x"
Output: "Infinite solutions"
Example 3:

Input: equation = "2x=x"
Output: "x=0"

Constraints:

3 <= equation.length <= 1000
equation has exactly one '='.
equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.
'''


class Solution:
  def solveEquation(self, equation: str) -> str:
    left, right = equation.split('=')
    # print(left, right)
    
    def notion_value(s: str):
      x, cst = 0, 0
      val = -1
      sign = 1
      
      for ch in s:
        if '0' <= ch <= '9':
          if val < 0:
            val = int(ch)
          else:
            val = (10*val + int(ch))
            
        elif ch == 'x':
          x += sign * (1 if val < 0 else val)
          val = -1
          
        else:
          if val >= 0:
            cst += sign * val
            
          sign = 1 if ch == '+' else -1
          val = -1
      
        # print(ch, sign, val, (x, cst))
        
      if val >= 0:
        cst += sign * val
        
      return x, cst
    
    lx, lc = notion_value(left)
    rx, rc = notion_value(right)
    # print((lx, lc), (rx, rc))
    
    x = lx-rx
    if x == 0:
      return 'Infinite solutions' if lc == rc else 'No solution'
      
    return f'x={(rc-lc) // x}'
    