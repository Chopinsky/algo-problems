'''
3307. Find the K-th Character in String Game II
'''

from typing import List

class Solution:
  def kthCharacter(self, k: int, ops: List[int]) -> str:
    if k == 1:
      return "a"
    
    ln = 1
    shift = 0
    idx = 0
    
    while ln < k:
      ln <<= 1
      idx += 1
    
    # print('init:', ln, idx, ops[:ln+1])
    idx -= 1
    
    while k > 1:
      nxt = ln >> 1
      offset = ln-k
      if offset < nxt:
        k = nxt - offset
        shift = (shift+ops[idx])%26
        
      ln = nxt
      idx -= 1
    
    return chr(ord('a') + shift)
      