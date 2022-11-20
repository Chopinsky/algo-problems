'''
2478. Number of Beautiful Partitions

You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.

A partition of s is called beautiful if:

s is partitioned into k non-intersecting substrings.
Each substring has a length of at least minLength.
Each substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.
Return the number of beautiful partitions of s. Since the answer may be very large, return it modulo 109 + 7.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "23542185131", k = 3, minLength = 2
Output: 3
Explanation: There exists three ways to create a beautiful partition:
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"
Example 2:

Input: s = "23542185131", k = 3, minLength = 3
Output: 1
Explanation: There exists one way to create a beautiful partition: "2354 | 218 | 5131".
Example 3:

Input: s = "3312958", k = 3, minLength = 1
Output: 1
Explanation: There exists one way to create a beautiful partition: "331 | 29 | 58".

Constraints:

1 <= k, minLength <= s.length <= 1000
s consists of the digits '1' to '9'.
'''

from functools import lru_cache
from bisect import bisect_left


class Solution:
  def beautifulPartitions(self, s: str, k: int, min_len: int) -> int:
    n = len(s)
    if n < k*min_len:
      return 0
    
    primes = {'2', '3', '5', '7'}
    if s[0] not in primes or s[-1] in primes:
      return 0
    
    head = [0]
    mod = 10**9 + 7
    
    for i in range(1, n):
      if s[i] in primes and s[i-1] not in primes and (n-i) >= min_len:
        head.append(i)
    
    m = len(head)
    # print(m, head)
    
    @lru_cache(None)
    def part(i: int, rem: int) -> int:
      if i >= m or rem <= 0:
        return 0
      
      if rem == 1:
        # print('1:', i, rem)
        return 1
      
      # get the next head
      j = bisect_left(head, head[i]+min_len)
      # print('bisect:', i, rem, j, head[i]+min_len)
      
      # no more valid partitions beyond this point
      if j >= m:
        return 0
      
      # one partition and done
      if rem == 2:
        # print('2:', i, rem, m-j)
        return (m-j) % mod
      
      count = 0
      for k in range(j, m):
        nxt = part(k, rem-1)
        if nxt == 0:
          break
          
        # print('iter:', i, rem, k)
        count = (count + nxt) % mod
      
      # print('final:', i, rem, count)
      return count
      
    # return 0
    return part(0, k)
  