'''
3971-maximum-total-value
'''


class Solution:
  def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
    mod = 10**9 + 7
    n = len(value)

    def count(x: int) -> int:
      cnt = 0

      for i, val in enumerate(value):
        if val < x:
          continue

        cnt += (val-x) // decay[i] + 1
        if cnt >= m:
          break

      return cnt

    lo, hi = 1, 10**9+1 # count range
    th = 0

    while lo <= hi:
      mid = (lo + hi) // 2

      if count(mid) >= m:
        th = mid
        lo = mid+1
      else:
        hi = mid-1

    total = 0
    used = 0

    for i, val in enumerate(value):
      # won't be used as it's below the m-th
      # value to begine with
      if val <= th:
        continue

      d = decay[i]
      cnt = (val-(th+1)) // d + 1
      used += cnt

      # tail value before falling off m-th value threshold
      last_val = val - (cnt-1)*d

      # aggregate over {cnt} usage of value[i] above m-th 
      # value threshold
      total += cnt * (val + last_val) // 2

    # count tail usage: exactly {remaining} values will be used
    # at the m-th value threshold
    remaining = m - used
    if remaining > 0:
      total += remaining * th
    # print('done:', remaining, th)

    return total % mod

  '''
  def maxTotalValue1(self, value: list[int], decay: list[int], m: int) -> int:
    mod = 10**9 + 7
    ans = 0
    q = sorted((-val, decay[i], i) for i, val in enumerate(value))
    # print('init:', q)

    while m > 0 and q:
      val, d, i = heappop(q)
      val = -val
      ans = (ans + val) % mod
      m -= 1

      if val - d > 0:
        heappush(q, (-val+d, d, i))

    return ans
  '''
