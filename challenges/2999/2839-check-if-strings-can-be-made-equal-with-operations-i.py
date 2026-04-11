'''
2839-check-if-strings-can-be-made-equal-with-operations-i
'''


class Solution:
  def canBeEqual(self, s1: str, s2: str) -> bool:
    if s1 == s2:
      return True

    def check(p1: bool, p2: bool) -> bool:
      ch = list(s1)
      if p1:
        ch[0], ch[2] = ch[2], ch[0]

      if p2:
        ch[1], ch[3] = ch[3], ch[1]

      return ''.join(ch) == s2

    return check(True, False) or check(True, True) or check(False, True)
