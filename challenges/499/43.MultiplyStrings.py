'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''


class Solution:
  def multiply(self, num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0':
      return '0'
    
    def add(a: str, b: str) -> str:
      if a == '0':
        return b
      
      if b == '0':
        return a
      
      if len(a) < len(b):
        a, b = b, a
      
      a = a[::-1]
      b = b[::-1]
      
      ans = ""
      co = 0
      o = ord('0')
      
      for i in range(len(a)):
        d = (ord(a[i])-o) + (ord(b[i])-o if i < len(b) else 0) + co
        # print(i, d)
        
        if d >= 10:
          d -= 10
          co = 1
        else:
          co = 0
          
        ans = str(d) + ans
      
      if co:
        ans = '1' + ans
      
      return ans
    
    def mult(a: str, b: str, padding: int) -> str:
      b = int(b)
      if not b:
        return '0'
      
      co = 0
      ans = ""
      o = ord('0')
      
      for n in a[::-1]:
        val = (ord(n) - o) * b + co
        
        if val >= 10:
          co = val // 10
          val %= 10
        else:
          co = 0
          
        ans = str(val) + ans
        
      if co > 0:
        ans = str(co) + ans
      
      return ans + '0' * padding
      
    if len(num1) < len(num2):
      num1, num2 = num2, num1
      
    ans = None
    for i, n in enumerate(num2[::-1]):
      val = mult(num1, n, i)
      # print(val, num1, n, i)
      
      if not ans:
        ans = val
      else:
        ans = add(ans, val)
      
    return ans
  