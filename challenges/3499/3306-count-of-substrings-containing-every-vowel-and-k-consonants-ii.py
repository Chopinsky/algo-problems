'''
3306-count-of-substrings-containing-every-vowel-and-k-consonants-ii
'''

from bisect import bisect_left
from collections import defaultdict


class Solution:
  def countOfSubstrings(self, word: str, k: int) -> int:
    count = 0
    v = set(['a', 'e', 'i', 'o', 'u'])
    vow = defaultdict(list)
    con = list()
    n = len(word)

    for i in range(n):
      if word[i] in v:
        vow[word[i]].append(i)
      else:
        con.append(i)

    # print('init:', vow, con)
    if len(vow) < 5 or len(con) < k:
      return count

    for i in range(n):
      if n-i < 5+k:
        break

      r = i
      done = False
      for lst in vow.values():
        if i > lst[-1]:
          done = True
          break

        idx = bisect_left(lst, i)
        r = max(r, lst[idx])

      if done:
        break

      if k == 0:
        idx = bisect_left(con, i)
        if idx >= len(con) or con[idx] > r:
          r1 = n if idx >= len(con) else con[idx]
          count += r1-r

        continue

      idx = bisect_left(con, i) + k - 1
      if idx >= len(con) or idx < 0:
        continue

      r0 = con[idx]
      r1 = n if idx+1 >= len(con) else con[idx+1]
      if r1 <= r:
        continue

      # print('update:', i, r, r0, r1, word[i:r1])
      count += r1-max(r, r0)

    return count
        