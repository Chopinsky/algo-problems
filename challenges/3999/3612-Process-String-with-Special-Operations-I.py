'''
3612-Process-String-with-Special-Operations-I
'''


class Solution:
  def processStr(self, s: str) -> str:
    res = []

    for ch in s:
      if ch == '*':
        if res:
          res.pop()

        continue

      if ch == '#':
        res.extend(res)
        continue

      if ch == '%':
        res = res[::-1]
        continue

      if 'a' <= ch <= 'z':
        res.append(ch)

    return ''.join(res)
        