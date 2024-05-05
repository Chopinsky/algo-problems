'''
3121. Count the Number of Special Characters II

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.

Constraints:

1 <= word.length <= 2 * 10^5
word consists of only lowercase and uppercase English letters.
'''

class Solution:
  def numberOfSpecialChars(self, word: str) -> int:
    pos = {}
    cnt = 0
    
    for i in range(len(word)):
      ch = word[i]
      if 'a' <= ch <= 'z':
        pos[ch] = i
        
      if 'A' <= ch <= 'Z' and ch not in pos:
        pos[ch] = i
        
    # print(pos)
    for ch in pos:
      if 'A' <= ch <= 'Z':
        continue
        
      capital_character = chr(ord('A') + ord(ch) - ord('a'))
      # print(ch, capital_character)
      
      if capital_character in pos and pos[ch] < pos[capital_character]:
        cnt += 1
    
    return cnt
        