'''
717-1-bit-and-2-bit-characters
'''

from typing import List


class Solution:
  def isOneBitCharacter(self, bits: List[int]) -> bool:
    n = len(bits)
    i = 0

    while i < n:
      if i == n-1:
        return True

      if i == n-2:
        return bits[i] == 0

      if bits[i] == 0:
        i += 1
      else:
        i += 2

    return True
