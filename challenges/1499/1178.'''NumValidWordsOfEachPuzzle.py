'''
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].

Example 1:

Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation: 
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.

Example 2:

Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
Output: [0,1,3,2,0]

Constraints:

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7

words[i] and puzzles[i] consist of lowercase English letters.
Each puzzles[i] does not contain repeated characters.
'''

from itertools import combinations
from collections import Counter, defaultdict
from typing import List


class Solution:
  '''
  the trick is that we can iterate over all the `mask` combinations with 
  `sub_mask = (sub_mask-1) & master_mask when (sub_mask > 0)`, then check
  how many words can fit into this subset of the chars in the puzzle.
  '''
  def bitmask(self, word: str) -> int:
    mask = 0
    for letter in word:
      mask |= 1 << (ord(letter) - ord('a'))

    return mask
  
  def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
    # Create a bitmask for each word.
    word_count = Counter(self.bitmask(word) for word in words)
    oa = ord('a')
    ans = []
    
    for p in puzzles:
      # the initial char must be present in the words
      init = 1 << (ord(p[0]) - oa)
      count = word_count[init]
      
      # iterate over all possible combinations of the
      # master_mask using `sub_mask = (sub_mask-1) & master_mask`
      master_mask = self.bitmask(p[1:])
      sub_mask = master_mask
      
      while sub_mask:
        count += word_count[sub_mask | init]
        sub_mask = (sub_mask - 1) & master_mask
        
      ans.append(count)
      
    return ans
  
    
  def findNumOfValidWords0(self, words: List[str], puzzles: List[str]) -> List[int]:
    ans = []
    oa = ord('a')
    word_src = [defaultdict(int) for _ in range(26)]
    acceptable = {}
    
    for p in puzzles:
      chars = list(set(p))
      init = 1 << (ord(p[0]) - oa)
      
      for l in range(1, 8):
        for sub in combinations(chars, l):
          mask = 0
          # print(p, l, sub)
          for ch in sub:
            mask |= 1 << (ord(ch) - oa)
            
          if mask not in acceptable:
            acceptable[mask] = 0
            
          acceptable[mask] |= init
      
    for w in words:
      chars = list(set(w))
      if len(chars) > 7:
        continue
        
      mask = 0
      for ch in chars:
        mask |= 1 << (ord(ch) - oa)
        
      # if the supset does not exist, or the init char is not in 
      # this word
      if (mask not in acceptable) or (acceptable[mask] & mask == 0):
        # print('skip 1:', w)
        continue
      
      for ch in chars:
        idx = ord(ch) - oa
        if (1<<idx) & acceptable[mask] == 0:
          # print('skip 2:', w, ch)
          continue
          
        word_src[idx][mask] += 1
    
    for p in puzzles:
      chars = list(set(p))
      mask = 0
      
      for ch in chars:
        mask |= 1 << (ord(ch) - oa)  
      
      count = 0
      src = word_src[ord(p[0]) - oa]
      
      for key in src:
        if mask == (mask | key):
          count += src[key]
      
      ans.append(count)
    
    return ans
  
  