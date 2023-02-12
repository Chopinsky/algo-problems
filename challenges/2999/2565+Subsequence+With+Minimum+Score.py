'''
2565. Subsequence With the Minimum Score

You are given two strings s and t.

You are allowed to remove any number of characters from the string t.

The score string is 0 if no characters are removed from the string t, otherwise:

Let left be the minimum index among all removed characters.
Let right be the maximum index among all removed characters.
Then the score of the string is right - left + 1.

Return the minimum possible score to make t a subsequence of s.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abacaba", t = "bzaa"
Output: 1
Explanation: In this example, we remove the character "z" at index 1 (0-indexed).
The string t becomes "baa" which is a subsequence of the string "abacaba" and the score is 1 - 1 + 1 = 1.
It can be proven that 1 is the minimum score that we can achieve.
Example 2:

Input: s = "cde", t = "xyz"
Output: 3
Explanation: In this example, we remove characters "x", "y" and "z" at indices 0, 1, and 2 (0-indexed).
The string t becomes "" which is a subsequence of the string "cde" and the score is 2 - 0 + 1 = 3.
It can be proven that 3 is the minimum score that we can achieve.

Constraints:

1 <= s.length, t.length <= 10^5
s and t consist of only lowercase English letters.
'''

from collections import defaultdict
from bisect import bisect_right, bisect_left


class Solution:
  '''
  the question is essentially asking that if prefix t[:left] is a subsequence to s 
  which matches s[:left_idx], then what's the longest suffix t[right:] such that it's
  a subsequence to s[left_idx:], this is because we can delete all characters in the
  the [left, right] range from t without affecting the final score, so just do it
  to maximize the length of t[right:]
  '''
  def minimumScore(self, s: str, t: str) -> int:
    pos = defaultdict(list)
    ns = len(s)
    nt = len(t)
    
    for i, ch in enumerate(s):
      pos[ch].append(i)
      
    # print(pos)
    lstack = [-1] * nt
    rstack = [-1] * nt
    curr = -1
    score = nt
    
    for l in range(nt):
      ch = t[l]
      if ch not in pos or curr > pos[ch][-1]:
        break
        
      idx = bisect_right(pos[ch], curr)
      if idx >= len(pos[ch]):
        break
        
      curr = pos[ch][idx]
      lstack[l] = curr
      score = min(score, nt-l-1)
      
    curr = ns
    for r in range(nt-1, -1, -1):
      ch = t[r]
      if ch not in pos or curr < pos[ch][0]:
        break
        
      idx = bisect_left(pos[ch], curr)-1
      if idx < 0:
        break
        
      curr = pos[ch][idx]
      rstack[r] = curr
      score = min(score, r)
      
    # print(lstack, rstack, score)
    l, r = 0, 0
    
    while l < nt and lstack[l] != -1:
      while r < nt and (rstack[r] == -1 or rstack[r] <= lstack[l]):
        r += 1
        
      if l <= r < nt:
        # print('new match:', l, r)
        score = min(score, 0 if r <= l+1 else (r-l-1))
        
      l += 1
    
    return score
    