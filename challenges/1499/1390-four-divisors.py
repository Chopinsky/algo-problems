'''
1390-four-divisors
'''

from math import isqrt


vals = {}

def find_sum(val: int):
  if val <= 5:
    return -1

  cand = []
  for v0 in range(isqrt(val)):
    v0 += 1
    if val%v0 == 0:
      if v0*v0 == val:
        cand.append(v0)
      else:
        cand.append(v0)
        cand.append(val//v0)

    if len(cand) > 4:
      break

  return -1 if len(cand) != 4 else sum(cand)


for val in range(10**5):
  val += 1
  res = find_sum(val)
  if res > 0:
    vals[val] = res


class Solution:
  def sumFourDivisors(self, nums: list[int]) -> int:
    # print('init:', vals)
    total = 0

    for num in nums:
      if num in vals:
        total += vals[num]

    return total
        