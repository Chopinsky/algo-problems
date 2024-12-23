'''
3377. Digit Operations to Make Two Integers Equal
'''

from heapq import heappush, heappop


top = 10001
siv = [i for i in range(top)]
for v0 in range(2, top):
  if siv[v0] < v0:
    continue
    
  for v1 in range(v0*v0, top, v0):
    siv[v1] = v0
    
primes = set(val for val in siv if siv[val] == val and val > 1)

class Solution:
  def minOperations(self, n: int, m: int) -> int:
    if n in primes or m in primes:
      return -1
    
    seen = {n:n}
    stack = [(n, n)]
    ln = len(str(n))
    mult = [10**i for i in range(ln)][::-1]
    # print('init:', ln, mult)
    
    while stack:
      cost, val = heappop(stack)
      if val == m:
        return cost
      
      sval = str(val)
      sv = [0]*(ln-len(sval)) + [int(d) for d in list(sval)]
      # print('iter:', val, sv)
      
      for i in range(ln):
        # can decrease
        if sv[i] > 0:
          v1 = val - mult[i]
          c1 = cost + v1
          if v1 not in primes and v1 >= mult[0] and (v1 not in seen or c1 < seen[v1]):
            seen[v1] = c1
            heappush(stack, (c1, v1))
            
        # can increase
        if sv[i] < 9:
          v2 = val + mult[i]
          c2 = cost + v2
          if v2 not in primes and v2 >= mult[0] and (v2 not in seen or c2 < seen[v2]):
            seen[v2] = c2
            heappush(stack, (c2, v2))
      
    return -1
    