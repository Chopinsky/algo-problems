'''
140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
'''

from typing import List
from functools import lru_cache

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    root = [None]*26 + [False]
    n = len(s)
    
    def add(word: str):
      curr = root
      
      for ch in word:
        idx = ord(ch) - ord('a')
        if curr[idx] is None:
          curr[idx] = [None]*26 + [False]
          
        curr = curr[idx]
          
      curr[26] = True
      
    @lru_cache(None)
    def search(i: int):
      if i >= n:
        return tuple([''])
      
      result = []
      curr = root
      
      for j in range(i, n):
        ch_idx = ord(s[j]) - ord('a')
        if not curr[ch_idx]:
          break
          
        curr = curr[ch_idx]
        if curr[26] == True:
          prefix = s[i:j+1]
          for suffix in search(j+1):
            spacing = ' ' if suffix else ''
            result.append(prefix + spacing + suffix)
      
      return tuple(result)
    
    for word in wordDict:
      add(word)
      
    # print(root)
    
    return search(0)
    