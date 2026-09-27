'''
4068-maximize-meeting-earnings-with-idle-gaps
'''

from heapq import heappush, heappop


class Solution:
  def maxEarnings(self, meetings: list[list[int]]) -> int:
    meetings.sort()
    last = meetings[-1][0]
    ans = 0
    # [end_time, accumulated_score]
    cand = []
    # [gap_included_huristic_score, end_time, accumulated_score]
    prev = [0, -1, 0]  

    for s0, e0, r0 in meetings:
      while cand and cand[0][0] <= s0:
        e1, r1 = heappop(cand)
        r_fin = r1 + (last-e1)
        if r_fin > prev[0]:
          prev[0] = r_fin
          prev[1] = e1
          prev[2] = r1

      r2 = r0 + prev[2] + (s0 - prev[1] if prev[1] >= 0 else 0)
      ans = max(ans, r2)
      heappush(cand, (e0, r2))

    return ans
