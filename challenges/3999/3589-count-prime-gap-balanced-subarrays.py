'''
3589-count-prime-gap-balanced-subarrays
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop


top = 5*10**4
arr = [val for val in range(top+1)]
for v0 in range(2, top+1):
  if arr[v0] < v0:
    continue

  for v1 in range(v0*v0, top+1, v0):
    arr[v1] = v0

primes = set(val for val in arr if val > 1 and arr[val] == val)


class Solution:
  def primeSubarray(self, nums: List[int], k: int) -> int:
    # print('init:', primes)
    count = 0
    j, pdx = 0, 0
    pp = []
    pc = 0
    small = []
    large = []
    c = defaultdict(int)
    n = len(nums)

    for i in range(n):
      # pop last
      if i > 0 and nums[i-1] in primes:
        c[nums[i-1]] -= 1
        pc -= 1

        while small and c[small[0]] == 0:
          heappop(small)

        while large and c[-large[0]] == 0:
          heappop(large)

      # move the right pointer
      while j < n:
        curr = nums[j]
        if curr in primes:
          if small and abs(curr - small[0]) > k:
            break

          if large and abs(curr + large[0]) > k:
            break

          pp.append(j)
          c[curr] += 1
          pc += 1

          # a new value
          if c[curr] == 1:
            heappush(small, curr)
            heappush(large, -curr)

        j += 1  

      if pc > 1:
        while pdx < len(pp) and pp[pdx] < i:
          pdx += 1

        # print('found:', i, j, pp, pdx)
        if pdx+1 < len(pp):
          count += max(0, j - pp[pdx+1])

    return count
