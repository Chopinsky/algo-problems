'''
3561-resulting-string-after-adjacent-removals
'''


class Solution:
  def resultingString(self, s: str) -> str:
    stack = []

    def is_cons(a: str, b: str):
      diff = abs(ord(b) - ord(a))
      return diff == 1 or diff == 25

    for ch in s:
      if stack and is_cons(stack[-1], ch):
        stack.pop()
      else:
        stack.append(ch)

    return ''.join(stack)
        