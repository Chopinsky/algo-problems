'''
1234. Replace the Substring for Balanced String
'''

from collections import Counter, defaultdict


class Solution:
  def balancedString(self, s: str) -> int:
    j = 0
    total = Counter(s)
    n = len(s)
    tgt = n//4
    
    if all(cnt <= tgt for cnt in total.values()):
      return 0
    
    curr = defaultdict(int)
    long = n-1
    
    def check() -> bool:
      for ch, cnt in total.items():
        rem = cnt - curr[ch]
        if rem > tgt:
          return False
        
      return True
    
    for i in range(n):
      if i > 0:
        ch = s[i-1]
        curr[ch] -= 1
        
      while j < n and not check():
        ch = s[j]
        curr[ch] += 1
        j += 1
        
      # print('iter:', (i, j), curr)
      if check():
        long = min(long, j-i)
        
    return long
    
        