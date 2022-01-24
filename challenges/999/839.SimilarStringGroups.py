'''
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
'''


from typing import List


class Solution:
  def numSimilarGroups(self, strs: List[str]) -> int:
    n = len(strs)
    m = len(strs[0])
    group = [i for i in range(n)]
    
    def find(x: int) -> int:
      while x != group[x]:
        x = group[x]
    
      return x
    
    def union(x: int, y: int):
      rx, ry = find(x), find(y)
      if rx <= ry:
        group[ry] = rx
      else:
        group[rx] = ry
        
    def is_similar(a: str, b: str) -> bool:
      diff_pos = []
      for i in range(m):
        if a[i] != b[i]:
          diff_pos.append(i)
        
        if len(diff_pos) > 2:
          return False
        
      return (len(diff_pos) == 0) or (len(diff_pos) == 2)
    
    for i in range(n-1):
      for j in range(i+1, n):
        # print(strs[i], strs[j], is_similar(strs[i], strs[j]))
        if is_similar(strs[i], strs[j]):
          union(i, j)
        
    groups = set()
    for i in range(n):
      root = find(i)
      groups.add(root)
    
    return len(groups)
  