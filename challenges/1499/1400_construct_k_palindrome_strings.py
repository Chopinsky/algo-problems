'''
1400. construct-k-palindrome-strings
'''

from collections import Counter


class Solution:
  def canConstruct(self, s: str, k: int) -> bool:
    n = len(s)
    if k >= n:
      return k == n

    c = Counter(s).values()
    # print('init:', c)

    return sum(1 if cnt%2 == 1 else 0 for cnt in c) <= k

        