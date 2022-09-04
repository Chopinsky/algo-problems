'''
2396. Strictly Palindromic Number

An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.

Example 1:

Input: n = 9
Output: false
Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
In base 3: 9 = 100 (base 3), which is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
Note that in bases 4, 5, 6, and 7, n = 9 is also not palindromic.
Example 2:

Input: n = 4
Output: false
Explanation: We only consider base 2: 4 = 100 (base 2), which is not palindromic.
Therefore, we return false.

Constraints:

4 <= n <= 10^5
'''

class Solution:
  def isStrictlyPalindromic(self, n: int) -> bool:
    def is_pal(val: str) -> bool:
      i, j = 0, len(val)-1
      while i < j and val[i] == val[j]:
        i += 1
        j -= 1
        
      return i >= j
    
    def to_str(val: int, base: int) -> str:
      res = ''
      while val > 0:
        res = str(val % base) + res
        val //= base
        
      # print(val, base, res)
      return res
    
    for base in range(2, n-1):
      if not is_pal(to_str(n, base)):
        return False
      
    return True
    