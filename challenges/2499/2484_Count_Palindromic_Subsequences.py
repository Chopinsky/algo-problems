'''
2484. Count Palindromic Subsequences

Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.

Note:

A string is palindromic if it reads the same forward and backward.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:

Input: s = "103301"
Output: 2
Explanation: 
There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301". 
Two of them (both equal to "10301") are palindromic.
Example 2:

Input: s = "0000000"
Output: 21
Explanation: All 21 subsequences are "00000", which is palindromic.
Example 3:

Input: s = "9999900000"
Output: 2
Explanation: The only two palindromic subsequences are "99999" and "00000".

Constraints:

1 <= s.length <= 10^4
s consists of digits.
'''

from collections import defaultdict


class Solution:
  def countPalindromes(self, s: str) -> int:
    rc, rs = defaultdict(int), defaultdict(int)
    lc, ls = defaultdict(int), defaultdict(int)
    n = len(s)
    
    # add new right sequences into the right side store
    for i in range(n-1, 1, -1):
      v0 = s[i]
      for v1, c1 in rc.items():
        rs[v0+v1] += c1
        
      rc[v0] += 1
      
    # print(rc, rs)
    total = 0
    mod = 10**9 + 7
    
    for i in range(n-2):
      v0 = s[i]
      if i >= 2:
        # pop right sequences
        rc[v0] -= 1
        for v1, c1 in rc.items():
          rs[v0+v1] -= c1

        # print(i, v0, lc, ls, rc, rs)
        for s1, c1 in ls.items():
          s2 = s1[::-1]
          if s2 in rs and rs[s2] > 0:
            total = (total + c1*rs[s2]) % mod

      # add new left sequences into the left side store
      for v1, c1 in lc.items():
        ls[v1+v0] += c1
        
      lc[v0] += 1
      
    return total
    