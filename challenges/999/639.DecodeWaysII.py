'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s containing digits and the '*' character, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: s = "*"
Output: 9
Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
Hence, there are a total of 9 ways to decode "*".

Example 2:

Input: s = "1*"
Output: 18
Explanation: The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
Hence, there are a total of 9 * 2 = 18 ways to decode "1*".

Example 3:

Input: s = "2*"
Output: 15
Explanation: The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29".
"21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".

Constraints:

1 <= s.length <= 10 ** 5
s[i] is a digit or '*'.
'''

class Solution:
  def numDecodings(self, s: str) -> int:
    ls = len(s)
    if ls == 0:
      return 0
    
    if s[0] == '0':
      return 0
    
    def check_one(ch: chr) -> int:
      if ch == '0':
        return 0
      
      return 9 if ch == '*' else 1
    
    def check_two(last: chr, ch: chr) -> int:
      if last == '0':
        return 0
      
      if ch == '*':
        if last == '*':
          return 15
        
        if last == '1':
          return 9
        
        if last == '2':
          return 6
        
        return 0
      
      if ch <= '6':
        if last == '*':
          return 2
        
        if last == '1' or last == '2':
          return 1
        
        return 0
      
      return 1 if last == '*' or last == '1' else 0
        
    mod = 10 ** 9 + 7
    d0, d1 = 1, check_one(s[0])
    
    for i in range(1, ls):
      curr = d0 * check_two(s[i-1], s[i]) + d1 * check_one(s[i])
      # if i == ls-1:
      #   print(i, d0, check_two(s[i-1], s[i]), d1, check_one(s[i]), curr)  
      
      d0, d1 = d1, curr % mod
      if d0 == 0 and d1 == 0:
        return 0
    
    return d1
  