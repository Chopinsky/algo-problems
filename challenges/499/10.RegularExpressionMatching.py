'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false

Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''


class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    i, j = 0, 0
    cache = {}
    
    def check(s: str, p: str) -> bool:
      if (s, p) in cache:
        return cache[(s, p)]
      
      ans = False
      lp, ls = len(p), len(s)
      
      if lp == 0 or ls == 0:
        # pattern or source is exhuasted
        if lp == 0 and ls == 0:
          ans = True
        elif lp >= 2 and p[1] == '*':
          ans = check(s, p[2:])
          
      else:
        if lp > 1:
          # lp >= 2
          if p[1] != '*':
            ans = (s[0] == p[0] or p[0] == '.') and check(s[1:], p[1:])
            
          else:
            for i in range(ls):
              if s[i] != p[0] and p[0] != '.':
                break
              
              done = check(s[i+1:], p[2:])
              if done:
                ans = True
                break
            
            if not ans:
              ans = check(s, p[2:])
              
        else:
          # lp == 1
          ans = (ls == 1 and (s[0] == p[0] or p[0] == '.'))
      
      cache[(s, p)] = ans
      return ans
    
    res = check(s, p)
    # print(cache)
    
    return res