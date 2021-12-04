'''
An original string, consisting of lowercase English letters, can be encoded by the following steps:

Arbitrarily split it into a sequence of some number of non-empty substrings.
Arbitrarily choose some elements (possibly none) of the sequence, and replace each with its length (as a numeric string).
Concatenate the sequence as the encoded string.
For example, one way to encode an original string "abcdefghijklmnop" might be:

Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
Choose the second and third elements to be replaced by their lengths, respectively. The sequence becomes ["ab", "12", "1", "p"].
Concatenate the elements of the sequence to get the encoded string: "ab121p".
Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive), return true if there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.

Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.

Example 1:

Input: s1 = "internationalization", s2 = "i18n"
Output: true
Explanation: It is possible that "internationalization" was the original string.
- "internationalization" 
  -> Split:       ["internationalization"]
  -> Do not replace any element
  -> Concatenate:  "internationalization", which is s1.
- "internationalization"
  -> Split:       ["i", "nternationalizatio", "n"]
  -> Replace:     ["i", "18",                 "n"]
  -> Concatenate:  "i18n", which is s2

Example 2:

Input: s1 = "l123e", s2 = "44"
Output: true
Explanation: It is possible that "leetcode" was the original string.
- "leetcode" 
  -> Split:      ["l", "e", "et", "cod", "e"]
  -> Replace:    ["l", "1", "2",  "3",   "e"]
  -> Concatenate: "l123e", which is s1.
- "leetcode" 
  -> Split:      ["leet", "code"]
  -> Replace:    ["4",    "4"]
  -> Concatenate: "44", which is s2.

Example 3:

Input: s1 = "a5b", s2 = "c5b"
Output: false
Explanation: It is impossible.
- The original string encoded as s1 must start with the letter 'a'.
- The original string encoded as s2 must start with the letter 'c'.

Example 4:

Input: s1 = "112s", s2 = "g841"
Output: true
Explanation: It is possible that "gaaaaaaaaaaaas" was the original string
- "gaaaaaaaaaaaas"
  -> Split:      ["g", "aaaaaaaaaaaa", "s"]
  -> Replace:    ["1", "12",           "s"]
  -> Concatenate: "112s", which is s1.
- "gaaaaaaaaaaaas"
  -> Split:      ["g", "aaaaaaaa", "aaaa", "s"]
  -> Replace:    ["g", "8",        "4",    "1"]
  -> Concatenate: "g841", which is s2.
  
Example 5:

Input: s1 = "ab", s2 = "a2"
Output: false
Explanation: It is impossible.
- The original string encoded as s1 has two letters.
- The original string encoded as s2 has three letters.
 

Constraints:

1 <= s1.length, s2.length <= 40
s1 and s2 consist of digits 1-9 (inclusive), and lowercase English letters only.
The number of consecutive digits in s1 and s2 does not exceed 3.
'''


from typing import List
from functools import lru_cache


class Solution:
  def possiblyEquals(self, s1: str, s2: str) -> bool:
    def build(s: str) -> List[str]:
      seq = []
      num = ''
      
      for ch in s:
        if ch.isalpha():
          if num:
            seq.append(num)
            num = ''
            
          seq.append(ch)
          continue
          
        num += ch
        
      if num:
        seq.append(num)
      
      return seq
    
    @lru_cache(None)
    def from_num(s: str) -> List[int]:
      # print('convert:', s)
      if len(s) == 1:
        return [int(s)]
      
      if len(s) == 2:
        return [int(s), int(s[0])+int(s[1])]
      
      return [int(s), int(s[:2])+int(s[2]), int(s[0])+int(s[1:]), int(s[0])+int(s[1])+int(s[2])]
      
    seq1, seq2 = build(s1), build(s2)
    # print(seq1, seq2)
    
    @lru_cache(None)
    def compare(i: int, j: int, balance: int) -> bool:
      # end of the game
      if i < 0 and j < 0:
        return (balance == 0)
      
      # edge case 1: run out of s1
      if i < 0 and balance <= 0:
        return False

      # edge case 2: run out of s2
      if j < 0 and balance >= 0:
        return False

      # more chars from s2, match with prev balance first
      if balance < 0:
        if seq1[i].isalpha():
          return compare(i-1, j, balance+1)

        for c1 in from_num(seq1[i]):
          if compare(i-1, j, balance+c1):
            # print('e7', i, j, balance, c1)
            return True
          
        return False
      
      # more chars from s1, match with prev balance first
      if balance > 0:
        if seq2[j].isalpha():
          return compare(i, j-1, balance-1)

        for c2 in from_num(seq2[j]):
          if compare(i, j-1, balance-c2):
            # print('e8', i, j, balance, c2)
            return True
          
        return False
      
      # all remaining cases assuming balance is 0
      # both are chars, check if they are equal
      if seq1[i].isalpha() and seq2[j].isalpha():
        return compare(i-1, j-1, 0) if seq1[i] == seq2[j] else False
      
      # both are digits, try all pairs 
      if seq1[i].isnumeric() and seq2[j].isnumeric():
        for c1 in from_num(seq1[i]):
          for c2 in from_num(seq2[j]):
            if compare(i-1, j-1, balance+c1-c2):
              # print('e4', i, j, balance, c1, c2)
              return True
            
        return False
      
      # s1 is a char, s2 is a num
      if seq1[i].isalpha() and seq2[j].isnumeric():
        for c2 in from_num(seq2[j]):
          if compare(i-1, j-1, balance+1-c2):
            # print('e5', i, j, balance, c2)
            return True
          
        return False
      
      # s1 is a num, s2 is a char
      for c1 in from_num(seq1[i]):
        if compare(i-1, j-1, balance-1+c1):
          # print('e6', i, j, balance, c1)
          return True
        
      return False

    return compare(len(seq1)-1, len(seq2)-1, 0)
    