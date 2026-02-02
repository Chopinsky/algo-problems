'''
3147-taking-maximum-energy-from-the-mystic-dungeon
'''

from typing import List


class Solution:
  def maximumEnergy(self, energy: List[int], k: int) -> int:
    low = [0]*k
    curr = [0]*k
    n = len(energy)

    for i in range(n):
      j = i%k
      nxt = curr[j]+energy[i]

      if i+k < n:
        low[j] = min(low[j], nxt)

      curr[j] = nxt

    # print('done:', curr, low)
    return max(val-low_val for val, low_val in zip(curr, low))
        