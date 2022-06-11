'''
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199

Constraints:

1 <= num.length <= 35
num consists only of digits.

Follow up: How would you handle overflow for very large input integers?
'''


class Solution:
  def isAdditiveNumber(self, num: str) -> bool:
    n = len(num)
    
    def test(a: int, b: int, k: int) -> bool:
      if k >= n:
        return False
      
      while k < n:
        c = a + b
        c_str = str(c)
        ln = len(c_str)
        
        if num[k:k+ln] != c_str:
          return False
        
        a, b = b, c
        k += ln
        
      return True
    
    for i in range(n-2):
      if num[0] == '0' and i > 0:
        return False
      
      for j in range(i+1, n-1):
        if num[i+1] == '0' and j > i+1:
          continue
          
        if test(int(num[:i+1]), int(num[i+1:j+1]), j+1):
          return True
        
    return False
        