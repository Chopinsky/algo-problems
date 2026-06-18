'''
3896-minimum-operations-to-transform-array-into-alternating-prime
'''

from bisect import bisect_left


mx = 2*10**5 + 1
siev = [val for val in range(mx)]
primes = list()

for v0 in range(2, mx):
  if siev[v0] < v0:
    continue

  primes.append(v0)
  for v1 in range(v0*v0, mx, v0):
    siev[v1] = v0


class Solution:
  def minOperations(self, nums: list[int]) -> int:
    # print('p:', primes)
    ops = 0

    def dist(val: int) -> int:
      idx = bisect_left(primes, val)
      if idx >= len(primes):
        return val - primes[-1]

      return primes[idx]-val

    for i in range(len(nums)):
      d = dist(nums[i])
      # print('iter:', nums[i], d)

      if i%2 == 0:
        if d > 0:
          ops += d
      else:
        if d == 0:
          ops += 2 if nums[i] == 2 else 1

    return ops
        