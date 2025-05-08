'''
3365-rearrange-k-substrings-to-form-target-string
'''

from collections import defaultdict


class Solution:
  def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
    n = len(s)
    if k == n:
      return True

    ln = n // k
    freq = defaultdict(int)

    for i in range(0, n, ln):
      freq[s[i:i+ln]] += 1

    # print('init:', freq)
    for i in range(0, n, ln):
      seg = t[i:i+ln]
      if not freq[seg]:
        return False

      freq[seg] -= 1

    return True
        