'''
984. String Without AAA or BBB

Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.

Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"
 
Constraints:

0 <= a, b <= 100
It is guaranteed such an s exists for the given a and b.
'''

from functools import lru_cache


class Solution:
  def strWithout3a3b(self, a: int, b: int) -> str:
    @lru_cache(None)
    def build(a: int, b: int, curr: int):
      if a == 0:
        # print('end-a', a, b, curr)
        return '' if b > 2 or curr == 0 else 'b' * b
      
      if b == 0:
        # print('end-b', a, b, curr)
        return '' if a > 2 or curr == 1 else 'a' * a
      
      # max: 'aabaabaa' or 'abbabb'
      if curr == 0 and (a > 2*(b+1) or 2*a < b):
        return ''
      
      # max: 'bbabbabb' or 'baabaa'
      if curr == 1 and (b > 2*(a+1) or 2*b < a):
        return ''
      
      if curr == 0:
        s0 = build(a-1, b, 1-curr)
        if s0:
          return 'a' + s0
        
        if a > 1:
          s1 = build(a-2, b, 1-curr)
          # print('a-s1', s1)
          if s1:
            return 'aa' + s1
        
        return ''
      
      s0 = build(a, b-1, 1-curr)
      if s0:
        return 'b' + s0
      
      if b > 1:
        s1 = build(a, b-2, 1-curr)
        if s1:
          return 'bb' + s1
        
      return ''
      
    s0 = build(a, b, 0)
    # print('a:', s0)
    if s0:
      return s0
    
    s1 = build(a, b, 1)
    # print('b:', s1)
    return s1
  