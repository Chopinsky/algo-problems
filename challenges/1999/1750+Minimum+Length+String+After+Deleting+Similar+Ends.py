'''
1750. Minimum Length of String After Deleting Similar Ends

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

Constraints:

1 <= s.length <= 10^5
s only consists of characters 'a', 'b', and 'c'.

Test Cases:
"ca"
"cabaabac"
"aabccabba"
"bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
'''


class Solution:
  def minimumLength(self, s: str) -> int:
    i, j = 0, len(s)-1
    last = len(s)
    
    while i <= j and s[i] == s[j]:
      ch = s[i]
      cnt = 0
      
      while i <= j and s[i] == ch:
        cnt += 1
        i += 1
        
      while i <= j and s[j] == ch:
        cnt += 1
        j -= 1
        
      if i > j:
        last = 0 if cnt > 1 else 1
        break
      
      last = j-i+1
    
    return last
        
  def minimumLength(self, s: str) -> int:
    l, r = 0, len(s)-1
    
    while l < r and s[l] == s[r]:
      ch = s[l]
      while l < r and s[l] == ch:
        l += 1
        
      while l <= r and s[r] == ch:
        r -= 1
      
      # print(s[l:r+1])
      
    return r-l+1
    