'''
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

Constraints:

1 <= s.length <= 10^5
s[i] is 'a' or 'b'​​.
'''

class Solution:
  def minimumDeletions(self, s: str) -> int:
    n = len(s)
    a_count = [0]*n
    b_count = [0]*n
    
    for i in range(n):
      before = (b_count[i-1] if i > 0 else 0)
      b_count[i] = before + (1 if s[i] == 'b' else 0)
        
    for i in range(n-1, -1, -1):
      after = (a_count[i+1] if i < n-1 else 0)
      a_count[i] = after + (1 if s[i] == 'a' else 0)
        
    # print(a_count, b_count)
    removal = n
    
    for i in range(n):
      b_before = b_count[i-1] if i > 0 else 0
      a_after = a_count[i+1] if i < n-1 else 0
      removal = min(removal, b_before+a_after)
      # print(i, b_before, a_after)
      
    return removal
        
  def minimumDeletions(self, s: str) -> int:
    n = len(s)
    a, b = [0]*n, [0]*n
    
    for i in range(n):
      if s[i] == 'b':
        b[i] = 1 if i == 0 else b[i-1] + 1
      else:
        b[i] = 0 if i == 0 else b[i-1]
        
    for i in range(n-1, -1, -1):
      if s[i] == 'a':
        a[i] = 1 if i == n-1 else a[i+1] + 1
      else:
        a[i] = 0 if i == n-1 else a[i+1]
            
    # print(a, b)
    count = n
    
    for i in range(n):
      before = 0 if i == 0 else b[i-1]
      after = 0 if i == n-1 else a[i+1]
      # print(i, before, after)
      count = min(count, before + after)
        
    return count
      