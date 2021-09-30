'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10 ** 4
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
'''

from collections import defaultdict
from bisect import bisect_right

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    seq = defaultdict(list)
    for i, ch in enumerate(t):
      seq[ch].append(i)

    # print(seq)
    last = -1

    for ch in s:
      if ch not in seq:
        return False

      positions = seq[ch]
      idx = bisect_right(positions, last)

      if idx < len(positions) and positions[idx] == last:
        idx += 1

      # print(ch, last, idx, positions)

      if idx >= len(positions):
        return False

      last = positions[idx]

    return True
