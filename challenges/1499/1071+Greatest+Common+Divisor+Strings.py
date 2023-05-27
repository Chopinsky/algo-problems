'''
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''


class Solution:
  def gcdOfStrings(self, s1: str, s2: str) -> str:
    n1, n2 = len(s1), len(s2)
    if n1 < n2:
      s1, s2 = s2, s1
      n1, n2 = n2, n1
      
    if not s1.startswith(s2):
      return ""
    
    common = ""
    
    for ln in range(1, n2+1):
      if n1 % ln != 0 or n2 % ln != 0:
        continue
        
      c1, c2 = n1//ln, n2//ln
      base = s2[:ln]
      # print(ln, base)
      
      if c1*base != s1 or c2*base != s2:
        continue
        
      common = base
    
    return common
    