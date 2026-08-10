'''
4017-peaks-in-array-ii
'''


class Solution:
  def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
    n = len(nums)
    c = [0]*(n+2)
    gap = [0]*(n+2)
    peak = [0]*n

    def update(a: list[int], i: int, d: int):
      while i <= n:
        a[i] += d
        i += i & -i

    def query(a: list[int], i: int) -> int:
      res = 0
      while i > 0:
        res += a[i]
        i -= i & -i

      return res

    def kth(a: list[int], k: int) -> int:
      idx = 0
      mask = 1 << (n.bit_length() - 1)

      while mask:
        nxt = idx + mask
        if nxt <= n and a[nxt] < k:
          idx = nxt
          k -= a[nxt]

        mask >>= 1

      return idx + 1

    def f(x: int) -> int:
      return ((x-1) * (x-2)) // 2 if x >= 3 else 0

    def add_peak(p: int):
      cnt_prev = query(c, p)
      cnt_upto_p = query(c, p+1)
      cnt_total = query(c, n)

      prev_p = kth(c, cnt_prev) - 1 if cnt_prev > 0 else -1
      nxt_p = kth(c, cnt_upto_p+1) - 1 if cnt_upto_p < cnt_total else -1

      if prev_p != -1:
        old_gap = f(nxt_p - prev_p + 1) if nxt_p != -1 else 0
        new_gap = f(p - prev_p + 1)
        update(gap, prev_p+1, new_gap-old_gap)

      new_gap_p = f(nxt_p-p+1) if nxt_p != -1 else 0
      update(gap, p+1, new_gap_p)
      update(c, p+1, 1)
      peak[p] = 1

    def remove_peak(p: int):
      cnt_prev = query(c, p)
      cnt_upto_p = query(c, p+1)
      cnt_total = query(c, n)

      prev_p = kth(c, cnt_prev) - 1 if cnt_prev > 0 else -1
      nxt_p = kth(c, cnt_upto_p+1) - 1 if cnt_upto_p < cnt_total else -1

      curr_gap_p = f(nxt_p-p+1) if nxt_p != -1 else 0
      update(gap, p+1, -curr_gap_p)

      if prev_p != -1:
        old_gap = f(p-prev_p+1)
        new_gap = f(nxt_p-prev_p+1) if nxt_p != -1 else 0
        update(gap, prev_p+1, new_gap-old_gap)

      update(c, p+1, -1)
      peak[p] = 0
        
    for i in range(1, n-1):
      if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        peak[i] = 1
        add_peak(i)

    ans = []
    for q in queries:
      if q[0] == 1:
        l, r = q[1], q[2]
        if r-l+1 < 3:
          ans.append(0)
          continue

        cnt_upto_r = query(c, r)
        cnt_upto_l = query(c, l+1)

        if cnt_upto_r - cnt_upto_l == 0:
          ans.append(0)
          continue

        first = kth(c, cnt_upto_l+1) - 1
        last = kth(c, cnt_upto_r) - 1
        total_f = f(r-l+1)
        sum_gap_internal = query(gap, last) - query(gap, first)
        non_peak = f(first-l+1) + f(r-last+1) + sum_gap_internal
        ans.append(total_f - non_peak)

        continue

      idx, val = q[1], q[2]
      nums[idx] = val
      for i in (idx-1, idx, idx+1):
        if 0 <= i < n:
          is_peak = (i > 0 and i < n-1 and nums[i] > nums[i-1] and nums[i] > nums[i+1])
          if peak[i] != is_peak:
            if is_peak:
              add_peak(i)
            else:
              remove_peak(i)

    return ans
