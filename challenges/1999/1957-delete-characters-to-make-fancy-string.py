'''
1957-delete-characters-to-make-fancy-string
'''


class Solution:
  def makeFancyString(self, s: str) -> str:
    prev = ""
    count = 0
    n = len(s)
    res = ""

    for ch in s:
      if ch != prev:
        prev = ch
        count = 1
        res += ch
      elif count < 2:
        count += 1
        res += ch

    return res

        