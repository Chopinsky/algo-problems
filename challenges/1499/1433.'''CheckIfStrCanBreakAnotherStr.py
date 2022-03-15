'''
Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

 

Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false 
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true
 

Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.
'''


from collections import Counter
from bisect import bisect_left


class Solution:
  def checkIfCanBreak(self, s1: str, s2: str) -> bool:
    c1, c2 = Counter(s1), Counter(s2)
    cand1 = sorted(c1)
    cand2 = sorted(c2)
    
    def can_break(src1, src2, d1, d2) -> bool:
      for ch1 in src1[::-1]:
        cnt = d1[ch1]
        idx = bisect_left(src2, ch1)
        
        while cnt > 0 and idx < len(src2):
          ch2 = src2[idx]
          remove = min(cnt, d2[ch2])
          d2[ch2] -= remove
          cnt -= remove
          idx += 1
          
        if cnt > 0:
          # print(src1, src2)
          return False
        
      return True
    
    return can_break(cand1, cand2, c1.copy(), c2.copy()) or can_break(cand2, cand1, c2, c1)
    