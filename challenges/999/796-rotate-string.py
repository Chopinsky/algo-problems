'''
796-rotate-string
'''


class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    n = len(s)
    s += s[:-1]
    # print('init:', s)

    for i in range(n):
      if s[i:i+n] == goal:
        return True

    return False
        