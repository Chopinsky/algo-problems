'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''

from typing import List


class Solution:
  def partitionLabels(self, s: str) -> List[int]:
    ans = []
    pos = {}
    n = len(s)
    
    for i in range(n):
      if s[i] not in pos:
        pos[s[i]] = [i, i]
      else:
        pos[s[i]][1] = i
        
    arr = sorted(pos.values())
    curr = None
    # print(arr)
    
    for a, b in arr:
      if not curr:
        curr = [a, b]
        continue
        
      if a > curr[1]:
        ans.append(curr[1]-curr[0]+1)
        curr[0] = a
        curr[1] = b
        continue
        
      curr[1] = max(curr[1], b)
        
    ans.append(curr[1]-curr[0]+1)
    
    return ans  
    