'''
1769. Minimum Number of Operations to Move All Balls to Each Box
'''

from typing import List


class Solution:
  def minOperations(self, boxes: str) -> List[int]:
    n = len(boxes)
    count = [0]*n
    prefix = [0]*n
    
    for i in range(n):
      pc = count[i-1] if i > 0 else 0
      pp = prefix[i-1] if i > 0 else 0
      count[i] = pc + (1 if boxes[i] == '1' else 0)
      prefix[i] = pp + (i if boxes[i] == '1' else 0)
    
    # print('init:', count, prefix)
    ops = [0] * n
    
    for i in range(n):
      lc = count[i-1] if i > 0 else 0
      lp = prefix[i-1] if i > 0 else 0
      lmoves = lc*i - lp
      
      rc = count[-1] - count[i]
      rp = prefix[-1] - prefix[i]
      rmoves = rp - rc*i
      
      # print('moves:', lmoves, rmoves)
      ops[i] = lmoves + rmoves
      
    return ops
  