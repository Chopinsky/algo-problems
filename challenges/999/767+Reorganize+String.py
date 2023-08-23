'''
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''

from collections import Counter


class Solution:
  def reorganizeString(self, s: str) -> str:
    c = Counter(s)
    n = len(s)
    ans = ""
    lst = sorted(s, key=lambda x: (c[x], x))
    a = lst[n//2:]
    b = lst[:n//2]
    # print(lst, a, b)
    
    while a or b:
      if a:
        ch = a.pop()
        if ans and ch == ans[-1]:
          return ""
        
        ans += ch
        
      if b:
        ch = b.pop()
        if ans and ch == ans[-1]:
          return ""
        
        ans += ch
    
    return ans
        
        
  def reorganizeString(self, s: str) -> str:
    c = Counter(s)
    total = sum(c.values())
    top = max(c.values())
    if top > (total-top) + 1:
      return ''
    
    cand = sorted(c, key=lambda x: -c[x])
    n, j = len(s), 0
    ans = [''] * n
    
    for i in [idx for idx in range(0, n, 2)] + [idx for idx in range(1, n, 2)]:
      ch = cand[j]
      ans[i] = ch
      c[ch] -= 1
      if c[ch] == 0:
        j += 1
    
    return ''.join(ans)
   