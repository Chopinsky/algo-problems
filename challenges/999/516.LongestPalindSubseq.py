'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''


from functools import lru_cache


class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    @lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i > j:
        return 0
      
      if i == j:
        return 1
      
      if i+1 == j:
        return 2 if s[i] == s[j] else 1
      
      if s[i] == s[j]:
        return 2 + dp(i+1, j-1)
      
      return max(dp(i+1, j), dp(i, j-1))
    
    return dp(0, len(s)-1)
  