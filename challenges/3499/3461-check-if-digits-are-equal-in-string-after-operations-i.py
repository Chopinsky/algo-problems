'''
3461-check-if-digits-are-equal-in-string-after-operations-i
'''


class Solution:
  def hasSameDigits(self, s: str) -> bool:
    while len(s) > 2:
      nxt = ""
      prev = int(s[0])

      for ch in s[1:]:
        d = int(ch)
        nxt += str((prev+d)%10)
        prev = d

      # print('iter:', s, nxt)
      s = nxt

    return s[0] == s[1]
        