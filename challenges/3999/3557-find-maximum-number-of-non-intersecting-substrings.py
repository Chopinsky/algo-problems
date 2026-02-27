'''
3557-find-maximum-number-of-non-intersecting-substrings
'''

from collections import defaultdict


class Solution:
  def maxSubstrings(self, word: str) -> int:
    n = len(word)
    ln = [0]*n
    idx = defaultdict(list)

    for i in range(n):
      ch = word[i]
      cnt = 0
      lst = idx[ch]

      for j in range(len(lst)-1, -1, -1):
        k = lst[j]
        sub_ln = i - k + 1
        
        if sub_ln >= 4:
          cnt = max(cnt, 1+(ln[k-1] if k > 0 else 0))
          break

      lst.append(i)
      ln[i] = max(ln[i-1] if i > 0 else 0, cnt)
      # print('iter:', ln[i])

    return ln[-1]
        