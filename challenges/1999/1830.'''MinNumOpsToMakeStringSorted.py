'''
You are given a string s (0-indexed)​​​​​​. You are asked to perform the following operation on s​​​​​​ until you get a sorted string:

Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
Swap the two characters at indices i - 1​​​​ and j​​​​​.
Reverse the suffix starting at index i​​​​​​.
Return the number of operations needed to make the string sorted. Since the answer can be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "cba"
Output: 5
Explanation: The simulation goes as follows:
Operation 1: i=2, j=2. Swap s[1] and s[2] to get s="cab", then reverse the suffix starting at 2. Now, s="cab".
Operation 2: i=1, j=2. Swap s[0] and s[2] to get s="bac", then reverse the suffix starting at 1. Now, s="bca".
Operation 3: i=2, j=2. Swap s[1] and s[2] to get s="bac", then reverse the suffix starting at 2. Now, s="bac".
Operation 4: i=1, j=1. Swap s[0] and s[1] to get s="abc", then reverse the suffix starting at 1. Now, s="acb".
Operation 5: i=2, j=2. Swap s[1] and s[2] to get s="abc", then reverse the suffix starting at 2. Now, s="abc".
Example 2:

Input: s = "aabaa"
Output: 2
Explanation: The simulation goes as follows:
Operation 1: i=3, j=4. Swap s[2] and s[4] to get s="aaaab", then reverse the substring starting at 3. Now, s="aaaba".
Operation 2: i=4, j=4. Swap s[3] and s[4] to get s="aaaab", then reverse the substring starting at 4. Now, s="aaaab".
 

Constraints:

1 <= s.length <= 3000
s​​​​​​ consists only of lowercase English letters.
'''


from functools import lru_cache
from collections import defaultdict
from typing import List
import bisect


class Solution:
  '''
  the problem is essentially asking how many permutations to take to transform a partially sorted
  string to a fully sorted string, say `daabccd`, to `aabccdd`, since 1 operation will make 1 
  permutation: `daabccd` ==(in 1 op)==> `cddcbaa`.
  '''
  def makeStringSorted0(self, s: str) -> int:
    mod = 1_000_000_007
    n = len(s)
    count = 0
    
    @lru_cache(None)
    def factorial(val: int) -> int:
      return 1 if val <= 1 else (val * factorial(val-1)) % mod
    
    @lru_cache(None)
    def inv(val: int) -> int:
      return pow(factorial(val), mod-2, mod)
    
    cnt = [0] * 26
    for i in range(n-1, -1, -1):
      idx = ord(s[i]) - ord('a')
      cnt[idx] += 1
      
      ops = sum(cnt[:idx]) * factorial(n-i-1)
      for j in range(26):
        ops = (ops * inv(cnt[j])) % mod
        
      count = (count + ops) % mod
      
    return count
    
  
  def makeStringSorted(self, s: str) -> int:
    mod = 1_000_000_007
    n = len(s)
      
    # if already sorted, done
    if n <= 1 or ''.join(sorted(s)) == s:
      return 0

    if n == 2:
      return 0 if s[0] <= s[1] else 1
    
    @lru_cache(None)
    def factorial(val: int) -> int:
      return 1 if val <= 1 else (val * factorial(val-1)) % mod
    
    @lru_cache(None)
    def inv(val: int) -> int:
      return pow(factorial(val), mod-2, mod)
      
    def calc_base(total: int, values: List[int]) -> int:
      base = factorial(total)
      for val in values:
        base = (base * inv(val)) % mod
      
      return base
    
    count = 0
    chars = [s[-1]]
    
    c = defaultdict(int)
    c[s[-1]] += 1
    total = 1

    for i in range(n-2, -1, -1):
      # insert the new char
      last = chars[0]
      if s[i] not in c:
        bisect.insort(chars, s[i])
      
      # adding this char to the char counter
      c[s[i]] += 1
      total += 1
      
      # this char is good, no op required
      if s[i] <= last:
        continue
        
      idx = 0
      base = calc_base(total-1, c.values())
      # print(i, s[i], chars)
      
      while idx < len(chars) and chars[idx] < s[i]:
        count = (count + base * c[chars[idx]]) % mod
        idx += 1
  
    # print(chars, c)
    return count
    