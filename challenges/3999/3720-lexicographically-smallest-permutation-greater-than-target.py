'''
3720-lexicographically-smallest-permutation-greater-than-target
'''

from collections import Counter


class Solution:
  def lexGreaterPermutation(self, s: str, target: str) -> str:
    s0 = ''.join(sorted(list(s), reverse=True))
    if s0 < target:
      return ""

    c: Counter[str, int] = Counter(s)
    n = len(s)
    # print('init:', c)

    def gen(i: int) -> str:
      t_ch = target[i]
      cand = sorted(ch for ch in c if c[ch] > 0)

      if i == n-1:
        return "" if cand[0] <= t_ch else cand[0]

      for ch in cand:
        if ch < t_ch:
          continue

        # can use this character
        c[ch] -= 1

        if ch == t_ch:
          # equal, need to look at others
          rest = gen(i+1)
        else:
          # large, done
          rest = ''.join(ch*c[ch] for ch in cand)

        # print('iter:', i, )
        if rest:
          return ch + rest

        c[ch] += 1

      return ""

    return gen(0)
        