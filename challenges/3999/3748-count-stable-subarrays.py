'''
3748-count-stable-subarrays
'''

from typing import List
from bisect import bisect_left, bisect_right
from math import comb


class Solution:
  def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    idx = []
    accu = [0]*n
    cnt = 0
    ans = []

    for i in range(n):
      # restart the count
      if i == 0 or nums[i] < nums[i-1]:
        cnt = 0
        idx.append(i)

      cnt += 1
      accu[i] = cnt + (accu[i-1] if i > 0 else 0)

    def get_sub_cnt(ln: int) -> int:
      if ln <= 0:
        return 0

      return 1 if ln == 1 else (comb(ln, 2) + ln)

    debug = False
    if debug:
      print('init:', idx, accu)
    sz = len(idx)

    for l, r in queries:
      if l == r:
        ans.append(1)
        continue

      ldx = bisect_left(idx, l)
      rdx = bisect_right(idx, r)
      sub_cnt = 0
      if debug:
        print('q:', (l, r), sz, (ldx, rdx))
      
      # case 1: the [l, r] is an increasing subarray
      if ldx >= sz or idx[ldx] > r or (idx[ldx] <= l and rdx == ldx+1):
        sub_cnt = get_sub_cnt(r-l+1)
        if debug:
          print('case1:', sub_cnt)

      # calc left, mid, right and sum together
      else:
        # left cnt:
        c_left = get_sub_cnt(idx[ldx]-l)

        # mid cnt:
        rcnt = accu[idx[rdx-1]-1]
        lcnt = accu[idx[ldx]-1] if idx[ldx] > 0 else 0
        c_mid = rcnt - lcnt

        # right cnt:
        c_right = get_sub_cnt(r-idx[rdx-1]+1)

        # add together
        sub_cnt = c_left + c_mid + c_right
        if debug:
          print('case2:', sub_cnt, (c_left, c_mid, c_right))

      ans.append(sub_cnt)

    return ans
        