'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
'''


class Solution:
  '''
  idea is to create the kmp jump table and check what's the longest common substring at `kmp[-1]`
  '''
  def longestPrefix(self, s: str) -> str:
    n = len(s)
    if s[:-1] == s[1:]:
      return s[:-1]
    
    # build the kmp jump table
    kmp, j = [0] * n, 0
    for i in range(1, n):
      while j > 0 and s[j] != s[i]:
        j = kmp[j-1]
        
      if s[j] == s[i]:
        j += 1
        
      kmp[i] = j
      
    ln = kmp[-1]
    # print(kmp)
    
    return s[:ln]
  