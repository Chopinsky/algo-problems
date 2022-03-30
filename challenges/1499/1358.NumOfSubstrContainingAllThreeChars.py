'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''


class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    # ca, cb, cc = [], [], []
    ca, cb, cc = -1, -1, -1
    count = 0
    
    for i, ch in enumerate(s):
      if ch == 'a':
        ca = i
        if cb < 0 or cc < 0:
          continue
          
        # print('a', i, j)
        count += min(cb, cc) + 1
        
      elif ch == 'b':
        cb = i
        if ca < 0 or cc < 0:
          continue
          
        # print('b', i, j)
        count += min(ca, cc) + 1
        
      else:
        cc = i
        if ca < 0 or cb < 0:
          continue
          
        # print('c', i, j)
        count += min(ca, cb) + 1
        
    # print(ca, cb, cc)
    return count 
      