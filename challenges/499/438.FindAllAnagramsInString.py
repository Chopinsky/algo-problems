'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''


from typing import List


class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    ns, np = len(s), len(p)
    if ns < np:
      return []
    
    c0 = Counter(p)
    c1 = Counter(s[:np])
    ans = []
    
    def check(base, sub):
      for ch in base:
        if ch not in sub or base[ch] != sub[ch]:
          return False
        
      return True
    
    if check(c0, c1):
      ans.append(0)
      
    for i in range(np, ns):
      j = i-np
      pop_ch = s[j]
      add_ch = s[i]
      
      c1[pop_ch] -= 1
      c1[add_ch] = c1.get(add_ch, 0) + 1
      
      if check(c0, c1):
        ans.append(i-np+1)
        
    return ans
    
    
  def findAnagrams(self, s: str, p: str) -> List[int]:
    n = len(p)
    oa = ord('a')
    
    sd = [0] * 26
    pd = [0] * 26
    ans = []
    
    if len(s) < n:
      return ans
    
    for ch in p:
      pd[ord(ch) - oa] += 1
      
    for ch in s[:n]:
      sd[ord(ch) - oa] += 1
    
    for i in range(len(s)-n+1):
      match = True
      for j in range(26):
        if pd[j] != sd[j]:
          match = False
          break
          
      if match:
        ans.append(i)
        
      if i < len(s) - n:
        sd[ord(s[i])-oa] -= 1
        sd[ord(s[i+n])-oa] += 1
        
    return ans
  