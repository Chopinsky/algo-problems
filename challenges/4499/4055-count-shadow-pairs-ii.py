'''
4055-count-shadow-pairs-ii
'''

from bisect import bisect_right


class Solution:
  def shadowPairs(self, nums: list[int]) -> int:
    d = {val:i for i, val in enumerate(sorted(set(nums)))}
    q = [([d[val] for val in nums], 0, len(d))]
    cnt = 0
    # print('init:', d, q)

    while q:
      cand, l, r = q.pop()
      if r-l <= 1 or len(cand) < 2:
        # nothing more to conquer
        continue

      m = (l+r) // 2
      lo, hi = [], []

      for i, pos in enumerate(cand):
        if pos < m:
          while lo and cand[lo[-1]] < pos:
            lo.pop()

          lo.append(i)

        else:
          while hi and cand[hi[-1]] >= pos:
            hi.pop()

          p = hi[-1] if hi else -1
          cnt += len(lo) - bisect_right(lo, p)
          hi.append(i)

      q.append(([pos for pos in cand if pos < m], l, m))
      q.append(([pos for pos in cand if pos >= m], m, r))

    return cnt

  def shadowPairs1(self, nums: list[int]) -> int:
    cnt = 0
    n = len(nums)

    for j in range(1, n):
      th = 0
      vj = nums[j]

      for i in range(j-1, -1, -1):
        vi = nums[i]
        if vi >= vj or vi < th:
          continue

        cnt += 1
        th = vi

    return cnt
