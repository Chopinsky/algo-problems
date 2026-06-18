'''
1344-angle-between-hands-of-a-clock
'''


class Solution:
  def angleClock(self, hour: int, minutes: int) -> float:
    h = 30.0 * (hour%12 + minutes/60.0)
    m = 6.0 * minutes

    if h >= 360.0:
      h -= 360.0

    if m >= 360.0:
      m -= 360.0

    diff = abs(h-m)
    # print('init:', h, m)

    return min(diff, 360-diff)
