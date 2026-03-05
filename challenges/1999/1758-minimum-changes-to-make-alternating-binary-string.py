'''
1758-minimum-changes-to-make-alternating-binary-string
'''


class Solution:
  def minOperations(self, s: str) -> int:
    lst = list(int(ch) for ch in s)

    def count(val: int) -> int:
      ops = 0
      
      for d in lst:
        if d != val:
          ops += 1

        val = 1 - val

      return ops

    return min(count(0), count(1))
        