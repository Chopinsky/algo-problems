'''
3234. Count the Number of Substrings With Dominant Ones
'''

from bisect import bisect_left
from math import sqrt

class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    n = len(s)
    upper = sqrt(n)
    zeros = []
    
    for i in range(n):
      if s[i] == '0':
        zeros.append(i)
    
    count = 0
    nz = len(zeros)
    # print('init:', zeros)
    
    for i in range(n):
      j = bisect_left(zeros, i)
      if j >= len(zeros):
        count += n-i
        # print('tail:', n-i)
        continue

      # before seeing the first zero
      count += zeros[j]-i
      
      for k in range(j, nz):
        zc = k-j+1
        if zc > upper:
          break
          
        nxt_zero = n if k == nz-1 else zeros[k+1]
        oc = zc**2
        r = max(i+zc+oc, zeros[k]+1)
        
        if r <= nxt_zero:
          count += nxt_zero-r+1
          # print('add:', (i, r, nxt_zero), nxt_zero-r+1)
          
    return count
        