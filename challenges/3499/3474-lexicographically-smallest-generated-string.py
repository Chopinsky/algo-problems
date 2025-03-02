'''
3474-lexicographically-smallest-generated-string
'''

from typing import List
from collections import deque


class Solution:
  def generateString(self, s1: str, s2: str) -> str:
    def z_table(s) -> List:
      n = len(s)
      z = [0]*n
      L, R = 0, 0

      for i in range(1, n):
        if i < R:
          k = i - L
          if z[k] + i < R:
            z[i] = z[k]
            continue

          L = i
        else:
          L, R = i, i
          
        while R < n and s[R-L] == s[R]:
          R += 1

        z[i] = R - L

      return z
    
    n, m = len(s1), len(s2)
    z = z_table(s2)
    ans = ['*']*(n+m-1)
    prev = -m

    for i, ch in enumerate(s1):
      if ch == 'F':
        continue

      diff = i-prev
      if diff < m:
        if z[diff] != m-diff:
          return ''

        ans[prev+m:i+m] = s2[-diff:]

      else:
        ans[i:i+m] = s2

      prev = i

    words = list(s2) + ['$'] + ans
    wild = set()
    change = deque()

    for i in range(m+1, len(words)):
      if words[i] != '*':
        continue

      words[i] = 'a'
      wild.add(i)
      if i < 2*m+1:
        change.append(i)

    z = z_table(words)
    i = m+1

    while i < len(words):
      if change and i > change[0]:
        change.popleft()

      j = i+m-1
      if j in wild:
        change.append(j)

      start = i-(m+1)
      if start < n and s1[i-(m+1)] == 'F' and z[i] == m:
        if not change:
          return ''

        j = change.popleft()
        while change and change[0] == j+1 and j+1 < i+m:
          j = change.popleft()

        words[j] = 'b'
        i = j+1

      else:
        i += 1

    return ''.join(words[m+1:])
