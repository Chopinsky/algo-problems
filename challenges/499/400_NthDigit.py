'''
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 

Constraints:

1 <= n <= 2^31 - 1
'''

from functools import lru_cache


class Solution:
  def findNthDigit0(self, n: int) -> int:
    s, last = 0, 0
    p = 0
    
    while s < n:
      add = 9 * (10 ** p) * (p + 1)
      last = s
      s += add
      p += 1

    need = n - last
    more = (need // p, need % p)
    if more[1] == 0:
      return int(str(10**(p-1) - 1 + more[0])[-1])
    
    d = more[1] - 1
    return int(str(10**(p-1) + more[0])[d])
  
  
  def findNthDigit(self, k: int) -> int:
    if k < 10:
      return k % 10
    
    @lru_cache(None)
    def count(n: int) -> int:
      if n < 10:
        return n
      
      s = str(n)
      m = len(s)
      if s == '9' * m:
        return m * int('9' + '0' * (m-1)) + count(int('9' * (m-1)))
      
      base = int('1' + '0' * (m-1))
      return m * (n-base+1) + count(int('9' * (m-1)))
    
    l, r = 10, k
    # print('init', l, r, count(k))  
    
    while l < r:
      mid = (l + r) // 2
      cnt = count(mid)
      sm = str(mid)
      ln = len(sm)
      
      # print('bi', mid, cnt)
      if cnt-ln+1 <= k <= cnt:
        return sm[ln-cnt+k-1]
      
      if k < cnt-ln+1:
        r = mid - 1
      else:
        l = mid + 1
      
    # print(l, r, count(l))
    cnt = count(l)
    sm = str(l)
    ln = len(sm)
    
    return sm[ln-cnt+k-1]
  