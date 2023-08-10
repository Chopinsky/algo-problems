'''
1081. Smallest Subsequence of Distinct Characters

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
'''


class Solution:
  def smallestSubsequence(self, s: str) -> str:
    last = {c: i for i, c in enumerate(s)}
    stack = []
    
    for i, c in enumerate(s):
      # already seen and it's at rightful place
      if c in stack:
        continue
        
      # we will see this to-be-popped char again
      while stack and c < stack[-1] and i < last[stack[-1]]:
        stack.pop()
        
      stack.append(c)
      
    return ''.join(stack)
  