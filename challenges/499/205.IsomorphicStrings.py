'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Constraints:

1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
'''

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    change = {}
    used = set()
    
    for i in range(len(s)):
      cs = s[i]
      ct = t[i]
      
      if cs not in change:
        if ct in used:
          return False
        
        change[cs] = ct
        used.add(ct)
        
      if ct != change[cs]:
        return False
    
    return True
        
  def isIsomorphic(self, s: str, t: str) -> bool:
    ls, lt = len(s), len(t)
    if ls != lt:
      return False
    
    d = {}
    added = set()
    
    for i in range(ls):
      if s[i] not in d:
        if t[i] in added:
          return False 
        
        d[s[i]] = t[i]
        added.add(t[i])
        
        continue
        
      if d[s[i]] != t[i]:
        return False
      
    return True
  