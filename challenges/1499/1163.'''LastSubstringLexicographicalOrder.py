'''
Given a string s, return the last substring of s in lexicographical order.

Example 1:

Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:

Input: s = "leetcode"
Output: "tcode"

Constraints:

1 <= s.length <= 4 * 105
s contains only lowercase English letters.
'''

class Solution:
  def lastSubstring(self, s: str) -> str:
    n = len(s)
    if n <= 1:
      return s
    
    if s == s[0]*n:
      return s
    
    top_char = s[0]
    idx = 0
    i = 0
    
    while i < n-1:
      i += 1
      
      # larger char, refreshing the pointers
      if s[i] > top_char:
        top_char = s[i]
        idx = i
        continue
        
      # continuing top_char, this position won't be better
      # than the previous position, e.g. `tttb` > `ttb*` and `tttt` > `ttt`, 
      # skip it; and if current char is smaller, no need to update anything,
      # keep the winner running
      if s[i] == s[i-1] or s[i] < top_char:
        continue
        
      # the situation where s[i] == top_char; here`j` is the offset 
      # pointer to the characters we're comparing
      j = 1

      # find the first char that's different, or before the current char,
      # this is because the current char is the largest in s[idx:i+1], meaning
      # s[idx:] will be at least in the same order lexicographically, but it
      # has a better chance to be better because it's longer
      while i+j < n and s[i+j] == s[idx+j] and idx+j < i:
        j += 1

      # finding a new larger char, update the substring pointer
      if i+j < n and s[i+j] > s[idx+j]:
        idx = i

      # we have compared `j-1` extra chars, which has warrented us the best 
      # answer in s[i:i+j-1]
      i += j-1
        
    return s[idx:]
    
  def lastSubstring0(self, s: str) -> str:
    n = len(s)
    if n <= 1:
      return s
    
    if s == s[0]*n:
      return s

    top_char = max(s)
    ans = ''
    prev = -2
    
    for i in range(n):
      # only cares about substrings starting with the largest char
      # that we have found
      if s[i] != top_char:
        continue
        
      # `zzzb` is larger than `(z)zzb`, meaning if we're seeing continuing
      # substring of `top_char`, we skip because eventually the current
      # `ans` is the lexicographically largest one 
      if i == prev+1:
        prev += 1
        continue
        
      # only need to compare the next 26 characters, which will cover all 
      if s[i:i+26] > ans:
        ans = s[i:]
        
      # update the prev substring's starting index
      prev = i
        
    return ans
  
