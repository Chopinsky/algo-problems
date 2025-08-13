'''
326-power-of-three
'''


class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    if n < 1:
      return False

    while n > 1:
      if n%3 != 0:
        return False

      n //= 3

    return True
        