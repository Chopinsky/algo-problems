'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

import math

class Solution:
  def firstUniqChar(self, s: str) -> int:
    c = Counter(s)
    for i, ch in enumerate(s):
      if ch in c and c[ch] == 1:
        return i
      
    return -1
    
    
  def firstUniqChar(self, s: str) -> int:
    dic = {}
    for i, ch in enumerate(s):
      if ch in dic:
        dic[ch] = math.inf
      else:
        dic[ch] = i
        
    idx = min(dic.values())    
    
    return -1 if idx == math.inf else idx


  def firstUniqChar(self, s: str) -> int:
    chars = [-1] * 26
    
    for i, ch in enumerate(s):
      idx = ord(ch) - ord('a')
      if chars[idx] == -1:
        chars[idx] = i
        continue
        
      if chars[idx] == -2:
        continue
      
      if chars[idx] >= 0:
        chars[idx] = -2
      
    pos = -1
    for p in chars:
      if p >= 0:
        pos = p if pos < 0 else min(p, pos)
    
    return pos