'''
3629-minimum-jumps-to-reach-end-via-prime-teleportation
'''

from collections import defaultdict
from typing import List


top = 10**6 + 1
vals = [val for val in range(top)]
p = []

for v0 in range(2, top):
  if vals[v0] < v0:
    continue

  p.append(v0)
  for v1 in range(v0*v0, top, v0):
    vals[v1] = v0

ps = set(p)


class Solution:
  def minJumps(self, nums: List[int]) -> int:
    n = len(nums)
    tv = max(nums)
    pos = defaultdict(list)

    for i, val in enumerate(nums):
      pos[val].append(i)

    # print('init:', jumps)
    s = 0
    visited = set()
    used = set()
    curr, nxt = set([0]), set()

    while n-1 not in curr:
      visited |= curr
      s += 1

      for i in curr:
        if i-1 >= 0 and i-1 not in visited:
          nxt.add(i-1)

        if i+1 < n and i+1 not in visited:
          nxt.add(i+1)

        val = nums[i]
        if val not in ps or val in used:
          continue

        used.add(val)
        for v1 in range(val, tv+1, val):
          for j in pos[v1]:
            if j in visited or j in nxt:
              continue

            nxt.add(j)

      curr, nxt = nxt, curr
      nxt.clear()
      # print('jump:', s, curr)

    return s
