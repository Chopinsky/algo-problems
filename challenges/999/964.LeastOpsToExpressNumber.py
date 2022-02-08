'''
Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /). For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happen before addition and subtraction.
It is not allowed to use the unary negation operator (-). For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
We would like to write an expression with the least number of operators such that the expression equals the given target. Return the least number of operators used.

Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.
The expression contains 5 operations.
Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
The expression contains 8 operations.
Example 3:

Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.
The expression contains 3 operations.

Constraints:

2 <= x <= 100
1 <= target <= 2 * 10^8
'''


from functools import lru_cache
import math


class Solution:
  def leastOpsExpressTarget(self, x: int, target: int) -> int:
    if target == 1:
      return 0 if x == 1 else 1
      
    dic = {1:2}
    base = 1
    idx = 0
    
    while base*x < 2*target:
      base *= x
      idx += 1
      
      if idx == 1:
        dic[base] = 1
      else:
        dic[base] = idx
    
    # print(dic)
    
    @lru_cache(None)
    def dp(num: int, p: int) -> int:
      if num == 0:
        return 0
      
      if (p == 0) or (num > 2*target) or (pow(x, p) < num):
        return math.inf
      
      if num in dic:
        return dic[num]
      
      ops = math.inf
      base = 1
      
      for i in range(p):
        # if num == target:
        #   print(i, base)
          
        for j in range(1, max(x, 2)):
          ops = min(ops, j*dic[base] + dp(abs(num-j*base), i))
          
        base *= x
        
      return ops
      
    return dp(target, idx+1)-1
    