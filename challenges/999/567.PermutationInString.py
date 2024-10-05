'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
'''

from collections import Counter


class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
      return False
    
    c1 = Counter(s1)
    c2 = Counter(s2[:n1])
    
    def check(c1, c2):
      for ch, cnt in c1.items():
        if ch not in c2 or c2[ch] != cnt:
          return False
        
      return True
    
    if check(c1, c2):
      return True
      
    for i in range(n1, n2):
      remove = s2[i-n1]
      addition = s2[i]
      
      c2[remove] -= 1
      c2[addition] += 1
      
      if check(c1, c2):
        return True
    
    return False
        
  def checkInclusion(self, s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
      return False
    
    base = Counter(s1)
    running = Counter(s2[:n1])
    
    def compare(base, running):
      for ch in base:
        if ch not in running or running[ch] != base[ch]:
          return False
        
      return True
    
    if compare(base, running):
      return True
    
    # print('init:', running)
    for i in range(n1, n2):
      pop_ch = s2[i-n1]
      add_ch = s2[i]
      running[pop_ch] -= 1
      running[add_ch] = running.get(add_ch, 0) + 1
      # print(i, s2[i], running)
      
      if compare(base, running):
        # print(i, s2[i], base, running)
        return True
      
    return False
    