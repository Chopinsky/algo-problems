'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''


class Solution:
  '''
  the idea is to pop the tail char that is larger than the current char, and the
  tail char can be added back in later part of the string
  '''
  def removeDuplicateLetters(self, s: str) -> str:
    last = {ch: i for i, ch in enumerate(s)}
    stack = []
    seen = set()
    
    for i, ch in enumerate(s):
      # this char is in better position, skip
      if ch in seen:
        continue
      
      # pop any char that can be added back later
      while stack and ch < stack[-1] and i < last[stack[-1]]:
        seen.discard(stack.pop())
        
      # add this char to the tail of the string
      stack.append(ch)
      seen.add(ch)
      
    return ''.join(stack)
  