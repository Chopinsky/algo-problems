'''
648. Replace Words

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
'''

from typing import List


class Solution:
  def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    if not sentence:
      return ''
    
    root = {}
    
    def insert(w):
      curr = root
      for ch in w:
        if ch not in curr:
          curr[ch] = {}
          
        curr = curr[ch]
          
      curr['$'] = None
      
    def find(w):
      curr = root
      prefix = ''
      
      for ch in w:
        if '$' in curr:
          return prefix
        
        if ch not in curr:
          return ''
        
        curr = curr[ch]
        prefix += ch
        
      if curr and '$' in curr:
        return prefix
      
      return ''
    
    for w in dictionary:
      insert(w)
      
    words = sentence.split(' ')
    res = []
    
    for w in words:
      prefix = find(w)
      # print(w, prefix)
      
      if not prefix:
        res.append(w)
      else:
        res.append(prefix)
    
    return ' '.join(res)
    