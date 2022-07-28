'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

from typing import Counter


class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    c0 = Counter(s)
    c1 = Counter(t)
    
    if set(c0) != set(c1):
      return False
    
    for ch in c0:
      if c0[ch] != c1[ch]:
        return False
      
    return True


  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    ch = [0]*26
    
    for i in range(len(s)):
      si, ji = ord(s[i]) - ord('a'), ord(t[i]) - ord('a')
      ch[si] += 1
      ch[ji] -= 1
      
    for val in ch:
      if val != 0:
        return False
      
    return True
  