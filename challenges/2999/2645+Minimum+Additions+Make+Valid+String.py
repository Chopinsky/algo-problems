'''
2645. Minimum Additions to Make Valid String

Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.

A string is called valid if it can be formed by concatenating the string "abc" several times.

Example 1:

Input: word = "b"
Output: 2
Explanation: Insert the letter "a" right before "b", and the letter "c" right next to "a" to obtain the valid string "abc".
Example 2:

Input: word = "aaa"
Output: 6
Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid string "abcabcabc".
Example 3:

Input: word = "abc"
Output: 0
Explanation: word is already valid. No modifications are needed. 

Constraints:

1 <= word.length <= 50
word consists of letters "a", "b" and "c" only. 
'''

from functools import lru_cache


class Solution:
  def addMinimum(self, word: str) -> int:
    if not word:
      return 3
    
    insert = 0
    n = len(word)
    last = -1
    
    for i in range(n):
      key = ord(word[i]) - ord('a')
      
      if i == 0 or last == 2:
        insert += key
      elif key <= last:
        insert += key + (2-last)
      else:
        insert += key - last - 1
      
      if i == n-1:
        insert += 2-key
        
      last = key
    
    return insert
  

  def addMinimum0(self, word: str) -> int:
    n = len(word)

    @lru_cache(None)
    def dp(i: int, s: int):
      if i >= n:
        return 2-s
      
      key = ord(word[i]) - ord('a')
      insert = 0

      if s < 0 or s == 2:
        # if first char or last char is 'c', insert
        # missing chars before
        insert += key
      elif key <= s:
        # if a char before the last char, insert all
        # missing chars
        insert += key + (2-s)
      else:
        insert += key-s-1

      # print(word[i], key, insert)
      return insert+dp(i+1, key)
    
    return dp(0, -1)
    
    