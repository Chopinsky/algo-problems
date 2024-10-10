'''
3302. Find the Lexicographically Smallest Valid Sequence

Test cases:

"vbcca"
"abc"
"bacdc"
"abc"
"aaaaaa"
"aaabc"
"abc"
"ab"
"ccbccccbcc"
"b"
"ghhgghhhhhh"
"gg"
"effgiihrhhagiie"
"ihihh"
"lmlmmmmlmll"
"ll"
'''

from typing import List


class Solution:
  def validSequence(self, word1: str, word2: str) -> List[int]:
    n1 = len(word1)
    n2 = len(word2)
    if n2 <= 1:
      return [0]
    
    i2 = n2-1
    suffix = []
    
    for i1 in range(n1-1, -1, -1):
      if i2 >= 0 and word1[i1] == word2[i2]:
        i2 -= 1

      suffix.append(n2-1-i2)
    
    suffix = suffix[::-1]
    prefix = []
    # print('suffix:', suffix, (n1, n2), len(suffix))
    
    def add_rest(i1: int, i2: int) -> List[int]:
      idx = []
    
      while i1 < n1 and i2 < n2:
        if word1[i1] == word2[i2]:
          idx.append(i1)
          i2 += 1
          
        i1 += 1
        
      # print('rest:', (i1, i2), idx)
      return idx
      
    i2 = 0
    for i1 in range(n1):
      if word1[i1] == word2[i2]:
        prefix.append(i1)
        i2 += 1
        
      elif i1+1 < n1 and len(prefix)+1+suffix[i1+1] >= n2:
        prefix.append(i1)
        prefix += add_rest(i1+1, i2+1)
        # print('add rest?')
      
      # print('iter:', (i1, i2), prefix)
      
      curr = len(prefix)
      if curr == n2:
        break
        
      if curr+1 == n2 and i1 != (prefix[-1] if prefix else None):
        prefix.append(i1)
        break
      
    return prefix if len(prefix) == n2 else []
    