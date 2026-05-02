'''
788-rotated-digits
'''

from bisect import bisect_right


valid = list()

mapping = {
  0: 0,
  1: 1,
  2: 5,
  5: 2,
  6: 9,
  8: 8,
  9: 6,
}

def is_valid(val: int) -> bool:
  v1 = ""

  for ch in str(val):
    v0 = int(ch)
    if v0 not in mapping:
      return False

    v1 += str(mapping[v0])

  return val != int(v1)

for val in range(1, 10001):
  if is_valid(val):
    valid.append(val)


class Solution:
  def rotatedDigits(self, n: int) -> int:
    # print('test:', valid)
    return bisect_right(valid, n)
        