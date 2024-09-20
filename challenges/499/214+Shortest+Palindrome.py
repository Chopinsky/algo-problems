'''
214. Shortest Palindrome

Test cases:
"aacecaaa"
"abcd"
"abbacd"
'''

class Solution:
  '''
  use KMP to calculate the longest suffix that's also the prefix, where
  the suffix is the appended reversed string with a separator to break
  any pattern across the boundary
  '''
  def shortestPalindrome(self, s: str) -> str:
    # build the KMP prefix table
    def make_prefix(s: str) -> list:
      prefix = [0] * len(s)
      ln = 0

      for i in range(1, len(s)):
        while ln > 0 and s[i] != s[ln]:
          ln = prefix[ln - 1]
        
        if s[i] == s[ln]:
          ln += 1
          
        prefix[i] = ln
        
      return prefix
      
    # Reverse the original string
    rs = s[::-1]

    # Combine the original and reversed strings with a separator
    combined = s + "#" + rs

    # Build the prefix table for the combined string
    prefix = make_prefix(combined)
    # print(combined, prefix)

    # Construct the shortest palindrome by appending the reverse of the suffix
    suffix = rs[:-prefix[-1]]
    
    return suffix + s
  