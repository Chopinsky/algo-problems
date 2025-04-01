'''
3138-minimum-length-of-anagram-concatenation
'''


class Solution:
  def minAnagramLength(self, s: str) -> int:
    n = len(s)
    cand = []

    for ln in range(1, n+1):
      if n%ln == 0:
        cand.append(ln)

    l, r = 0, len(cand)-1
    last = n
    # print('init:', cand)

    def is_equal(d0, d1) -> bool:
      if len(d0) != len(d1):
        return False

      for ch in d0:
        if ch not in d1 or d0[ch] != d1[ch]:
          return False

      return True

    def check(ln: int) -> bool:
      d0 = Counter(s[:ln])
      # print('check:', ln)

      for i in range(ln, n, ln):
        d1 = Counter(s[i:i+ln])
        if not is_equal(d0, d1):
          return False

      return True

    for ln in cand:
      if check(ln):
        return ln

    return n
        