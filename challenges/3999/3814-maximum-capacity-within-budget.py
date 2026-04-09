'''
3814-maximum-capacity-within-budget
'''

from typing import List
from bisect import bisect_left


class Solution:
  def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
    n = len(costs)
    arr = sorted(zip(costs, capacity))
    top = 0
    # print('init:', arr)

    if arr[0][0] >= budget:
      return top

    c = [a[0] for a in arr]
    cap = [a[1] for a in arr]
    prev = []

    for i in range(n):
      c0 = c[i]
      c1 = cap[i]
      # print('iter:', c0, c1)

      if c0 < budget:
        top = max(top, c1)

      j = min(len(prev)-1, bisect_left(c, budget-c0)-1)
      if j >= 0:
        top = max(top, c1+prev[j])

      if i == 0:
        prev.append(c1)
      else:
        prev.append(max(prev[-1], c1))

    return top
        