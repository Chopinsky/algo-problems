'''
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Example 3:

Input: palindrome = "aa"
Output: "ab"

Example 4:

Input: palindrome = "aba"
Output: "abb"

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
'''


class Solution:
  def breakPalindrome(self, p: str) -> str:
    n = len(p)
    if n == 1:
      return ''
    
    for i in range(n):
      if n%2 == 1 and 2*i+1 == n:
        continue
        
      if p[i] != 'a':
        return p[:i] + 'a' + p[i+1:]
      
    return p[:n-1] + 'b'


  def breakPalindrome(self, palindrome: str) -> str:
    n = len(palindrome)
    if n == 1:
      return ""
    
    ch = list(palindrome)
    for i in range(n):
      # can't get lower
      if i < n//2:
        if ch[i] != 'a':
          ch[i] = 'a'
          break
        else:
          continue
        
      # mid point
      if n%2 == 1 and 2*i+1 == n:
        continue
      
      if ch[i] == 'a':
        if i == n-1:
          ch[i] = 'b'
          
      else:
        ch[i] = 'a'
        break
      
    # print(ch)
    
    return "".join(ch)
  