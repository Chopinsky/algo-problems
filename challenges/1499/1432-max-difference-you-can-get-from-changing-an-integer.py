'''
1432-max-difference-you-can-get-from-changing-an-integer
'''


class Solution:
  def maxDiff(self, num: int) -> int:
    head = int(str(num)[0])

    def update(a: int, b: int):
      base = 0
      curr = num
      tens = 1

      while curr > 0:
        digit = curr % 10
        if digit == a:
          base += b * tens
        else:
          base += tens * digit

        curr //= 10
        tens *= 10

      return base

    high = num
    low = num

    for v0 in range(10):
      for v1 in range(10):
        if v0 == v1:
          continue

        if v0 == head and v1 == 0:
          continue

        v2 = update(v0, v1)
        if v2 == num:
          continue
          
        # print('iter:', v2)
        high = max(high, v2)
        low = min(low, v2)

    return high - low
