'''
2833-furthest-point-from-origin
'''


class Solution:
  def furthestDistanceFromOrigin(self, moves: str) -> int:
    def count(left: bool) -> int:
      dist = 0
      curr = 0

      for ch in moves:
        if ch == '_':
          curr += 1 if not left else -1
        elif ch == 'L':
          curr -= 1
        elif ch == 'R':
          curr += 1

        dist = max(dist, abs(curr))
        # print('move:', left, ch, curr)

      return abs(curr)

    return max(count(True), count(False))

        