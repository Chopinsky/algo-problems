'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
'''


from collections import defaultdict, Counter
from typing import List


class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    group = defaultdict(list)
    
    def serialize(src) -> str:
      base = ""
      for ch in sorted(src):
        base += f'{ch},{src[ch]};'
        
      return base
    
    for s in strs:
      c = serialize(Counter(s))
      group[c].append(s)
      
    return [arr for arr in group.values()]

  def groupAnagrams0(self, strs: List[str]) -> List[List[str]]:
    d = defaultdict(list)
    
    for w in strs:
      c = Counter(w)
      chars = []
      
      for ch in c:
        chars.append(ch)

      chars.sort()
      key = ""

      for ch in chars:
        key += f"({ch},{c[ch]})"
        
      d[key].append(w)

    ans = []
    for v in d.values():
      ans.append(v)
    
    return ans