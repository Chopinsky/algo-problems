'''
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

Constraints:

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 105
'''


from typing import List


class Solution:
  '''
  the idea is to try every possible trie matches, and continue
  '''
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    root = {}
    words.sort(key=len)
    
    def insert(w: str):
      curr = root
      
      for ch in w:
        if ch not in curr:
          curr[ch] = {}
        
        curr = curr[ch]
          
      curr['#'] = None
      
    def find(w: str) -> bool:
      if not w:
        return True
      
      curr = root
      for i, ch in enumerate(w):
        if ch not in curr:
          return False
        
        curr = curr[ch]
        
        # try find if substring can be divided into seen words
        if '#' in curr and find(w[i+1:]):
          return True
        
      return False
    
    ans = []
    for w in words:
      if not w:
        continue
        
      if find(w):
        # the word is not seen, but it can be divided into 
        # seen words, just append it to the answer, no need 
        # to add it to the trie
        ans.append(w)
      else:
        # the word is not seen before, add it
        insert(w)
      
    return ans
    
    
  def findAllConcatenatedWordsInADict0(self, words: List[str]) -> List[str]:
    words.sort(key=lambda x: (len(x), x))
    # print(words)
    
    word_dict = [[] for _ in range(26)]
    ans = []
    cache = {}
    
    def match(base: str) -> bool:
      if not base:
        return True

      if base in cache:
        return cache[base]
        
      idx = ord(base[0]) - ord('a')
      # print(base, idx, word_dict[idx])
      
      if not word_dict[idx]:
        cache[base] = False
        return False
      
      n = len(base)
      for w in word_dict[idx]:
        n0 = len(w)
        if n0 > n:
          cache[base] = False
          return False
        
        if base[:n0] == w and match(base[n0:]):
          cache[base] = True
          return True
        
      cache[base] = False
      return False
    
    for w in words:
      if not w:
        continue
        
      if match(w):
        ans.append(w)
      else:
        idx = ord(w[0]) - ord('a')
        word_dict[idx].append(w)

      cache[w] = True
        
    return ans
  