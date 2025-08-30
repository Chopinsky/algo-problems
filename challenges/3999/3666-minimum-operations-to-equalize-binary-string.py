'''
3666-minimum-operations-to-equalize-binary-string
'''

import math


class Solution:
  def minOperations(self, s: str, k: int) -> int:
    def ceil(x: int, y: int) -> int:
      return (x+y-1) // y

    n = len(s)
    zc = s.count('0')

    if k == n:
      return 0 if zc == 0 else 1 if zc == n else -1

    ans = math.inf
    if zc%2 == 0:
      m = max(ceil(zc, k), ceil(zc, n-k))
      m += m & 1
      ans = min(ans, m)
    
    if zc%2 == k%2:
      m = max(ceil(zc, k), ceil(n-zc, n-k))
      m += m&1 == 0
      ans = min(ans, m)
    
    return ans if ans < math.inf else -1

