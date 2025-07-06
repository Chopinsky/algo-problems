'''
2138-divide-a-string-into-groups-of-size-k
'''

from typing import List


class Solution:
  def divideString(self, s: str, k: int, fill: str) -> List[str]:
    n = len(s)
    ans = [s[i:i+k] for i in range(0, n, k)]
    # print('done', len(ans[-1])-k)
    if len(ans[-1]) < k:
      ans[-1] += (k-len(ans[-1])) * fill

    return ans
        