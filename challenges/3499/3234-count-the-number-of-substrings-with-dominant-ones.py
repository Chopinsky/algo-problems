'''
3234-count-the-number-of-substrings-with-dominant-ones
'''

from collections import deque


class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    n = len(s)
    magic = int(n**0.5) + 1
    zeros = deque(i for i, c in enumerate(s) if c == '0')
    zeros.append(n)
    ans = 0

    for i in range(n):
      while zeros and zeros[0] < i:
        zeros.popleft()

      prev = i
      for num_zeros, curr in enumerate(zeros):
        if num_zeros >= magic:
          break

        min_ln = max(
          prev-i+1,
          num_zeros*num_zeros + num_zeros
        )
        max_ln = curr - i
        
        ans += max(max_ln-min_ln+1, 0)
        prev = curr

    return ans
