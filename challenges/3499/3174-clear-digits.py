'''
3174-clear-digits
'''


class Solution:
  def clearDigits(self, s: str) -> str:
    stack = []
    for ch in s:
      if '0' <= ch <= '9':
        if stack:
          stack.pop()

        continue

      stack.append(ch)

    return ''.join(stack)
        