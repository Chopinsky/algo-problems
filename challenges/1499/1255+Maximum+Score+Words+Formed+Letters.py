'''
1255. Maximum Score Words Formed by Letters

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.

Constraints:

1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
'''

from typing import List
from collections import Counter

class Solution:
  def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
    c = Counter(letters)
    w = [Counter(word) for word in words]
    n = len(w)
    # print(c, w)
    
    def calc_score(used: List):
      return sum(cnt*char_score for cnt, char_score in zip(used, score))
    
    def dp(i: int, used: List):
      if i >= n:
        return calc_score(used)
      
      # if not using the word
      s0 = dp(i+1, used)
      
      # if using the word
      chars = w[i]
      can_use = True
      with_word = used.copy()
      
      for ch, cnt in chars.items():
        ch_idx = ord(ch) - ord('a')
        if with_word[ch_idx] + cnt > c.get(ch, 0):
          can_use = False
          break
          
        with_word[ch_idx] += cnt
      
      s1 = dp(i+1, with_word) if can_use else 0
      
      return max(s0, s1)
    
    return dp(0, [0]*26)
        