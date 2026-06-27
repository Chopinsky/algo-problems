'''
3899-angles-of-a-triangle
'''

from math import acos, degrees


class Solution:
  def internalAngles(self, sides: list[int]) -> list[float]:
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
      return []

    a, b, c = sides
    a0 = acos((b**2 + c**2 - a**2) / (2*b*c))
    a1 = acos((a**2 + c**2 - b**2) / (2*a*c))
    a2 = acos((a**2 + b**2 - c**2) / (2*a*b))

    return sorted([degrees(a0), degrees(a1), degrees(a2)])
        