'''
3609-minimum-moves-to-reach-target-in-grid
'''


class Solution:
  '''
  moving backwards: from (tx, ty) --> (sx, sy)
  '''
  def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
    if sx == 0 and sy == 0:
      return 0 if tx == 0 and ty == 0 else -1

    res = 0

    while (sx, sy) != (tx, ty):
      if sx > tx or sy > ty:
        return -1

      res += 1
      if tx > ty:
        # must come from (x+x, y)
        if tx > 2*ty:
          if tx % 2 == 1:
            return -1

          tx >>= 1
          continue

        # must come from (x+y, y)
        tx -= ty
        continue

      if tx < ty:
        # must come from (x, y+y)
        if ty > 2*tx:
          if ty % 2 == 1:
            return -1

          ty >>= 1
          continue

        # must come from (x, y+x)
        ty -= tx
        continue

      # tx == ty for all below cases
      if sx == 0:
        tx = 0
        continue

      if sy == 0:
        ty = 0
        continue

      return -1

    return res if (sx, sy) == (tx, ty) else -1
        