'''
4063-longest-subarray-divisible-by-k-with-at-most-one-negation-i
'''


class Solution:
  def longestSubarray(self, nums: list[int], k: int) -> int:
    pf = {}
    n = len(nums)
    pval = 0
    debug = False

    for i, val in enumerate(nums):
      pval = (pval + val) % k
      pf[pval] = i

    prev = {0:-1}
    pval = 0
    ln = 0
    if debug:
      print('init:', pf)

    for i, val in enumerate(nums):
      pval = (pval + val) % k
      t0 = (k - pval) % k
      if debug:
        print('iter:', (i, val), pval, prev)

      if pval in prev:
        ln = max(ln, i-prev[pval])
        # print('1:', (prev[pval], i))

      # find subarr if we exclude value at i 
      lval = 0
      for j in range(i, -1, -1):
        # left side sums
        lval = (lval + nums[j]*(-1 if j == i else 1)) % k
        if lval == 0:
          ln = max(ln, i-j+1)

        t0 = (k - lval) % k  # what we need from the right side
        t1 = (pval + t0) % k # prefix for the right side tail
        if debug:
          print('inner:', (j, lval), t0, t1)

        if t1 in pf and pf[t1] > i:
          ln = max(ln, pf[t1]-j+1)
          # print('2:', (j, pf[t1]))

      # adding the first appearance of pval to prefix
      if pval not in prev:
        prev[pval] = i

    return ln
    