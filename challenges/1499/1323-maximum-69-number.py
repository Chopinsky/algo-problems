'''
1323-maximum-69-number
'''


class Solution:
  def maximum69Number (self, num: int) -> int:
    d = list(str(num))
    n = len(d)

    for i in range(n):
      if d[i] == '6':
        d[i] = '9'
        break

    return int(''.join(d))
        