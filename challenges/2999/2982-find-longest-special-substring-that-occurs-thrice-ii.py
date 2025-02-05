'''
2982-find-longest-special-substring-that-occurs-thrice-ii
'''

from collections import defaultdict


class Solution:
  def maximumLength(self, s: str) -> int:
    store = [defaultdict(int) for _ in range(26)]
    prev = ''
    cnt = 0

    for ch in s + '$':
      if ch == prev:
        cnt += 1
        continue

      if prev:
        idx = ord(prev)-ord('a')
        store[idx][cnt] += 1

      prev = ch
      cnt = 1
    
    long = -1
    for lst in store:
      if not lst:
        continue

      # cand = sorted(lst.items(), reverse=True)
      ln = max(lst.keys())
      cnt = 0
      total = 0
      # print('check:', lst, ln)

      while ln > 0:
        cnt += lst[ln]
        total += cnt
        # print('iter:', ln, cnt, total)

        if total >= 3:
          long = max(long, ln)
          break

        ln -= 1

    return long
