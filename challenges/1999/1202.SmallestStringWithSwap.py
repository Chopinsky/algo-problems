'''
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
'''


from typing import List


class Solution:
  def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    chars = list(s)
    idx = [i for i in range(len(chars))]
    
    def find(i: int) -> int:
      while i != idx[i]:
        i = idx[i]
        
      return i
    
    def union(i: int, j: int) -> int:
      ri, rj = find(i), find(j)
      if ri == rj:
        return ri
      
      if ri < rj:
        idx[rj] = ri
        return ri
      
      idx[ri] = rj
      return rj
    
    for a in pairs:
      union(a[0], a[1])
      
    groups = {}
    for i, n in enumerate(idx):
      root = find(n)
      
      if root in groups:
        groups[root][0].append(i)
        groups[root][1].append(s[i])
      else:
        groups[root] = [[i], [s[i]]]
        
    # print(idx, groups)
    
    for data in groups.values():
      if len(data) <= 1:
        continue
        
      i = sorted(data[0])
      c = sorted(data[1])
      
      for j, si in enumerate(i):
        chars[si] = c[j]
    
    return "".join(chars)
  
