'''
2124-check-if-all-as-appears-before-all-bs
'''


class Solution:
  def checkString(self, s: str) -> bool:
    last_a = -1
    first_b = -1

    for i, ch in enumerate(s):
      if ch == 'a':
        last_a = i
      elif first_b < 0:
        first_b = i

    if last_a < 0 or first_b < 0:
      return True

    return last_a < first_b
        