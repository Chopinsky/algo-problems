'''
4033-valid-k-unique-subarrays-i
'''

from math import isqrt


class Solution:
  def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
    n, nq = len(nums), len(queries)
    block_size = max(1, isqrt(n))
    res = [False] * nq

    # Group query by block size, then shrink and expand in each block to minimize the ops
    q = [(l, r, i) for i, (l, r) in enumerate(queries)]
    q.sort(key=lambda x: (x[0]//block_size, x[1] if (x[0]//block_size)%2 == 0 else -x[1]))

    freq = {}
    odd_freq = set()

    # add nums[i] to the subarray freq/odd_freq
    def add(i: int):
      nonlocal freq, odd_freq

      val = nums[i]
      freq[val] = 1 + (freq[val] if val in freq else 0)

      if val in odd_freq:
        odd_freq.remove(val)
      else:
        odd_freq.add(val)

    # remove nums[i] from the subarray freq/odd_freq
    def remove(i: int):
      nonlocal freq, odd_freq

      val = nums[i]
      freq[val] -= 1
      if not freq[val]:
        del freq[val]

      if val in odd_freq:
        odd_freq.remove(val)
      else:
        odd_freq.add(val)

    l, r = 0, -1

    # apply mo's algo along the sorted queries
    for start, end, i in q:
      while l > start:
        l -= 1
        add(l)

      while r < end:
        r += 1
        add(r)

      while l < start:
        remove(l)
        l += 1

      while r > end:
        remove(r)
        r -= 1

      res[i] = len(freq) == k and len(odd_freq) == 0

    return res
