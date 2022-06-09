'''
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
'''

from typing import List


class Solution:
  def maxProduct(self, words: List[str]) -> int:
    def word_score(s: str):
      chars = set(s)
      score = 0
      for ch in chars:
        score |= 1 << (ord(ch) - ord('a'))
      
      return score
    
    stack = []
    prod = 0
    
    for w in words:
      s0 = word_score(w)
      l0 = len(w)
      
      for s1, l1 in stack:
        if s0 & s1 > 0:
          continue
          
        prod = max(prod, l0 * l1)
        
      stack.append((s0, l0))
      
    return prod
  