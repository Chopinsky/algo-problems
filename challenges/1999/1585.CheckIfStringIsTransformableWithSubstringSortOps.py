'''
Given two strings s and t, transform string s into string t using the following operation any number of times:

Choose a non-empty substring in s and sort it in place so the characters are in ascending order.
For example, applying the operation on the underlined substring in "14234" results in "12344".
Return true if it is possible to transform s into t. Otherwise, return false.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following sort operations:
"84532" (from index 2 to 3) -> "84352"
"84352" (from index 0 to 2) -> "34852"
Example 2:

Input: s = "34521", t = "23415"
Output: true
Explanation: You can transform s into t using the following sort operations:
"34521" -> "23451"
"23451" -> "23415"
Example 3:

Input: s = "12345", t = "12435"
Output: false

Constraints:

s.length == t.length
1 <= s.length <= 10^5
s and t consist of only digits.
'''


from collections import Counter, defaultdict


class Solution:
  def isTransformable(self, s: str, t: str) -> bool:
    if Counter(s) != Counter(t):
      return False
    
    pos = defaultdict(list)
    for i in reversed(range(len(s))):
      pos[ord(s[i]) - ord('0')].append(i)
      
    # print(pos)
    
    for ch in t:
      num = ord(ch) - ord('0')
      if not pos[num]:
        return False
      
      base = pos[num][-1]
      for n0 in range(num):
        if len(pos[n0]) > 0 and pos[n0][-1] <= base:
          # print(num, base, n0)
          return False
      
      pos[num].pop()
      
    return True
    