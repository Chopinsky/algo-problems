'''
3345-smallest-divisible-digit-product-i
'''


class Solution:
  def smallestNumber(self, n: int, t: int) -> int:
    def is_ok(val: int) -> int:
      if t == 1:
        return True

      res = 1
      for d in str(val):
        res = res * int(d)

      return res%t == 0

    res = n
    while not is_ok(res):
      res += 1

    return res
        