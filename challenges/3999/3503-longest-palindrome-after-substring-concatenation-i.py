'''
3503-longest-palindrome-after-substring-concatenation-i
'''

from functools import cache


class Solution:
  def longestPalindrome(self, s: str, t: str) -> int:
    candt = set()
    cands = set()
    ans = 0
    ns = len(s)
    nt = len(t)

    @cache
    def is_pal(w: str) -> bool:
      if not w:
        return True

      i, j = 0, len(w)-1
      while i < j and w[i] == w[j]:
        i += 1
        j -= 1

      return i >= j

    for i in range(nt):
      for j in range(i, nt):
        candt.add(t[i:j+1][::-1])

    # print('init:', ans, cand)
    for i in range(ns):
      for j in range(i, ns):
        cands.add(s[i:j+1][::-1])

        if is_pal(s[i:j+1]):
          ans = max(ans, j-i+1)

        if s[i:j+1] in candt:
          ans = max(ans, 2*(j-i+1))

        for k in range(i+1, j+1):
          if not is_pal(s[k:j+1]):
            continue

          if s[i:k] not in candt:
            continue

          ans = max(ans, j-i+1+(k-i))

    for i in range(nt):
      for j in range(i, nt):
        if is_pal(t[i:j+1]):
          ans = max(ans, j-i+1)

        if t[i:j+1] in cands:
          ans = max(ans, 2*(j-i+1))

        for k in range(i, j):
          if not is_pal(t[i:k+1]):
            continue

          if t[k+1:j+1] not in cands:
            continue

          # print('t:', t[i:j+1], t[i:k+1])
          ans = max(ans, j-i+1+(j-k))

    return ans
