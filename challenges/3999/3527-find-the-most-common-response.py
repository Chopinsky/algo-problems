'''
3527-find-the-most-common-response
'''

from typing import List
from collections import defaultdict


class Solution:
  def findCommonResponse(self, resp: List[List[str]]) -> str:
    m, n = len(resp), len(resp[0])
    cand = [set(resp[i]) for i in range(m)]
    cnt = defaultdict(int)

    for a in cand:
      for b in a:
        cnt[b] += 1

    most = max(cnt.values())
    ans = sorted(k for k in cnt if cnt[k] == most)

    return ans[0]
        