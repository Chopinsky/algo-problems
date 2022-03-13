'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
'''


class Solution:
  def getSum(self, a: int, b: int) -> int:
    ans = 0
    co = 0
    
    for i in range(16):
      val = ((a>>i) & 1) + ((b>>i) & 1) + co
      val, co = val % 2, val // 2
        
      if val == 1:
        ans |= 1 << i
        
      # print(i, val)
    
    if (ans>>15) & 1 == 1:
      res = 0
      for i in range(16):
        if (ans>>i) & 1 == 0:
          res |= 1 << i
        
      ans = 0
      co = 1
      for i in range(16):
        val = ((res>>i) & 1) + co
        val, co = val % 2, val // 2
        
        if val == 1:
          ans |= 1 << i
        
      ans = -ans
      
    return ans
  