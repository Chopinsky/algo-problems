'''
1317-convert-integer-to-the-sum-of-two-no-zero-integers
'''

from typing import List


class Solution:
  def getNoZeroIntegers(self, n: int) -> List[int]:
    def contains_zero(val: int) -> bool:
      while val > 0:
        if val%10 == 0:
          # print('val:', val)
          return True

        val //= 10

      return False
    
    for v0 in range(1, n//2+1):
      if contains_zero(v0):
        # print('v0:', v0)
        continue

      v1 = n-v0
      if contains_zero(v1):
        # print('v1:', v1)
        continue

      return [v0, v1]

    return []

