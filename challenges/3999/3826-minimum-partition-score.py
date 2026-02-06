'''
3826-minimum-partition-score
'''

from typing import List
from collections import deque


class Line:
  def __init__(self, s: int, it: int, pt: int):
    self.s = s
    self.it = it
    self.pt = pt

  def eval(self, x: int) -> int:
    return self.s*x + self.it


class Solution:
  def minPartitionScore(self, nums: List[int], k: int) -> int:
    n = len(nums)

    prefix_sum = [0] * (n + 1)
    for i in range(n):
      prefix_sum[i+1] = prefix_sum[i] + nums[i]

    dp = [0] * (n + 1)
    for i in range(1, n+1):
      s = prefix_sum[i]
      dp[i] = (s * (s+1)) // 2

    def intersect(l1, l2):
      return (l2[1] - l1[1]) / (l1[0] - l2[0])

    for partition in range(2, k+1):
      nxt_dp = [0] * (n + 1)
      dq = deque()

      def add_line(idx: int):
        p_sum = prefix_sum[idx]
        m = -2*p_sum
        c = 2*dp[idx] + p_sum*p_sum - p_sum
        line = (m, c)

        while len(dq) >= 2:
          if intersect(dq[-1], line) > intersect(dq[-2], dq[-1]):
            break

          dq.pop()

        dq.append(line)

      add_line(partition-1)

      for i in range(partition, n+1):
        x = prefix_sum[i]

        while len(dq) >= 2:
          if dq[0][0]*x + dq[0][1] < dq[1][0]*x + dq[1][1]:
            break

          dq.popleft()

        best_line = dq[0]
        val = best_line[0]*x + best_line[1]

        total_val = val + x*x + x
        nxt_dp[i] = total_val // 2

        if i < n:
          add_line(i)

      dp = nxt_dp

    return dp[n]
    
  def minPartitionScore(self, nums: List[int], k: int) -> int:
    n = len(nums)
    prefix = [0]*(n+1)

    for i in range(1, n+1):
      prefix[i] = prefix[i-1] + nums[i-1]

    def is_redundant(l1, l2, l3):
      v1 = (l3.it-l1.it) * (l1.s-l2.s)
      v2 = (l2.it-l1.it) * (l1.s-l3.s)
      return v1 <= v2

    def solve_with_penalty(lmb: int):
      dq = deque([])
      dq.append(Line(0, 0, 0))

      di = 0
      pi = 0

      for i in range(1, len(prefix)):
        x = prefix[i]

        while len(dq) > 1:
          first = dq.popleft()
          second = dq[0]

          if first.eval(x) <= second.eval(x):
            dq.appendleft(first)
            break

        best = dq[0]
        di = x*x + x + 2*lmb + best.eval(x)
        pi = best.pt + 1
        new_line = Line(-2*x, di+x*x-x, pi)

        while len(dq) > 1:
          last = dq.pop()
          second_last = dq[-1]
          if not is_redundant(second_last, last, new_line):
            dq.append(last)
            break

        dq.append(new_line)

      return di, pi

    l = 0
    r = 10**15+1
    best_lambda = 0

    while l <= r:
      mid = (l+r) // 2
      _, pi = solve_with_penalty(mid)

      if pi <= k:
        best_lambda = mid
        r = mid - 1
      else:
        l = mid + 1
    
    di, pi = solve_with_penalty(best_lambda)

    return (di - 2*k*best_lambda) // 2
        