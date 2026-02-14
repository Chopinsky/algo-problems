'''
3713-longest-balanced-substring-i
'''

from typing import List


class Solution:
  def longestBalanced(self, s: str) -> int:
    def check(c: List) -> bool:
      cnt = 0

      for val in c:
        if val == 0:
          continue

        if cnt > 0 and val != cnt:
          return False

        cnt = val

      return True

    ln = 1
    n = len(s)

    for i in range(n):
      if n-i < ln:
        break

      a = [0]*26
      for j in range(i, n):
        idx = ord(s[j]) - ord('a')
        a[idx] += 1

        if check(a):
          ln = max(ln, j-i+1)

    return ln



        
        