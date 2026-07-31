'''
3913-sort-vowels-by-frequency
'''

from collections import defaultdict


class Solution:
  def sortVowels(self, s: str) -> str:
    v: set[str] = set('aeiou')
    ch: list[str] = list(s)
    cnt: dict[str, int] = defaultdict(int)
    first: dict[str, int] = {}
    cand: list[int] = []

    for i, c in enumerate(s):
      if c not in v:
        continue

      if c not in first:
        first[c] = i

      cand.append(i)
      cnt[c] += 1

    vals = sorted([cnt, -first[c], c] for c, cnt in cnt.items())
    idx = 0
    # print('init:', vals)

    while vals and idx < len(cand):
      i = cand[idx]
      idx += 1

      while vals and vals[-1][0] == 0:
        vals.pop()

      if vals:
        ch[i] = vals[-1][2]
        vals[-1][0] -= 1

    # print(ch)
    return "".join(ch)

