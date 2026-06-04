'''
2126-destroying-asteroids
'''

from typing import List


class Solution:
  def asteroidsDestroyed(self, mass: int, a: List[int]) -> bool:
    if not a:
      return True

    a.sort()
    if mass < a[0]:
      return False 

    a[0] += mass
    for i in range(1, len(a)):
      if a[i] > a[i-1]:
        return False

      a[i] += a[i-1]

    return True
        