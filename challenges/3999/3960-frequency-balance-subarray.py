'''
3960-frequency-balance-subarray
'''

from typing import List
from collections import Counter


class Solution:
  def getLength(self, nums: List[int]) -> int:
    mp = {v:i for i,v in enumerate(sorted(set(nums)))}
    m = len(mp)
    n = len(nums)
    ans = 1
    
    if m == 1:
      return n

    if m == n:
      return 1

    for i in range(n):
      if ans >= n-i:
        break

      counter = [0] * m
      fq = [0] * (n+1)
      mx = 0
      dis = 0
      
      for j in range(i, n):
        idx = mp[nums[j]]
        counter[idx] += 1

        if counter[idx] == 1:
          dis += 1
        else:
          fq[counter[idx]-1] -= 1

        fq[counter[idx]] += 1
        mx = max(mx, counter[idx])
        
        if dis == 1 or (mx%2 == 0 and fq[mx//2] > 0 and (fq[mx//2] + fq[mx]) == dis):
          ans=max(ans,j-i+1)

    return ans

  def getLength0(self, nums: List[int]) -> int:
    n = len(nums)

    def test(c, f) -> bool:
      if not c or not f:
        return False

      if len(c) == 1:
        return True

      if len(f) != 2:
        return False

      cand = list(f.keys())
      return (cand[0] == 2*cand[1]) or (cand[1] == 2*cand[0])

    def update_freq(f, curr: int, nxt: int):
      if curr > 0:
        f[curr] -= 1

      if not f[curr]:
        del f[curr]

      if nxt > 0:
        f[nxt] += 1

    def find(ln: int) -> bool:
      l, r = 0, ln-1
      c = Counter(nums[l:r+1])
      f = Counter(c.values())

      while r < n:
        if test(c, f):
          return True

        r += 1
        if r < n:
          rval = nums[r]
          c[rval] += 1
          update_freq(f, c[rval]-1, c[rval])

        lval = nums[l]
        c[lval] -= 1
        update_freq(f, c[lval]+1, c[lval])
        if not c[lval]:
          del c[lval]

        l += 1

      return False

    for ln in range(n, 2, -1):
      if find(ln):
        return ln
        
    return 1
