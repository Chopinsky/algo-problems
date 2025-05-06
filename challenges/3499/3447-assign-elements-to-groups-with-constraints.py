'''
3447-assign-elements-to-groups-with-constraints
'''

from typing import List
from collections import defaultdict


class Solution:
  def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
    top = max(groups)
    idx = defaultdict(list)
    ans = [-1]*len(groups)
    seen = set()
    n = len(elements)
    one_pos = n 

    for i, val in enumerate(groups):
      idx[val].append(i)

    # print('init:', idx)
    for i, val in enumerate(elements):
      if val == 1:
        one_pos = min(one_pos, i)
        continue

      if val in seen:
        continue

      for v1 in range(val, top+1, val):
        if v1 not in idx:
          continue

        for j in idx[v1]:
          ans[j] = i

        idx.pop(v1)

      seen.add(val)

    # print('done:', one_pos, n, ans)
    if one_pos < n:
      for i in range(len(groups)):
        if ans[i] == -1 or ans[i] > one_pos:
          ans[i] = one_pos

    return ans
        