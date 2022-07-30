'''
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

Constraints:

1 <= words1.length, words2.length <= 10^4
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
'''

from typing import List
from collections import defaultdict, Counter


class Solution:
  def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    full_set = defaultdict(int)
    
    for w in words2:
      c = Counter(w)
      for ch, cnt in c.items():
        full_set[ch] = max(full_set[ch], cnt)
      
    ans = []
    for w in words1:
      c = Counter(w)
      found = True
      
      for ch in full_set:
        if ch not in c or c[ch] < full_set[ch]:
          found = False
          break
          
      if found:
        ans.append(w)
      
    return ans