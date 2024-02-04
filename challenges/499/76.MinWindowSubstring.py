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
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

from collections import defaultdict, Counter
from bisect import bisect_left

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    tc = Counter(t)
    sc = defaultdict(list)
    chars = sorted(tc)
    
    for i in range(len(s)):
      sc[s[i]].append(i)
    
    for c in tc:
      if tc[c] > len(sc[c]):
        return ""
    
    def search(i: int):
      if s[i] not in tc:
        return -1
      
      tail = i
      for ch in chars:
        cnt = tc[ch]
        idx = bisect_left(sc[ch], i)
        if idx+cnt > len(sc[ch]):
          return -2
        
        tail = max(tail, sc[ch][idx+cnt-1])
        
      # print('search:', i, tail)
      return tail
      
    ans = s
    for i in range(len(s)):
      tail = search(i)
      if tail == -1:
        continue
        
      if tail == -2:
        break
      
      substr = s[i:tail+1]
      if len(substr) < len(ans) or (len(substr) == len(ans) and substr < ans):
        ans = substr
     
    return ans
    

  def minWindow(self, s: str, t: str) -> str:
    c = Counter(s)
    tgt = Counter(t)
    
    def match() -> bool:
      for ch, cnt in tgt.items():
        if ch not in c or cnt > c[ch]:
          return False
        
      return True
    
    if not match():
      return ''
      
    c = defaultdict(int)
    l, r, n = 0, 0, len(s)
    
    '''
    cnt = 0

    while r < n and cnt < len(tgt):
      ch = s[r]
      if ch in tgt:
        c[ch] += 1
        if c[ch] == tgt[ch]:
          cnt += 1
          
      r += 1
      
    while l < r:
      ch = s[l]
      if ch in tgt:
        if c[ch] == tgt[ch]:
          break
          
        c[ch] -= 1
        
      l += 1

    res = s[l:r]
    '''

    res = s
    # print(res, l, r)
    
    while r < n:
      # start by removing a must-have char from the substring
      while l < r and (s[l] not in tgt or match()):
        if s[l] in tgt:
          c[s[l]] -= 1
          
        l += 1
        
      # expand the substring until we have enough required chars
      while r < n and not match():
        if s[r] in tgt:
          c[s[r]] += 1
          
        r += 1
        
      # popping unnecessary chars that exceeds the expectations
      while l < r and (s[l] not in tgt or c[s[l]] > tgt[s[l]]):
        if s[l] in tgt:
          c[s[l]] -= 1
          
        l += 1
          
      # print('run', l, r, s[l:r])
      if match() and r-l < len(res):
        res = s[l:r]
    
    return res


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