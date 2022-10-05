'''
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
'''

class Solution:
  def strStr(self, s: str, p: str) -> int:
    m = len(s)
    n = len(p)
    
    if (n > m) or (n == m and s != p):
      return -1
    
    for i in range(m):
      if m-i < n:
        break
        
      if s[i] != p[0]:
        continue
        
      if s[i:i+n] == p:
        return i
    
    return -1
    