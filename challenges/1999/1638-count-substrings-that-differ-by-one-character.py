'''
1638-count-substrings-that-differ-by-one-character
'''

from collections import defaultdict


class Solution:
  def countSubstrings(self, s: str, t: str) -> int:
    n, m = len(s), len(t)

    def test(i: int, j: int):
      res = 0
      pre = 0
      curr = 0

      for k in range(min(n-i, m-j)):
        curr += 1
        if s[i+k] != t[j+k]:
          pre, curr = curr, 0

        res += pre

      return res

    return sum(test(i, 0) for i in range(n)) + sum(test(0, j) for j in range(1, m))

  def countSubstrings0(self, s: str, t: str) -> int:
    cand = 'abcdefghijklmnopqrstuvwxyz'
    ct = defaultdict(int)
    cs = defaultdict(int)
    ns = len(s)
    nt = len(t)
    pairs = 0

    for i in range(nt):
      for j in range(i, nt):
        ct[t[i:j+1]] += 1

    for i in range(ns):
      for j in range(i, ns):
        cs[s[i:j+1]] += 1

    # print('init:', cs, ct)
    for s0, cnt in cs.items():
      for k in range(len(s0)):
        for ch in cand:
          if ch == s0[k]:
            continue

          s1 = s0[:k] + ch + s0[k+1:]
          if s1 in ct:
            pairs += cnt * ct[s1]

    return pairs
        