'''
3645-maximum-total-from-optimal-activation-order
'''

from collections import defaultdict
from heapq import heappush, heappop


class Solution:
  def maxTotal(self, value: list[int], limit: list[int]) -> int:
    groups = defaultdict[int, list[int]](list)

    for v, l in zip(value, limit):
      heappush(groups[l], v)

      # only the top-l values can be included before
      # permanently flipping all
      if len(groups[l]) > l:
        heappop(groups[l])

    # print('done:', groups)
    return sum(sum(lst) for lst in groups.values())
        