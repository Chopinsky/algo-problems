'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
'''

from typing import List
from collections import defaultdict


class Solution:
  def longestStrChain(self, words: List[str]) -> int:
    words.sort(key=len)
    # print(words)
    
    cand = defaultdict(list)
    long = 1
    
    def match(w0, w1) -> bool:
      inserted = False
      i, j = 0, 0
      l0, l1 = len(w0), len(w1)
      
      while i < l0 and j < l1:
        if w0[i] != w1[j]:
          if inserted:
            return False
          
          inserted = True
          i += 1
          
        else:
          i += 1
          j += 1
          
      # print(w0, w1, i, j)
      if not inserted and i == l1 and j == l1:
        return True
      
      return i == l0 and j == l1
    
    for w0 in words:
      l0 = len(w0)
      s0 = 1
            
      for w1, s1 in cand[l0-1]:
        if match(w0, w1):
          s0 = max(s0, s1+1)
          
      cand[l0].append((w0, s0))
      long = max(long, s0)
    
    # print(cand)
    return long  
  