'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''


class Solution:
  def addBinary(self, a: str, b: str) -> str:
    if a == '0':
      return b
    
    if b == '0':
      return a
    
    a = list(reversed(a))
    b = list(reversed(b))
    if len(a) < len(b):
      a, b = b, a
    
    ans = []
    i, carryover = 0, 0
    # print(a, b)
    
    while i < len(a):
      if i >= len(b):
        if not carryover:
          ans.append(a[i])
        else:
          ans.append('0' if a[i] == '1' else '1')
          carryover = 1 if a[i] == '1' else 0
        
      else:
        if a[i] == '0' and b[i] == '0':
          ans.append('1' if carryover == 1 else '0')
          carryover = 0
        elif a[i] == '1' and b[i] == '1':
          ans.append('1' if carryover == 1 else '0')
          carryover = 1
        else:
          base = '1'
          if carryover == 1:
            ans.append('0')
            carryover = 1
          else:
            ans.append('1')
            carryover = 0
        
      i += 1
        
    if carryover:
      ans.append('1')
      
    ans.reverse()
    return ''.join(ans)
  