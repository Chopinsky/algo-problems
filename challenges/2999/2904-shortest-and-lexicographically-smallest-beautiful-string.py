'''
2904-shortest-and-lexicographically-smallest-beautiful-string
'''


class Solution:
  def shortestBeautifulSubstring(self, s: str, k: int) -> str:
    res = ""
    cnt = 0
    r = 0
    n = len(s)

    for l in range(n):
      while r < n and cnt < k:
        if s[r] == '1':
          cnt += 1

        r += 1

      if cnt == k and s[l] == '1':
        # print('iter:', (r-l), s[l:r])
        if res == "" or r-l < len(res):
          res = s[l:r]
        elif r-l == len(res):
          res = min(res, s[l:r])

      if s[l] == '1':
        cnt -= 1

    return res

        