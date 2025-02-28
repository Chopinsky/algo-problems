'''
3443-maximum-manhattan-distance-after-k-changes
'''


class Solution:
  def maxDistance(self, s: str, k: int) -> int:
    d = {
      'N': (0, 1),
      'E': (1, 0),
      'W': (-1, 0),
      'S': (0, -1),
    }
    # print('init:', c)

    def calc_dist(r0, r1, d0):
      rem = k
      x, y = 0, 0
      dist = 0

      for ch in s:
        if (ch == r0 or ch == r1) and rem > 0:
          ch = d0
          rem -= 1

        dx, dy = d[ch]
        x += dx
        y += dy
        dist = max(dist, abs(x)+abs(y))

      # print('dist:', (g0, g1), (r0, r1), d0, dist)
      return dist

    return max(
      calc_dist('S', 'W', 'N'), # NE to N
      calc_dist('S', 'W', 'E'), # NE to E
      calc_dist('S', 'E', 'N'), # NW to N
      calc_dist('S', 'E', 'W'), # NW to W
      calc_dist('N', 'E', 'S'), # SW to S
      calc_dist('N', 'E', 'W'), # SW to W
      calc_dist('N', 'W', 'S'), # SE to S
      calc_dist('N', 'W', 'E'), # SE to E
    )

        