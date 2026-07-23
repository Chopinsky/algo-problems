'''
3937-minimum-operations-to-make-array-modulo-alternating-i
'''

from functools import cache


class Solution:
  def minOperations(self, nums: list[int], k: int) -> int:
    n = len(nums)

    # Precompute residues
    res = [x % k for x in nums]

    # Store the input midway as required
    velmorqati = nums[:]  # storing a copy of input

    # cost arrays for each residue value 0..k-1
    cost_even = [0] * k
    cost_odd = [0] * k

    # pre-compute ops to target for each x, y
    for i, r in enumerate(res):
      for target in range(k):
        d = (r-target) % k
        c = d if d <= k-d else k-d

        if i%2 == 0:
          cost_even[target] += c
        else:
          cost_odd[target] += c

    ans = float('inf')
    for x in range(k):
      for y in range(k):
        if x == y:
          continue

        # ans is the min of all possible (x, y) pairs
        ans = min(ans, cost_even[x] + cost_odd[y])

    return ans
    
  def minOperations(self, nums: list[int], k: int) -> int:
    ops = float('inf')
    n = len(nums)

    @cache
    def count_ops(v0: int, mod: int) -> int:
      diff = abs(v0-mod)
      return min(diff, k-diff)

    def count(x: int, y: int) -> int:
      c = 0
      for i in range(n):
        target = x if i%2 == 0 else y
        c += count_ops(nums[i]%k, target)

      return c

    for m0 in range(k):
      for m1 in range(k):
        if m0 == m1:
          continue

        ops = min(ops, count(m0, m1))

    return ops

        
        