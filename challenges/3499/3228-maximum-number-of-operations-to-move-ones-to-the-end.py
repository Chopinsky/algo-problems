'''
3228-maximum-number-of-operations-to-move-ones-to-the-end
'''


class Solution:
  def maxOperations(self, s: str) -> int:
    ops = 0
    suffix = 0
    n = len(s)

    for i in range(n-1, -1, -1):
      d = s[i]
      if d == '1':
        ops += suffix

      if i == n-1 or s[i+1] == '1':
        suffix += 1

    return ops
