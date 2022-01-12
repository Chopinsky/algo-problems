'''
Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
Example 3:

Input: s = "LEETCODE"
Output: 92
 

Constraints:

1 <= s.length <= 10^5
s consists of uppercase English letters only.
'''


class Solution:
  '''
  the idea is that instead of count uniq chars in each substring, we count how
  many substrings the char appears uniq in, then add all the occurance # of this
  char
  '''
  def uniqueLetterString(self, s: str) -> int:
    # save the last 2 index where `c` appears in s
    char_pos = {c:[-1, -1] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    count = 0

    for i, ch in enumerate(s):
      k, j = char_pos[ch]
      
      # count # of all substrings with [l, r], where `l` is 
      # in [k+1, j], and `r` is in [j, i-1]
      count += (i - j) * (j - k)
      
      # update the char positions
      char_pos[ch] = [j, i]
    
    # count the "tail" substrings, where only the char appears
    # the last time in any of the substrings
    for c in char_pos:
      k, j = char_pos[c]
      
      # count # of all substrings with [l, r], where, `l` is
      # in [k+1, j], and `r` is in [j, len(s)-1]
      count += (len(s) - j) * (j - k)

    return count
      
    
  def uniqueLetterString0(self, s: str) -> int:
    if not s:
      return 0
    
    last_char_pos = [0] * 26
    char_contri = [0] * 26
    count = 0 # total unique char counts
    curr = 0  # current substrings uniq char counts
    
    for i, ch in enumerate(s):
      idx = ord(ch) - ord('A')
      
      # update the curr uniq char counts and the char 
      # contributions for all substrings
      curr -= char_contri[idx]
      char_contri[idx] = i - last_char_pos[idx] + 1
      
      # update the last position this char appears
      curr += char_contri[idx]
      last_char_pos[idx] = i+1
      
      # add all the extra uniq chars from the substrings
      count += curr
      
    return count
        