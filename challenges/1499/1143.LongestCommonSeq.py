'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''


from collections import defaultdict
from bisect import bisect_left

class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    n1, n2 = len(text1), len(text2)
    if n1 > n2:
      text1, text2 = text2, text1
      n1, n2 = n2, n1
      
    prev, curr = [0]*n2, [0]*n2
    
    for i in range(n1):
      for j in range(n2):
        if text1[i] == text2[j]:
          curr[j] = 1 + (prev[j-1] if j > 0 else 0)
          
        else:
          curr[j] = max(curr[j-1] if j > 0 else 0, prev[j])
          
      curr, prev = prev, curr
    
    return max(prev)
        
        
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    lcs = [[0]*n for _ in range(m)]
    longest = 0
    
    for i in range(m):
      for j in range(n):
        if i > 0:
          lcs[i][j] = max(lcs[i][j], lcs[i-1][j])
          
        if j > 0:
          lcs[i][j] = max(lcs[i][j], lcs[i][j-1])
          
        if text1[i] == text2[j]:
          lcs[i][j] = max(lcs[i][j], 1 + (0 if i == 0 or j == 0 else lcs[i-1][j-1]))
          
        longest = max(longest, lcs[i][j])
    
    return longest
    

  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    if m > n:
      m, n = n, m
      text1, text2 = text2, text1
      
    # print(text1, text2)
    char_pos = defaultdict(list)
    for i, c in enumerate(text2):
      char_pos[c].append(i)

    seq = []
    
    for i in range(m):
      for idx in char_pos[text1[i]][::-1]:
        if not seq or idx > seq[-1]:
          seq.append(idx)
          
        else:
          j = bisect_left(seq, idx)
          seq[j] = idx
                
    # print(seq)
    
    return len(seq)
  
      
  def longestCommonSubsequence0(self, text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    lcs = [[0]*(n+1) for _ in range(m+1)]
    long = 0
    
    for i in range(m):
      for j in range(n):
        if text1[i] == text2[j]:
          lcs[i+1][j+1] = lcs[i][j] + 1
        else:
          lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])
        
        long = max(long, lcs[i+1][j+1])
    
    # for r in lcs:
    #   print(r)
      
    return long
  