'''
3479-fruits-into-baskets-iii
'''

from typing import List


class Solution:
  def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
    n = len(baskets)
    tree = [0 for _ in range(4*n)]

    def insert(idx: int, l: int, r: int, pos: int, val: int):
      if l == r:
        tree[idx] = val
        return

      mid = (l + r) // 2
      ldx = 2*idx + 1
      rdx = ldx + 1

      if pos <= mid:
        insert(ldx, l, mid, pos, val)
      else:
        insert(rdx, mid+1, r, pos, val)

      tree[idx] = max(tree[ldx], tree[rdx])

    def update(idx: int, l: int, r: int, val: int):
      if val > tree[idx]:
        return False

      if l == r:
        if val <= tree[idx]:
          # print('update:', idx, l)
          tree[idx] = 0
          return True

        return False

      mid = (l + r) // 2
      ldx = 2*idx + 1
      rdx = ldx + 1

      if val <= tree[ldx]:
        # go to the left branch
        res = update(ldx, l, mid, val)
      else:
        # go to the right branch
        res = update(rdx, mid+1, r, val)

      if res:
        # subtree updated
        tree[idx] = max(tree[ldx], tree[rdx])

      return True

    for pos, val in enumerate(baskets):
      insert(0, 0, n, pos, val)

    # print('init:', tree)
    count = 0

    for f in fruits:
      if not update(0, 0, n, f):
        # print('left:', f, tree)
        count += 1

    return count
        