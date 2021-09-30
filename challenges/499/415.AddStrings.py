'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:

1 <= num1.length, num2.length <= 10 ** 4
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
'''


class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    n1 = list(num1)
    n2 = list(num2)
    
    n1.reverse()
    n2.reverse()
    
    ans = []
    idx = 0
    extra = 0
    o0 = ord('0')
    
    while idx < len(n1) or idx < len(n2):
      v1, v2 = 0, 0
      if idx < len(n1):
        v1 = ord(n1[idx]) - o0
        
      if idx < len(n2):
        v2 = ord(n2[idx]) - o0
        
      val = v1 + v2 + extra
      if val >= 10:
        val -= 10
        extra = 1
      else:
        extra = 0
        
      ans.append(chr(val + o0))
      idx += 1
      
    if extra == 1:
      ans.append('1')
      
    # print(ans)
    ans.reverse()
    
    return ''.join(ans)
  