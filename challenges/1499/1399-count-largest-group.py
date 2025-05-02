'''
1399-count-largest-group
'''

from collections import defaultdict


class Solution:
  def countLargestGroup(self, n: int) -> int:
    g = defaultdict(int)

    def convert(val: int) -> int:
      return sum(int(d) for d in str(val))

    for val in range(1, n+1):
      v0 = convert(val)
      g[v0] += 1
        
    top = max(g.values())

    return sum(1 if c == top else 0 for c in g.values())
