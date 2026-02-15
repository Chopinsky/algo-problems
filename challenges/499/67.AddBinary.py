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
    res = ""
    a = list(int(ch) for ch in a)
    b = list(int(ch) for ch in b)
    carryover = 0

    print('init:', a, b)
    if len(a) < len(b):
      a, b = b, a

    while a or b:
      d0 = a.pop() if a else 0
      d1 = b.pop() if b else 0
      d = d0 + d1 + carryover

      carryover = 0 if d < 2 else 1
      res = str(d%2) + res

    return res if carryover == 0 else "1"+res
        
  def addBinary(self, a: str, b: str) -> str:
    carryover = 0
    res = ''
    i, j = len(a)-1, len(b)-1
    
    while i >= 0 or j >= 0:
      va = int(a[i]) if i >= 0 else 0
      vb = int(b[j]) if j >= 0 else 0
      vc = va + vb + carryover
      
      res = str(vc % 2) + res
      carryover = vc // 2
      
      i -= 1
      j -= 1
      
    if carryover > 0:
      res = '1' + res
      
    return res
    


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
  