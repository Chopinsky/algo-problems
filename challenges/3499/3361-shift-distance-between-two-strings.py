'''
3361-shift-distance-between-two-strings
'''

from typing import List


class Solution:
  def shiftDistance(self, s: str, t: str, nextCost: List[int], prevCost: List[int]) -> int:
    sn = [[0]*26 for _ in range(26)]
    sp = [[0]*26 for _ in range(26)]

    for i in range(26):
      j = (i+1) % 26
      cost = nextCost[i]

      while j != i:
        sn[i][j] = cost
        cost += nextCost[j]
        j += 1
        j %= 26
        
      j = (i-1+26) % 26
      cost = prevCost[i]

      while j != i:
        sp[i][j] = cost
        cost += prevCost[j]
        j -= 1
        j = (j+26)%26

    # print('init:', sn, sp)
    total = 0

    for i in range(len(s)):
      j0 = ord(s[i]) - ord('a')
      j1 = ord(t[i]) - ord('a')
      total += min(sn[j0][j1], sp[j0][j1])

    return total
