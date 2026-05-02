'''
2078-two-furthest-houses-with-different-colors
'''

from typing import List


class Solution:
  def maxDistance(self, colors: List[int]) -> int:
    c1 = []
    n = len(colors)
    dist = 0

    for i in range(n-1, -1, -1):
      c = colors[i]

      if not c1:
        c1.append((c, i))
        continue

      if c != c1[-1][0]:
        c1.append((c, i))
        break

    for i in range(n):
      c = colors[i]

      if c == c1[0][0]:
        dist = max(dist, abs(i - c1[1][1]))
      else:
        dist = max(dist, abs(i - c1[0][1]))
        
    return dist
