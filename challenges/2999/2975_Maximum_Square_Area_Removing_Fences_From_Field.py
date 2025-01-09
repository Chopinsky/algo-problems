'''
2975. Maximum Square Area by Removing Fences From a Field
'''

from typing import List


class Solution:
  def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    mod = 10**9 + 7
    vf = [1] + sorted(vFences) + [n]
    hf = [1] + sorted(hFences) + [m]
    v_side = set()
    lv = len(vf)
    lh = len(hf)

    for i in range(lv-1):
      for j in range(i+1, lv):
        v_side.add(vf[j]-vf[i])

    # print('init:', v_side, hf)
    area = -1

    for i in range(lh-1):
      for j in range(i+1, lh):
        h_side = hf[j] - hf[i]
        # print('iter:', h_side, hf[j], hf[i])

        if h_side in v_side:
          area = max(area, h_side**2)

    return area % mod if area > 0 else area
