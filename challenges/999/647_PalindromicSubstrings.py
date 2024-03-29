'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''

class Solution:
  def countSubstrings(self, s: str) -> int:
    n = len(s)
    
    def count_odd(i: int) -> int:
      cnt = 1
      j = i+1
      i -= 1
      
      while i >= 0 and j < n and s[i] == s[j]:
        cnt += 1
        i -= 1
        j += 1
        
      return cnt
      
    def count_even(i: int) -> int:
      cnt = 0
      if i >= n-1:
        return cnt
      
      j = i+1
      
      while i >= 0 and j < n and s[i] == s[j]:
        cnt += 1
        i -= 1
        j += 1
        
      return cnt
      
    total = 0
    for i in range(n):
      total += count_odd(i) + count_even(i)
      
    return total
  

  def countSubstrings(self, s: str) -> int:
    n = len(s)
    
    def count_substr(x: int, y: int) -> int:
      count = 0
      while x >= 0 and y < n and s[x] == s[y]:
        count += 1
        x -= 1
        y += 1
      
      return count
      
    total = 0
    for i in range(n):
      total += count_substr(i, i)
      total += count_substr(i, i+1)
      
    return total
      