'''
3498-reverse-degree-of-a-string
'''


class Solution:
  def reverseDegree(self, s: str) -> int:
    return sum(
      (i+1) * (26 - (ord(ch) - ord('a')))
      for i, ch in enumerate(s)
    )
