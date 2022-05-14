'''
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.
 

Constraints:

1 <= s.length <= 10^4
s consists of lowercase English letters.
'''

import math
from collections import defaultdict
from typing import List


class Solution:
  def largestVariance(self, s: str) -> int:
    n = len(s)
    if len(set(s)) == n:
      return 0
    
    pos = defaultdict(list)
    chars = 'abcdefghijklmnopqrstuvwxyz'
    
    for i, ch in enumerate(s):
      pos[ch].append(i)
      
    def find_var(p0: List[int], p1: List[int]) -> int:
      i, j = 0, 0
      c0, c1 = 0, 0
      
      b0, b1 = [], []
      v0 = [math.inf, -math.inf]
      v1 = [math.inf, -math.inf]
      vc0 = [math.inf, -math.inf]
      vc1 = [math.inf, -math.inf]
      var = 0
      
      while i < len(p0) or j < len(p1):
        if j >= len(p1) or (i < len(p0) and p0[i] < p1[j]):
          c0 += 1
          i += 1
          ch = 0
          v1[0], v1[1] = vc1
          
        else:
          c1 += 1
          j += 1
          ch = 1
          v0[0], v0[1] = vc0

        # balance check 
        bal = c0 - c1
        if c0 > 0 and c1 > 0:
          var = max(var, abs(bal))
          
          if bal >= 0:
            if v0[0] != math.inf and bal > v0[0]:
              var = max(var, abs(bal - v0[0]) + 1)
              
            if v1[0] != math.inf and bal > v1[0]:
              var = max(var, abs(bal - v1[0]))
            
          elif bal <= 0:
            if v0[1] != -math.inf and bal < v0[1]:
              var = max(var, abs(bal - v0[1]))
              
            if v1[1] != -math.inf and bal < v1[1]:
              var = max(var, abs(bal - v1[1]) + 1)
          
          # print(bal, c0, c1, v0, v1, var)
          if ch == 0:
            vc0[0] = min(vc0[0], bal)
            vc0[1] = max(vc0[1], bal)

          else:
            vc1[0] = min(vc1[0], bal)
            vc1[1] = max(vc1[1], bal)
        
      # no p1 appears later
      if v0[0] == math.inf:
        var = max(var, c1-1)
        
      # no p0 appears later
      if v1[0] == math.inf:
        var = max(var, c0-1)
        
      return var
      
    max_var = 0
    for i in range(25):
      for j in range(i+1, 26):
        a, b = chars[i], chars[j]
        if a not in pos or b not in pos:
          continue
          
        max_var = max(max_var, find_var(pos[a], pos[b]))
        
    return max_var
    