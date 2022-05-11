'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045

Constraints:

1 <= n <= 50 
'''

from functools import lru_cache


class Solution:
  def countVowelStrings(self, n: int) -> int:
    @lru_cache(None)
    def dp(i, rem):
      if rem == 1:
        return 5 - i
      
      cnt = 0
      for j in range(i, 5):
        cnt += dp(j, rem-1)
        
      return cnt
    
    return dp(0, n)
    