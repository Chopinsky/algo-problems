'''
1544. Make The String Great

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.
'''

class Solution:
  def makeGood(self, s: str) -> str:
    stack = []
    
    for c0 in s:
      if not stack:
        stack.append(c0)
        continue
        
      if 'a' <= c0 <= 'z':
        c1 = chr(ord(c0) - ord('a') + ord('A'))
      else:
        c1 = chr(ord(c0) - ord('A') + ord('a'))
        
      # print(c0, c1)
      if c1 == stack[-1]:
        stack.pop()
        continue
        
      stack.append(c0)
        
    return ''.join(stack)
        
  def makeGood(self, s: str) -> str:
    if len(s) < 2:
      return s
    
    stack = []
    diff = abs(ord('A') - ord('a'))
    
    for ch in s:
      if stack and abs(ord(ch) - ord(stack[-1])) == diff:
        stack.pop()
      
      else:
        stack.append(ch)
    
    return ''.join(stack)
      