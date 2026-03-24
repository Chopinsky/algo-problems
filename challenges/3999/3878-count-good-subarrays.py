'''
3878-count-good-subarrays
'''


class Solution:
  def countGoodSubarrays(self, nums: list[int]) -> int:
    n = len(nums)
    prev = [-1]*31
    nxt = [n]*31

    l = [0]*n
    r = [n-1]*n

    for i in range(n):
      for bit in range(31):
        if nums[i] & (1<<bit) == 0:
          l[i] = max(l[i], prev[bit]+1)
        else:
          prev[bit] = i

    for i in range(n-1, -1, -1):
      for bit in range(31):
        if nums[i] & (1<<bit) == 0:
          r[i] = min(r[i], nxt[bit]-1)
        else:
          nxt[bit] = i

    ans = 0
    last = {}

    for i in range(n):
      ldx, rdx = l[i], r[i]
      val = nums[i]

      if nums[i] in last:
        ldx = max(ldx, last[val]+1)

      last[val] = i
      ans += (i-ldx+1) * (rdx-i+1)

    return ans
        