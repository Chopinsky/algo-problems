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
  