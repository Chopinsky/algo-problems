'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
'''


class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
      return 0
    
    i, j = 0, 1
    long = 1
    n = len(s)
    chars = set([s[0]])
    
    while j < n:
      while j < n and s[j] not in chars:
        chars.add(s[j])
        j += 1
        
      long = max(long, j-i)
      if j >= n:
        break
        
      while i < j and s[i] != s[j]:
        chars.discard(s[i])
        i += 1
        
      if i < n:
        chars.discard(s[i])
        i += 1
        
      # print(i, j)
      
    return long
