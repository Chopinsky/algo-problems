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
    
    # a refined and easier to understan solution
    def find_var(p0: List[int], p1: List[int]) -> int:
      # pointers and states
      i, j = 0, 0
      bal, var = 0, 0
      
      # the high / low balance states
      high, max_bal = -math.inf, -math.inf
      low, min_bal = math.inf, math.inf
      
      while i < len(p0) or j < len(p1):
        # append the p0 char
        if j >= len(p1) or (i < len(p0) and p0[i] < p1[j]):
          bal += 1
          i += 1
          
          # update the usable high and the maximum high
          high = max_bal
          max_bal = max(max_bal, bal)
          
          # if p0 has shown up before that can be trimmed
          if low != math.inf and bal > low:
            var = max(var, abs(bal - low))
          
        # append the p1 char
        else:
          bal -= 1
          j += 1
          
          # update the usable low and the minimum low
          low = min_bal
          min_bal = min(min_bal, bal)
          
          # if p1 has shown up before that can be trimmed
          if high != -math.inf and bal < high:
            var = max(var, abs(bal - high))
      
        # if a 2-chars substring has been formed, check if 
        # the entire substring is the optimal solution
        if i > 0 and j > 0:
          var = max(var, abs(bal))
        
      return var
    
    max_var = 0
    for i in range(25):
      for j in range(i+1, 26):
        a, b = chars[i], chars[j]
        if a not in pos or b not in pos:
          continue
          
        max_var = max(max_var, find_var(pos[a], pos[b]))
        
    return max_var
    