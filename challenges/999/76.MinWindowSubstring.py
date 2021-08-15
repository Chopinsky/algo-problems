'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''


from collections import defaultdict


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    ls, lt = len(s), len(t)
    if lt > ls:
      return ""
    
    rng = [0, lt-1]
    window = defaultdict(int)
    base = defaultdict(int)
    
    for char in t:
      base[char] += 1
    
    for char in s[:lt]:
      window[char] += 1
      
    def check() -> bool:
      for ch, cnt in base.items():
        if window[ch] < cnt:
          return False
        
      return True
      
    def reduce():
      start = rng[0]
      for i in range(start, ls):
        ch = s[i]
        rng[0] = i
        
        if ch in base and window[ch] == base[ch]:
          break
          
        window[ch] -= 1
      
      return
      
    if check():
      return s[:lt]
    
    curr = ""
    for char in s[lt:]:
      window[char] += 1
      rng[1] += 1
      
      if check():
        reduce()
        res = s[rng[0]:rng[1]+1]
        
        if not curr or len(curr) > len(res):
          curr = res
        
        # moves on 
        ch = s[rng[0]]
        window[ch] -= 1
        rng[0] += 1
        
        while rng[0] <= rng[1]:
          ch = s[rng[0]]
          if ch in base:
            break
            
          window[ch] -= 1
          rng[0] += 1
    
    # print(window, base)
    
    return curr