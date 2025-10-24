'''
2048. Next Greater Numerically Balanced Number

An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.

Constraints:

0 <= n <= 10^6

Test cases:
1
1000
3000
1000000
99999
188
'''

from functools import lru_cache
from typing import List, Tuple

class Solution:
  def nextBeautifulNumber(self, n: int) -> int:
    cnt = [i for i in range(10)]
    sz = len(str(n))

    def dfs(n: int, val: int, sz: int) -> int:
      if sz == 0:
        for i in range(1, 10):
          if cnt[i] != i and cnt[i] != 0:
            return 0

        return val if val > n else 0

      res = 0
      for i in range(1, 10):
        if cnt[i] > 0 and cnt[i] <= sz:
          cnt[i] -= 1
          res = dfs(n, val*10 + i, sz-1)
          cnt[i] += 1

        if res > 0:
          break

      return res

    res = dfs(n, 0, sz)
    if res > 0:
      return res

    return dfs(0, 0, sz+1)

  def nextBeautifulNumber(self, n: int) -> int:
    base = str(n)
    ln = len(base)
  
    @lru_cache(None)
    def find_cand(rem: int, curr: int):
      if rem < curr or curr > 9:
        return tuple()
      
      if rem == curr:
        return tuple([(curr, )])
      
      res = list(find_cand(rem, curr+1))
      for lst in find_cand(rem-curr, curr+1):
        if len(lst) > 0:
          res.append((curr, ) + lst)
          
      return tuple(res)
    
    def search(src: List, idx: int, mask: int, is_equal: True):
      if idx >= ln:
        return '', not is_equal
      
      if not is_equal:
        return ''.join(src[i] for i in range(ln) if (1<<i)&mask == 0), True
      
      for i in range(ln):
        # used
        if (1<<i) & mask > 0:
          continue
          
        # smaller
        if src[i] < base[idx]:
          continue
          
        if src[i] == base[idx]:
          val, found = search(src, idx+1, mask|(1<<i), is_equal)
          # if idx == 0:
          #   print('iter-1:', i, val, found)
        else:
          val, found = search(src, idx+1, mask|(1<<i), False)
          # if idx == 0:
          #   print('iter-2:', i, val, found)
          
        if found:
          return src[i] + val, True
        
      return '', False
    
    def gen_val(cand: Tuple):
      arr = ''.join(str(d)*d for d in cand)
      if len(cand) == 1 or len(arr) > ln:
        res = int(arr)
        return float('inf') if res <= n else res
      
      val, found = search(arr, 0, 0, True)
      # print('gen:', cand, arr, val)
      if found:
        return int(val)
      
      return float('inf')
      
    res = int('6'*6)
    for l in range(ln, min(10, ln+2)):
      val = min(gen_val(digits) for digits in find_cand(l, 1))
      res = min(res, val)
      
    return res
        