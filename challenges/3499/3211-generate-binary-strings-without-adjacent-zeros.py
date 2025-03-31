'''
3211-generate-binary-strings-without-adjacent-zeros
'''

from typing import List

class Solution:
  def validStrings(self, n: int) -> List[str]:
    curr = ['0', '1']
    nxt = []
    n -= 1

    while n > 0:
      for s in curr:
        if s[-1] == '1':
          nxt.append(s+'0')

        nxt.append(s+'1')

      curr, nxt = nxt, curr
      nxt.clear()
      n -= 1

    return curr

        