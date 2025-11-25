'''
3757-number-of-effective-subsequences
'''

from typing import List


class Solution:
  def countEffective(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    n = len(nums)

    total = 0
    for v in nums:
      total |= v

    if total == 0:
      return 0

    bits = []
    for b in range(20):
      if (total>>b) & 1:
        bits.append(b)

    k = len(bits)
    full_mask = (1<<k) - 1
    freq = [0] * (1<<k)

    for v in nums:
      mask = 0
      for i, bit in enumerate(bits):
        if (v>>bit) & 1:
          mask |= 1 << i

      freq[mask] += 1

    f = freq[:]

    # f[mask] = sum of freq[submask]
    for i in range(k):
      for mask in range(1<<k):
        if mask & (1<<i):
          f[mask] += f[mask ^ (1<<i)]

    p2 = [1] * (n+1)
    for i in range(1, n+1):
      p2[i] = (p2[i-1]*2) % mod

    ans = 0
    for bmask in range(1, 1<<k):
      complement = full_mask ^ bmask
      missing_count = f[complement]
      add_value = p2[missing_count]

      if bin(bmask).count('1') % 2 == 1:
        ans = (ans + add_value) % mod
      else:
        ans = (ans - add_value) % mod

    return ans % mod
    