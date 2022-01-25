'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
'''


class Solution:
  def detectCapitalUse(self, word: str) -> bool:
    c, l = 0, 0
    for ch in word:
      if 'a' <= ch <= 'z':
        l += 1
      else:
        c += 1

    return c == len(word) or l == len(word) or (c == 1 and 'A' <= word[0] <= 'Z')
    