'''
3614-process-string-with-special-operations-ii
'''


class Solution:
  def processStr(self, s: str, k: int) -> str:
    ln = 0
    for ch in s:
      if ch == '*':
        ln = max(0, ln-1)
        continue

      if ch == '#':
        ln *= 2
        continue

      if ch != '%':
        ln += 1

    # out of final string's bound
    if k >= ln:
      return '.'

    # reverse-gen the string -- from the back
    for i in range(len(s)-1, -1, -1):
      c = s[i]
      if c == '*':
        # push back due to deletion
        ln += 1
        continue

      if c == '#':
        ln //= 2
        if k >= ln:
          # copy the index to position
          k -= ln

        continue

      if c == '%':
        # mirror the position mapping
        k = ln-1-k
        continue

      ln -= 1
      if k == ln:
        return c

    return '.'

      
        