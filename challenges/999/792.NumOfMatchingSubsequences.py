'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
'''

from bisect import bisect_left
from collections import defaultdict
from typing import List

class Solution:
  def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    count = 0
    n = len(s)
    chars = defaultdict(list)
    
    for i, ch in enumerate(s):
      chars[ch].append(i)
      
    # print(chars)
    
    def is_match(w: str) -> bool:
      curr = -1
      for ch in w:
        if ch not in chars:
          return False
        
        src = chars[ch]
        pos = bisect_left(src, curr+1)
        
        if pos >= len(src):
          return False
        
        # print(w, ch, curr, pos)
        curr = src[pos]
      
      return True
    
    for w in words:
      if len(w) > n:
        continue
        
      if is_match(w):
        # print("match:", w)
        count += 1
            
    return count
  