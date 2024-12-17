'''
You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.

Constraints:

1 <= repeatLimit <= s.length <= 10^5
s consists of lowercase English letters.
'''

from collections import Counter


class Solution:
  def repeatLimitedString(self, s: str, limit: int) -> str:
    c = Counter(s)
    # print('init:', c)
    res = ''
    cand = sorted(c)
    
    def fill():
      nonlocal res
      
    while cand:
      ch = cand.pop()
      while c[ch] > 0:
        used = min(c[ch], limit)
        res += ch*used
        c[ch] -= used
        if c[ch] == 0:
          break
          
        while cand and c[cand[-1]] == 0:
          cand.pop()
        
        if not cand:
          break
          
        last = cand[-1]
        res += last
        c[last] -= 1
        if not c[last]:
          cand.pop()
    
    return res
        
  def repeatLimitedString(self, s: str, limit: int) -> str:
    c = Counter(s)
    chars = sorted(c)
    res = ''
    # print(c, chars)
    
    while chars:
      ch = chars.pop()
      if res and ch == res[-1]:
        break
      
      cnt = min(c[ch], limit)
      c[ch] -= cnt
      res += ch * cnt
      
      if c[ch] > 0:
        while chars and c[chars[-1]] == 0:
          chars.pop()
        
        if chars:
          nxt_ch = chars.pop()
          res += nxt_ch
          c[nxt_ch] -= 1
          
          if c[nxt_ch] > 0:
            chars.append(nxt_ch)
          
        chars.append(ch)
      
    return res
  