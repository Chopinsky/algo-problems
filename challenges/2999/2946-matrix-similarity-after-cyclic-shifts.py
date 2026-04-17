'''
2946-matrix-similarity-after-cyclic-shifts
'''

from typing import List


class Solution:
  def areSimilar(self, mat: List[List[int]], k: int) -> bool:
    n = len(mat[0])
    k %= n

    if k == 0:
      return True

    def shift(row: list[int], to_right: bool) -> bool:
      if to_right:
        nxt = row[n-k:] + row[:n-k]
      else:
        nxt = row[k:] + row[:k]

      return all(v0 == v1 for v0, v1 in zip(row, nxt))

    shift_to_right = False

    for row in mat:
      if not shift(row, shift_to_right):
        return False

      shift_to_right = not shift_to_right

    return True
        