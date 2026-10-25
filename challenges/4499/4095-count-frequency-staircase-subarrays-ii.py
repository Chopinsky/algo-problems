'''
4095-count-frequency-staircase-subarrays-ii
'''

from collections import defaultdict


class Solution:
  def countStaircase(self, nums: list[int]) -> int:
    n = len(nums)
    idx = [0] * n
    pos = defaultdict(list)
    cnt = 0

    for i, val in enumerate(nums):
      idx[i] = len(pos[val])
      pos[val].append(i)

    for i in range(n):
      seen = set()
      l = i    # subarr lower-bound
      r = n-1  # count-required upper-bound

      for j in range(i, n):
        # out of the longest subarr bound
        if j > r:
          break

        val = nums[j]
        if val in seen:
          continue

        seen.add(val)
        cand = pos[val]
        # count of val in this subarr
        k = len(seen) 
        
        # target index in cand
        tgt = idx[j]+k-1
        if tgt >= len(cand):
          # not enough left
          break

        # update with new lower and upper bounds
        l2 = cand[tgt]
        r2 = cand[tgt+1] if tgt+1 < len(cand) else n-1
        l = max(l, l2)
        r = min(r, r2)

        if l > r:
          break

        # the subarr end falls between the lower and upper bounds
        if l <= i + k*(k+1)//2 - 1 <= r:
          cnt += 1

    return cnt
        