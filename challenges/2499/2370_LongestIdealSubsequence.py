'''
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.

Constraints:

1 <= s.length <= 10^5
0 <= k <= 25
s consists of lowercase English letters.
'''

class Solution:
  def longestIdealString(self, s: str, k: int) -> int:
    ln = [0]*26
    seq = 0
    
    def update(val: int) -> int:
      long = 0
      ldx, rdx = val, val
      dist = 0
      
      while dist <= k and (ldx >= 0 or rdx < 26):
        if ldx >= 0:
          long = max(long, ln[ldx])
          
        if rdx < 26:
          long = max(long, ln[rdx])
          
        dist += 1
        ldx -= 1
        rdx += 1
        
      ln[val] = long+1
      
      return ln[val]
    
    for ch in s:
      seq = max(seq, update(ord(ch) - ord('a')))
    
    # print(ln)
    return seq
    
  def longestIdealString(self, s: str, k: int) -> int:
    ln = [0] * 26
    
    for ch in s:
      idx = ord(ch) - 97
      max_ln = 0
      #print(ch, idx)

      for j in range(max(0, idx-k), min(25, idx+k)+1):
        max_ln = max(max_ln, ln[j])
          
      ln[idx] = max(ln[idx], max_ln+1)
                      
    return max(ln)
    