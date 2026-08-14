'''
3776-minimum-moves-to-balance-circular-array
'''

from typing import List


class Solution:
  def minMoves(self, balance: List[int]) -> int:
    if all(b >= 0 for b in balance):
      return 0

    if sum(balance) < 0:
      return -1

    n = len(balance)
    neg_idx = -1
    neg_bal = 0
    moves = 0

    for i in range(n):
      if balance[i] < 0:
        neg_idx = i
        neg_bal = balance[i]
        break

    l, r = (neg_idx-1)%n, (neg_idx+1)%n
    # print('init:', l, r)

    while neg_bal < 0:
      dist = min(abs(r-neg_idx), abs(neg_idx-l))
      offset = min(-neg_bal, balance[l]+balance[r])
      moves += dist * offset
      neg_bal += offset
      # print('iter:', (l, r), dist, offset, neg_bal, moves)

      l = (l-1) % n
      r = (r+1) % n

    return moves
