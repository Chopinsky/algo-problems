'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
'''


from typing import List


class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    si, ti = len(s) - 1, len(t) - 1
    count_s, count_t = 0, 0

    while si >= 0 or ti >= 0:
      # si stops at non-deleted character in S or -1
      while si >= 0:
        if s[si] == '#':
          count_s += 1
          si -= 1
        elif s[si] != '#' and count_s > 0:
          count_s -= 1
          si -= 1
        else:
          break

      # ti stops at non-deleted character in T or -1
      while ti >= 0:
        if t[ti] == '#':
          count_t += 1
          ti -= 1
        elif t[ti] != '#' and count_t > 0:
          count_t -= 1
          ti -= 1
        else:
          break


      if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
        # eg. S = "a#", T = "a" 
        return False
      
      if (ti >= 0 and si >= 0) and s[si] != t[ti]:
        return False

      si -= 1
      ti -= 1
      
    return True
      
      
  def backspaceCompare0(self, s: str, t: str) -> bool:
    def build(src: str) -> List[str]:
      stack = []
      
      for ch in src:
        if ch == '#':
          if stack:
            stack.pop()

          continue

        stack.append(ch)
        
      return stack
      
    s1, s2 = build(s), build(t)
    if len(s1) != len(s2):
      return False
    
    for i in range(len(s1)):
      if s1[i] != s2[i]:
        return False
      
    return True
  