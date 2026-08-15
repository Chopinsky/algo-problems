'''
4023-elevator-requests-ii
'''

from bisect import bisect_left
import math


class Solution:
  def elevatorRequests(self, _n: int, start: int, req: list[int]) -> int:
    req = sorted(req)
    idx = bisect_left(req, start)
    
    if idx < len(req) and req[idx] == start:
      req.pop(idx)

    if not req:
      return 0

    m = len(req)
    INF = math.inf
    prev_at_high = [INF]*(m+1)
    prev_at_low = [INF]*(m+1)
    prev_at_high[m-1] = 0
    prev_at_high[m] = 0

    for h in range(m-2, -1, -1):
      prev_at_high[h] = (req[h+1]-req[h])*(m-h-1) + prev_at_high[h+1]

    for l in range(idx):
      curr_at_low = [INF]*(m+1)
      curr_at_high = [INF]*(m+1)
      rl = req[l]
      
      for h in range(m, l, -1):
        cnt = m - h + l
        if cnt <= 0:
          curr_at_low[h] = 0
          continue

        best = INF
        if l > 0:
          v = (rl-req[l-1])*cnt + prev_at_low[h]
          best = min(best, v)

        if h < m:
          v = (req[h]-rl)*cnt + prev_at_high[h]
          best = min(best, v)
        
        curr_at_low[h] = best
        if h < m:
          best = (req[h]-rl)*cnt + curr_at_low[h+1]
          if h+1 < m:
            v = (req[h+1]-req[h])*cnt + curr_at_high[h+1]
            best = min(best, v)

          curr_at_high[h] = best

      prev_at_low = curr_at_low
      prev_at_high = curr_at_high
    
    ans = INF
    if idx < m:
      ans = min(ans, (req[idx]-start)*m + prev_at_high[idx])

    if idx > 0:
      ans = min(ans, (start-req[idx-1])*m + prev_at_low[idx])

    return ans

  def elevatorRequests(self, _n: int, start: int, req: list[int]) -> int:
    req.sort()
    idx = bisect_left(req, start)
    
    # remove the current floor
    if idx < len(req) and req[idx] == start:
      req.pop(idx)
    
    # print('init:', req)
    if not req:
      return 0

    p = math.inf
    m = len(req)
    states = {}

    def dp(l: int, h: int, at_low: bool) -> int:
      # remain to visit
      cnt = (m-h) + l
      # print('dp:', (l, h, at_low), cnt)

      # done
      if cnt <= 0:
        return 0

      if (l, h, at_low) in states:
        return states[l, h, at_low]

      p = math.inf
      if at_low:
        if l-1 >= 0:
          # move lower
          p0 = (req[l]-req[l-1])*cnt + dp(l-1, h, True)
          p = min(p, p0)

        if h < m:
          # move higher
          p1 = (req[h]-req[l])*cnt + dp(l-1, h, False)
          p = min(p, p1)

      else:
        if l >= 0:
          # move lower
          p2 = (req[h]-req[l])*cnt + dp(l, h+1, True)
          p = min(p, p2)

        if h+1 < m:
          # move higher
          p3 = (req[h+1]-req[h])*cnt + dp(l, h+1, False)
          p = min(p, p3)

      # print('res:', p)
      states[l, h, at_low] = p

      return p

    # to higher floor first
    if idx < m:
      p0 = (req[idx]-start)*m + dp(idx-1, idx, False)
      p = min(p, p0)
      # print('init up:', p0)

    # to lower floor first
    if idx-1 >= 0:
      p1 = (start-req[idx-1])*m + dp(idx-1, idx, True)
      p = min(p, p1)
      # print('init down:', p1)

    return p
