'''
3458-select-k-disjoint-special-substrings
'''

from collections import Counter


class Solution:
  def maxSubstringLength(self, s: str, k: int) -> bool:
    first = {}
    last = {}
    count = Counter()

    for i, c in enumerate(s):
      if c not in first:
        first[c] = i

      last[c] = i
      count[c] += 1

    intervals = []
    for i in first.values():
      for j in last.values():
        if i > j:
          continue

        cnt = 0
        for c in count:
          if i <= first[c] <= last[c] <= j:
            cnt += count[c]

        if cnt == j-i+1 and cnt < len(s):
          intervals.append([i, j])

    intervals.sort(key=lambda s: s[1]-s[0])
    res = []

    for i, j in intervals:
      if all(y < i or j < x for x, y in res):
        res.append([i, j])

    return len(res) >= k
        