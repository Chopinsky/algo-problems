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
    count = [0, 0, 0]
    r = 0
    n = len(s)
    total = 0

    for i in range(n):
      while r < n and any(val == 0 for val in count):
        idx = ord(s[r]) - ord('a')
        count[idx] += 1
        r += 1

      if all(val > 0 for val in count):
        total += n-r+1

      idx = ord(s[i]) - ord('a')
      count[idx] -= 1

    return total
        
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
      