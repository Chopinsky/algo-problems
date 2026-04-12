'''
3901-good-subsequence-queries
'''

from math import isqrt
from collections import defaultdict


top = 5*10**4
factors = [None for _ in range(top+1)]

for v0 in range(2, top+1):
  f = set()
  idx = v0

  # Handle the number of 2s that divide n
  while v0 % 2 == 0:
    f.add(2)
    v0 //= 2
      
  # n must be odd at this point. So we can skip one element (Note i = i + 2)
  for i in range(3, isqrt(v0)+1, 2):
    # while i divides n, append i and divide n
    while v0 % i == 0:
      f.add(i)
      v0 //= i
          
  # Condition if n is a prime number greater than 2
  if v0 > 2:
    f.add(v0)

  factors[idx] = list(f)


class Solution:
  def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
    n = len(nums)
    if n <= 1:
      return 0

    # print('init:', factors)
    # count of active numbers divisible by prime factor
    pf = defaultdict(int)
    # frequency of counts of active numbers divisible by prime factors,
    # used to check if all active numbers are divisible by some prime factor
    ff = defaultdict(int)
    # count of active numbers
    act = 0
    cnt = 0
    
    def mod(v: int, d: int):
      nonlocal act

      if v%p > 0:
        return

      act += d
      for fval in (factors[v//p] or []):
        ff[pf[fval]] -= 1
        pf[fval] += d
        ff[pf[fval]] += 1

    def check() -> bool:
      # no active numbers, or some prime factor
      # can divide all active numbers, hence 
      # gcd(seq) > q
      if not act or ff[act] > 0:
        return False

      if act < n or n >= 7:
        return True

      # try remove 1 elem from the array and 
      # test if the seq is good
      for i in range(n):
        mod(nums[i], -1)
        ok = (ff[act] == 0)
        mod(nums[i], 1)

        if ok:
          return True

      return False

    for val in nums:
      mod(val, 1)

    for i, val in queries:
      # remove old val
      mod(nums[i], -1)

      # update to the new val
      nums[i] = val
      mod(nums[i], 1)

      if check():
        cnt += 1

    return cnt
        