'''
3762-minimum-operations-to-equalize-subarrays
'''

from typing import List


class Solution:
  def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
    n = len(nums)
    bad = [0]
    prev = -1
    step = 0

    for val in nums:
      rem = val % k
      step += (rem != prev)
      bad.append(step)
      prev = rem

    # print('init:', bad)
    ans = [-1]*len(queries)
    vals = [val//k for val in nums]
    sorted_vals = sorted(list(set(vals)))
    ranked = {v: i for i, v in enumerate(sorted_vals, 1)}
    m = len(sorted_vals)

    block = max(1, n//int(len(queries)**0.5 or 1))
    sorted_queries = [(l//block, r, l, i) for i, (l, r) in enumerate(queries)]
    sorted_queries.sort(key=lambda x: (x[0], x[1] if x[0]&1 else -x[1]))

    cnt_bit = [0]*(m+1) # frequency bit
    sum_bit = [0]*(m+1) # value sum bit
    curr_cnt = 0
    curr_sum = 0

    def update(i: int, delta: int):
      nonlocal curr_cnt, curr_sum

      v = vals[i]
      rank = ranked[v]

      val_delta = delta*v
      curr_cnt += delta
      curr_sum += val_delta

      while rank <= m:
        sum_bit[rank] += val_delta
        cnt_bit[rank] += delta
        rank += rank & -rank

    l, r = 0, -1
    highest_bit = 1 << (m.bit_length() - 1)

    for _, end, start, qidx in sorted_queries:
      # not the same remainder
      if bad[end+1] - bad[start+1] > 0:
        continue

      while l > start:
        l -= 1
        update(l, 1)

      while r < end:
        r += 1
        update(r, 1)

      while l < start:
        update(l, -1)
        l += 1

      while r > end:
        update(r, -1)
        r -= 1

      idx = 0
      pcnt = 0
      psum = 0
      mask = highest_bit
      target = curr_cnt >> 1

      while mask > 0:
        nxt_idx = idx + mask
        if nxt_idx <= m and pcnt+cnt_bit[nxt_idx] <= target:
          idx = nxt_idx
          pcnt += cnt_bit[idx]
          psum += sum_bit[idx]

        mask >>= 1

      median = sorted_vals[idx]
      ssum = curr_sum - psum
      scnt = curr_cnt - pcnt

      ans[qidx] = ssum - median*scnt + median*pcnt - psum

    return ans
        