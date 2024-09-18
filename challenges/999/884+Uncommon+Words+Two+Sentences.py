'''
884. Uncommon Words from Two Sentences
'''

from collections import Counter
from typing import List

class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    w1 = Counter(s1.split(' '))
    w2 = Counter(s2.split(' '))
    res = []
    
    for w in w1 + w2:
      c = w1.get(w, 0) + w2.get(w, 0)
      if c == 1:
        res.append(w)
    
    return res
        