'''
868-binary-gap
'''


class Solution:
  def binaryGap(self, n: int) -> int:
    s = bin(n)[2:]
    prev = -1
    dist = 0

    for i in range(len(s)):
      ch = s[i]
      if ch == '0':
        continue

      if prev >= 0:
        dist = max(dist, i-prev)

      prev = i
    
    return dist
