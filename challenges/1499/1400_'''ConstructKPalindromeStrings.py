'''
1400. Construct K Palindrome Strings

Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= 10^5
'''

from collections import Counter


class Solution:
  '''
  the trick is that a palindrome string can have at most 1 char with odd char counts; hence
  if we have m <= k number of odd counts of characters, we can divide the odd counted numbers
  into the k-strings; otherwise, we will be left with odd count chars that will cause rule
  violations.
  '''
  def canConstruct(self, s: str, k: int) -> bool:
    if len(s) < k:
      return False
    
    if len(s) == k:
      return True
    
    c = Counter(s) 
    odd_counts = 0
    
    for val in c.values():
      if val % 2 == 1:
        odd_counts += 1
        
    return odd_counts <= k
  