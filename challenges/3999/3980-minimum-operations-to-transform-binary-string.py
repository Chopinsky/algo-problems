'''
3980-minimum-operations-to-transform-binary-string
'''


class Solution:
  def minOperations(self, s1: str, s2: str) -> int:
    n = len(s1)
    if s1 == s2:
      return 0

    if n == 1:
      if s1 == '1' and s2 == '0':
        return -1

      return 1

    o0 = 0
    o1 = 0
    s = {
      '10,11': 1,
      '10,00': 2,
      '10,01': 3,
      '01,11': 1,
      '01,00': 2,
      '01,10': 3,
      '00,01': 1,
      '00,10': 1,
      '00,11': 2,
      '11,00': 1,
      '11,01': 2,
      '11,10': 2,
    }

    i = 0
    while i < n:
      if s1[i] == s2[i]:
        i += 1
        continue
      
      if s1[i] == '0' and s2[i] == '1':
        o0 += 1
        i += 1
        continue

      k0 = s1[i:i+2] if i < n-1 else s2[i-1] + s1[i]
      k1 = s2[i:i+2] if i < n-1 else s2[i-1:i+1]
      # print('convert:', k0, k1)

      if k0 != k1:
        o0 += s[k0+','+k1]

      i += 2

    i = n-1
    while i >= 0:
      if s1[i] == s2[i]:
        i -= 1
        continue

      if s1[i] == '0' and s2[i] == '1':
        o1 += 1
        i -= 1
        continue

      k0 = s1[i-1:i+1] if i > 0 else s1[i] + s2[i+1]
      k1 = s2[i-1:i+1] if i > 0 else s2[:i+2]

      if k0 != k1:
        o1 += s[k0+','+k1]

      i -= 2

    return min(o0, o1)
