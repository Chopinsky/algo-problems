'''
3703-remove-k-balanced-substrings
'''


class Solution:
  def removeSubstring(self, s: str, k: int) -> str:
    i = 0
    n = len(s)
    stack = []

    def make_updates():
      while len(stack) >= 2:
        if stack[-1][0] == stack[-2][0]:
          # combine
          _, c0 = stack.pop()
          stack[-1][1] += c0
        elif stack[-1][0] == ')' and stack[-1][1] >= k and stack[-2][1] >= k:
          # remove
          stack[-1][1] -= k
          stack[-2][1] -= k

          # clean up
          while stack and stack[-1][1] == 0:
            stack.pop()
        else:
          # done
          break


    while i < n:
      ch = s[i]
      if not stack or ch != stack[-1][0]:
        stack.append([ch, 1])
      else:
        stack[-1][1] += 1

      make_updates()
      # print('iter:', i, stack)
      i += 1

    res = ""
    for b, cnt in stack:
      res += b*cnt

    return res
        