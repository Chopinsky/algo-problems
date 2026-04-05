'''
657-robot-return-to-origin
'''

from collections import Counter


class Solution:
  def judgeCircle(self, moves: str) -> bool:
    c = Counter(moves)
    opp = {
      'L': 'R',
      'R': 'L',
      'U': 'D',
      'D': 'U',
    }

    for d, od in opp.items():
      if d not in c:
        continue

      if od not in c or c[d] != c[od]:
        return False

    return True
        