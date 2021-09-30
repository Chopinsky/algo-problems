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
    n = len(words)
    masks = [0] * n
    oa = ord('a')
    ans = 0

    for i, w in enumerate(words):
      m = 0
      for ch in w:
        m |= 1 << (ord(ch) - oa)

      masks[i] = m

      for j in range(i):
        if m & masks[j] == 0:
          product = len(w)*len(words[j])
          ans = max(ans, product)

    return ans
