'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:

10 <= low <= high <= 10^9
'''

from typing import List

class Solution:
  def sequentialDigits(self, low: int, high: int) -> List[int]:
    low_str = str(low)
    high_str = str(high)
    i0, d0 = int(low_str[0]), len(low_str)
    i1, d1 = int(high_str[0]), len(high_str)
    ans = []
    
    def generate(i: int, d: int):
      if i+d > 10:
        return -1
      
      curr = 0
      for _ in range(d):
        curr = curr*10 + i
        i += 1
        
      return curr
    
    for d in range(d0, d1+1):
      start, end = 1, 10
      if d == d0:
        start = i0
        
      if d == d1:
        end = i1+1
        
      for i in range(start, end):
        val = generate(i, d)
        if val < 0 or val > high:
          break
          
        if low <= val <= high:
          ans.append(val)
    
    return ans
        

  def sequentialDigits(self, low: int, high: int) -> List[int]:
    ans = []
    l, h = str(low), str(high)
    lnl, lnh = len(l), len(h)
    
    for ln in range(lnl, lnh+1):
      a = int(l[0]) if ln == lnl else 1
      b = int(h[0]) if ln == lnh else 10-ln
      # print(ln, a, b)
      
      for base in range(a, b+1):
        val = base
        base += 1
        
        for i in range(1, ln):
          if base >= 10:
            val = -1
            break
            
          val = 10*val + base
          base += 1
          
        # print(ln, val)
        if low <= val <= high:
          ans.append(val)
    
        if val > high:
          break
          
    return ans
  