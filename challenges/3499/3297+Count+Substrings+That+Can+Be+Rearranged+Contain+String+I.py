'''
3297. Count Substrings That Can Be Rearranged to Contain a String I
'''

from typing import Dict
from collections import defaultdict, Counter


class Solution:
  def validSubstringCount(self, word1: str, word2: str) -> int:
    i, j = 0, 0
    count = 0
    c = Counter(word2)
    n1, n2 = len(word1), len(word2)
    
    def is_match(d1: Dict, d2: Dict):
      for ch in d2:
        if ch not in d1 or d1[ch] < d2[ch]:
          return False
      
      return True
    
    d = defaultdict(int)
    
    while i+n2 <= n1:
      while j < n1 and not is_match(d, c):
        ch = word1[j]
        d[ch] += 1
        j += 1
      
      if is_match(d, c):
        count += n1-j+1
        # print('matched:', (i, j, word1[i:j]), n1-j+1)
        
      ch = word1[i]
      d[ch] -= 1
      i += 1
      
    return count
  