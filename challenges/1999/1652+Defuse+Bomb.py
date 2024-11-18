'''
1652. Defuse the Bomb
'''

from typing import List


class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    n = len(code)
    ans = [0]*n
    
    if k == 0:
      return ans
    
    code += code
    if k > 0:
      suffix = sum(code[n:n+k])
      ans[n-1] = suffix
      for i in range(n-2, -1, -1):
        suffix += code[i+1] - code[i+k+1]
        ans[i] = suffix
        
    else:
      k *= -1
      prefix = sum(code[n-k:n])
      ans[0] = prefix
      for i in range(n+1, 2*n):
        prefix += code[i-1] - code[i-k-1]
        ans[i-n] = prefix
      
    return ans
        