'''
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 
Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 10^5
s consists of only lowercase English letters.
'''


from collections import defaultdict
from bisect import bisect_right


class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
    pos = defaultdict(list)
    for i, ch in enumerate(s):
      pos[ch].append(i)
    
    count = 0
    chars = list(pos)
    
    for c0 in chars:
      if len(pos[c0]) < 2:
        continue
        
      # print(c0)
      for c1 in chars:
        if c0 == c1:
          count += 1 if len(pos[c0]) > 2 else 0
          
        else:
          idx = bisect_right(pos[c1], pos[c0][0])
          if idx < len(pos[c1]) and pos[c1][idx] < pos[c0][-1]:
            count += 1
    
    return count
  