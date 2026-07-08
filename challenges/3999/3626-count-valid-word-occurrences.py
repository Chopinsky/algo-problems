'''
3626-count-valid-word-occurrences
'''

from collections import defaultdict
from typing import Dict


class Solution:
  def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
    base = "".join(chunks)
    c: Dict[int, int] = defaultdict(int)
    cdx = set()
    curr = ""
    n = len(base)

    for i in range(n):
      if base[i] == '-' and (i-1 >= 0 and 'a' <= base[i-1] <= 'z') and (i+1 < n and 'a' <= base[i+1] <= 'z'):
        cdx.add(i)

    for i, ch in enumerate(base):
      if i in cdx or "a" <= ch <= "z":
        curr += ch
        continue

      if curr:
        c[curr] += 1
        curr = ""

    if curr:
      c[curr] += 1

    # print('init:', c)

    return [c[w] for w in queries]
        