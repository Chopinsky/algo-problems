'''
3298. Count Substrings That Can Be Rearranged to Contain a String II
'''

from collections import Counter, defaultdict


class Solution:
  def validSubstringCount(self, word1: str, word2: str) -> int:
    c2 = Counter(word2)
    c1 = defaultdict(int)
    count = 0
    meet = set()
    i, j = 0, 0
    n1 = len(word1)
    n2 = len(word2)
    ln = len(c2)
    
    while i <= n1-n2:
      while j < n1 and len(meet) < ln:
        ch = word1[j]
        if ch in c2:
          c1[ch] += 1
          if c1[ch] >= c2[ch]:
            meet.add(ch)

        j += 1
      
      if len(meet) == ln:
        count += n1-j+1
        # print('update:', (i, j))
      
      ch = word1[i]
      if ch in c2:
        c1[ch] -= 1
        if c1[ch] < c2[ch]:
          meet.discard(ch)
        
      i += 1
    
    return count
        