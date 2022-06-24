'''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
'''


class Solution:
  def longestDiverseString(self, a: int, b: int, c: int) -> str:
    letters = [[a, 'a'], [b, 'b'], [c, 'c']]
    letters.sort()
    s = ''
    
    while len(s) < a+b+c:
      n0, c0 = letters[2]
      n1, c1 = letters[1]
      
      if s and c0 == s[-1]:
        break
      
      factor = 2 if (n0 > n1 + letters[0][0] and n0 >= 2) else 1
      s += factor*c0 + (c1 if n1 > 0 else '')
      n0 -= factor
      n1 -= 1 if n1 > 0 else 0
        
      letters[2][0] = n0
      letters[1][0] = n1
      letters.sort()
    
    return s
    