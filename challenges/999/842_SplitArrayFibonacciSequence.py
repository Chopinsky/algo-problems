'''
You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
f.length >= 3, and
f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

Example 1:

Input: num = "1101111"
Output: [11,0,11,11]
Explanation: The output [110, 1, 111] would also be accepted.
Example 2:

Input: num = "112358130"
Output: []
Explanation: The task is impossible.
Example 3:

Input: num = "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Constraints:

1 <= num.length <= 200
num contains only digits.
'''

from typing import List


class Solution:
  def splitIntoFibonacci(self, num: str) -> List[int]:
    n = len(num)
    limit = 2**31
    
    def build(n0: int, n1: int, k: int):
      if k >= n:
        return None
      
      res = [n0, n1]
      # print(n0, n1, k)
      
      while k < n:
        nxt = res[-2] + res[-1]
        if nxt >= limit:
          return None
        
        nxt_str = str(nxt)
        ln = len(nxt_str)
        
        if num[k:k+ln] != nxt_str:
          return None
        
        res.append(nxt)
        k += ln
        
      return res if len(res) >= 3 else None
    
    for i in range(n-2):
      if num[0] == '0' and i > 0:
        return []
      
      for j in range(i+1, n-1):
        if num[i+1] == '0' and j > i+1:
          continue
          
        res = build(int(num[:i+1]), int(num[i+1:j+1]), j+1)
        if res:
          return res
        
    return []
  