'''
3223. Minimum Length of String After Operations
'''

from collections import defaultdict, Counter


class Solution:
  def minimumLength(self, s: str) -> int:
    pos = Counter(s)
    # print('init:', pos)

    return sum(1 if val%2 == 1 else 2 for val in pos.values())
        
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
        