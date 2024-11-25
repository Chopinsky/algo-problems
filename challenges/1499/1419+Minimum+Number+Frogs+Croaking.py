'''
1419. Minimum Number of Frogs Croaking

"croakcroak"
"crcoakroak"
"croakcrook"
"crocakcroraoakk"
"ccckkk"
'''

from collections import defaultdict
from heapq import heappush, heappop


class Solution:
  def minNumberOfFrogs(self, c: str) -> int:
    chars = set('croak')
    if any(ch not in chars for ch in c):
      return -1
    
    idx = defaultdict(list)
    for i, ch in enumerate(c):
      idx[ch].append(i)
      chars.discard(ch)
      
    if len(chars) > 0:
      return -1
    
    # print('init:', idx)
    calls = len(idx['c'])
    if any(len(lst) != calls for lst in idx.values()):
      return -1
    
    crogs = [-1]
    
    for i in range(calls):
      if crogs[0] < idx['c'][i]:
        heappop(crogs)
      
      prev = -1
      for ch in 'croak':
        curr = idx[ch][i]
        if curr <= prev:
          # invalid case
          return -1
        
        prev = curr
        
      heappush(crogs, prev)
    
    return len(crogs)
         