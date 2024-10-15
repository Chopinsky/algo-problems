'''
3223. Minimum Length of String After Operations
'''

from collections import defaultdict


class Solution:
  def minimumLength(self, s: str) -> int:
    c = defaultdict(int)
    for ch in s:
      c[ch] += 1
      
    # print('init:', c)
    ln = 0
    
    for n in c.values():
      if n <= 2:
        ln += n
        continue
        
      if n % 2 == 0:
        ln += 2
      else:
        ln += 1
    
    return ln
        