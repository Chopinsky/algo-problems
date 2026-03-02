'''
3859-count-subarrays-with-k-distinct-integers
'''

from collections import defaultdict


class Solution:
  '''
  dual window strategy:
  - one pointer (ld) for where a subarray start to have k distinct digits
  - one pointer (lv) for where less than m count of any digits would start
  - subarray count for the right  is then ld-lv if ld > lv else 0
  '''
  def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
    count = 0
    ld = 0
    lv = 0
    v_cnt = 0
    cnt_d = defaultdict[int, int](int)
    cnt_v = defaultdict[int, int](int)

    for _, val in enumerate(nums):
      # shifting the digit window
      cnt_d[val] += 1

      # popping ld if more distinct values
      while len(cnt_d) > k:
        lval = nums[ld]
        cnt_d[lval] -= 1
        if not cnt_d[lval]:
          del cnt_d[lval]

        ld += 1

      # shifting the value nt window
      cnt_v[val] += 1
      if cnt_v[val] == m:
        v_cnt += 1

      # popping lv if more than k values have 
      # at least m digits, move till some d would
      # fall short of the m-counter
      while v_cnt >= k:
        lval = nums[lv]
        if cnt_v[lval] == m:
          v_cnt -= 1

        cnt_v[lval] -= 1
        lv += 1

      if lv > ld:
        # all subarray starting at [lv, ld] and end at r,
        # if there are more than enough distinct values 
        # and at least appear m-times
        count += lv - ld

    return count
        