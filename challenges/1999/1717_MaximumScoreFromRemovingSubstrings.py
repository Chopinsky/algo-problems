'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

Constraints:

1 <= s.length <= 10^5
1 <= x, y <= 10^4
s consists of lowercase English letters.
'''


class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
    curr, nxt = list(s), []
    has_changes = True
    s1 = ["ab", x]
    s2 = ["ba", y]
    
    # swap
    if x < y:
      s1, s2 = s2, s1

    scores = 0
    # print('init:', s1, s2)

    while has_changes:
      has_changes = False
      # print('iter:', curr)
      
      for ch in curr:
        if nxt and nxt[-1] == s1[0][0] and ch == s1[0][1]:
          scores += s1[1]
          nxt.pop()
          has_changes = True
        else:
          nxt.append(ch)

      curr, nxt = nxt, curr
      nxt.clear()

      for ch in curr:
        if nxt and nxt[-1] == s2[0][0] and ch == s2[0][1]:
          scores += s2[1]
          nxt.pop()
          has_changes = True
        else:
          nxt.append(ch)

      curr, nxt = nxt, curr
      nxt.clear()

    return scores
        
  def maximumGain(self, s: str, x: int, y: int) -> int:
    def get_score(lst, pat, s0):
      s1 = 0
      stack = []
      # print(lst, pat, s0)
      
      for ch in lst:
        if stack and stack[-1] == pat[0] and ch == pat[1]:
          stack.pop()
          s1 += s0
          continue
          
        stack.append(ch)
    
      return stack, s1
    
    if x >= y:
      l1, s1 = get_score(list(s), 'ab', x)
      _, s2 = get_score(l1, 'ba', y)
      
      return s1+s2
    
    l1, s1 = get_score(list(s), 'ba', y)
    _, s2 = get_score(l1, 'ab', x)
    
    return s1+s2
        
  def maximumGain(self, s: str, x: int, y: int) -> int:
    stack = []
    if x >= y:
      a = ('a', 'b')
      b = ('b', 'a')
    else:
      a = ('b', 'a')
      b = ('a', 'b')
      x, y = y, x
      
    score = 0
    for ch in s:
      if not stack:
        stack.append(ch)
        continue
        
      if ch == a[1] and stack[-1] == a[0]:
        stack.pop()
        score += x
        continue
        
      stack.append(ch)
        
    nxt = []
    for ch in stack:
      if not nxt:
        nxt.append(ch)
        continue
        
      if ch == b[1] and nxt[-1]  == b[0]:
        nxt.pop()
        score += y
        continue
        
      nxt.append(ch)
      
    return score
  