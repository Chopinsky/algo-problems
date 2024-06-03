'''
2486. Append Characters to String to Make Subsequence

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
Example 3:

Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.

Constraints:

1 <= s.length, t.length <= 10^5
s and t consist only of lowercase English letters.
'''

from collections import defaultdict
from bisect import bisect_right

class Solution:
  def appendCharacters(self, s: str, t: str) -> int:
    pos = defaultdict(list)
    ls, lt = len(s), len(t)
    last = -1
    
    for i in range(ls):
      ch = s[i]
      pos[ch].append(i)
    
    for i in range(lt):
      ch = t[i]
      if ch not in pos:
        return lt-i
      
      cand = pos[ch]
      j = bisect_right(cand, last)
      if j >= len(cand):
        return lt-i
      
      last = cand[j]
      
    return 0
        
  def appendCharacters(self, s: str, t: str) -> int:
    i = 0
    for ch in s:
      if ch == t[i]:
        i += 1
        
      if i >= len(t):
        break
        
    return len(t) - i
  