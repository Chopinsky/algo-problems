'''
3640-trionic-array-ii
'''

from typing import List
import math


class Solution:
  def maxSumTrionic(self, nums: List[int]) -> int:
    n = len(nums)
    if n < 4:
      return 0

    cand = []

    def handle_up(i: int):
      if i >= n-1:
        return 1

      l = i
      r = i+1
      curr = nums[l] + nums[r]
      p = curr

      # scan to the right
      while r+1 < n and nums[r+1] > nums[r]:
        r += 1
        curr += nums[r]

        # find the max prefix
        p = max(p, curr)

      ll = r-1
      curr = nums[ll] + nums[r]
      s = curr

      # scan to the left
      while ll-1 >= i and nums[ll-1] < nums[ll]:
        ll -= 1
        curr += nums[ll]

        # find the max suffix
        s = max(s, curr)

      cand.append({
        "arr": "up",
        "rng": [l, r],
        "prefix": p,
        "suffix": s,
      })

      return r-l

    def handle_down(i: int):
      if i >= n-1:
        return 1

      l = i
      r = i+1
      curr = nums[l] + nums[r]

      while r+1 < n and nums[r] > nums[r+1]:
        r += 1
        curr += nums[r]

      cand.append({
        "arr": "down",
        "rng": [l, r],
        "prefix": curr,
        "suffix": curr,
      })

      return r-l

    idx = 0
    while idx < n-1:
      v0 = nums[idx+1]
      v1 = nums[idx]

      if v0 == v1:
        idx += 1
        continue

      if v0 < v1:
        idx += handle_down(idx)
      else:
        idx += handle_up(idx)

    # print('done:', cand)
    res = -math.inf
    nn = len(cand)

    for idx in range(nn):
      mid = cand[idx]
      if mid['arr'] == 'up':
        continue

      if idx == 0 or idx == nn-1:
        continue

      prev = cand[idx-1]
      if prev['arr'] != 'up' or prev['rng'][1] != mid['rng'][0]:
        continue

      nxt = cand[idx+1]
      if nxt['arr'] != 'up' or mid['rng'][1] != nxt['rng'][0]:
        continue
      
      # left and right index values are double counted
      l, r = mid['rng']
      val = prev['suffix'] + mid['prefix'] + nxt['prefix'] - nums[l] - nums[r]

      # update the result
      res = max(res, val)

    return res

  def maxSumTrionic(self, nums: List[int]) -> int:
    n = len(nums)
    res = -math.inf
    prefix = nums[0]
    l = 0
    p = 0
    q = 0

    for r in range(1, n):
      prefix += nums[r]

      # reset
      if nums[r-1] == nums[r]:
        l = r
        prefix = nums[r]
        continue

      if nums[r-1] > nums[r]:
        # flip
        if r > 1 and nums[r-2] < nums[r-1]:
          p = r-1
          while l < q:
            prefix -= nums[l]
            l += 1

          while l+1 < p and nums[l] < 0:
            prefix -= nums[l]
            l += 1

        continue

      if r > 1 and nums[r-2] > nums[r-1]:
        q = r-1

      if l < p and p < q:
        res = max(res, prefix)

    return res

