'''
3310. Remove Methods From Project
'''

from typing import List
from collections import defaultdict


class Solution:
  def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
    e = defaultdict(list)
    p = defaultdict(set)
    for a, b in invocations:
      e[a].append(b)
      p[b].add(a)
      
    curr, nxt = [k], []
    susp = set(curr)
    outs = set()
    
    while curr:
      for u in curr:
        outs |= p[u]
        for v in e[u]:
          if v in susp:
            continue
            
          nxt.append(v)
          susp.add(v)
          
      curr, nxt = nxt, curr
      nxt.clear()
      
    outs -= susp
    rem = set(i for i in range(n))
    # print('done:', susp, outs)
    
    return list(rem) if outs else list(rem-susp)
    