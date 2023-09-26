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
  def removeDuplicateLetters(self, s: str) -> str:
    stack = []
    last = {}
    n = len(s)
    
    for i, ch in enumerate(s):
      last[ch] = i
      
    # print(last)
    seen = set()
    
    for i, c0 in enumerate(s):
      if c0 in seen:
        continue
        
      while stack and stack[-1] > c0 and last[stack[-1]] > i:
        c1 = stack.pop()
        seen.discard(c1)
      
      stack.append(c0)
      seen.add(c0)
      # print('iter:', i, c0, stack)
    
    return ''.join(stack)
        
        
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
  