'''
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''

from typing import List
from collections import Counter

class Solution:
  def commonChars(self, words: List[str]) -> List[str]:
    count = Counter(words[0])
    
    for w in words[1:]:
      c0 = Counter(w)
      for ch in list(count):
        if ch not in c0:
          count.pop(ch, None)
          continue
          
        count[ch] = min(count[ch], c0[ch])
      
    ans = []
    for ch, cnt in count.items():
      ans += [ch]*cnt
      
    return ans
        