'''
1422. Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3

Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
'''

class Solution:
  def maxScore(self, s: str) -> int:
    n = len(s)
    l0, l1 = 0, 0
    r0 = s.count('0')
    r1 = n - r0
    score = 0

    for i in range(n-1):
      ch = s[i]
      if ch == '1':
        l1 += 1
        r1 -= 1
      else:
        l0 += 1
        r0 -= 1

      # print('iter:', ch, (l0, l1), (r0, r1))
      score = max(score, l0+r1)

    return score
        
  def maxScore(self, s: str) -> int:
    l0 = 0
    r1 = s.count('1')
    score = 0
    
    for ch in s[:-1]:
      if ch == '0':
        l0 += 1
      else:
        r1 -= 1
        
      score = max(score, l0+r1)
    
    return score
        