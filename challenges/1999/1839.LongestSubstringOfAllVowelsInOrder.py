'''
A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

Example 1:

Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.

Example 2:

Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.

Example 3:

Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.
 
Constraints:

1 <= word.length <= 5 * 105
word consists of characters 'a', 'e', 'i', 'o', and 'u'.
'''

class Solution:
  def longestBeautifulSubstring(self, word: str) -> int:
    longest = 0
    if len(word) < 5:
      return longest
    
    count = 0
    dic = { 'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5 }
    start = -1
    
    for i, ch in enumerate(word):
      if start < 0:
        if ch == 'a':
          start = i
          count = 1
          
        continue
      
      if dic[ch] == count:
        continue
        
      if dic[ch] == count+1:
        count += 1
        continue
        
      if start >= 0 and count == 5:
        longest = max(longest, i-start)
        # print(i, start)
      
      start = i if ch == 'a' else -1
      count = 1 if ch == 'a' else 0
      
    if start >= 0 and count == 5:
      longest = max(longest, len(word)-start)
      
    return longest      
