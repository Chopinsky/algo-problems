'''
1616. Split Two Strings to Make Palindrome

You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

Example 1:

Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
Example 2:

Input: a = "xbdef", b = "xecab"
Output: false
Example 3:

Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.

Constraints:

1 <= a.length, b.length <= 10^5
a.length == b.length
a and b consist of lowercase English letters
'''

class Solution:
  def checkPalindromeFormation(self, a: str, b: str) -> bool:
    def find(s: str):
      n = len(s)
      if len(s) % 2 == 0:
        i, j = n//2-1, n//2
      else:
        i, j = n//2, n//2
      
      while i >= 0 and j < n and s[i] == s[j]:
        i -= 1
        j += 1
        
      # print('find:', s, s[i+1:j])
      
      return i+1
    
    limit = min(find(a), find(b))
    
    def test(s0: str, s1: str) -> bool:
      if len(s0) != len(s1):
        return False
      
      i, j = 0, len(s0)-1
      
      while i < j and i <= limit:
        if s0[i] != s1[j]:
          break
          
        i += 1
        j -= 1
        
      if i >= j:
        return True
      
      # print('test:', s0, s1, s1[i:j+1])
      
      return i >= limit
      
    return test(a, b) or test(b, a)
        