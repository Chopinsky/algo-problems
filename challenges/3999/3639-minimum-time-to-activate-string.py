'''
3639-minimum-time-to-activate-string
'''


class Solution:
  def minTime(self, s: str, order: list[int], k: int) -> int:
    n = len(s)
    if n*(n-1)//2 + n < k:
      return -1

    def count(mid: int) -> int:
      cand = sorted(order[:mid+1])
      cnt = 0

      for i, idx in enumerate(cand):
        if i == 0:
          cnt += (idx+1) * (n-idx)
        else:
          cnt += (idx-cand[i-1]) * (n-idx)

      # print('check:', mid, cand, cnt)
      return cnt

    l, r = 0, n-1
    last = r

    while l <= r:
      mid = (l+r) // 2
      if count(mid) >= k:
        last = mid
        r = mid-1
      else:
        l = mid+1

    return last
        