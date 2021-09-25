'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

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
    chars = {}
    parts = []
    seq = []
    
    for i, c in enumerate(s):        
      if c not in chars:
        chars[c] = [i, i]
        seq.append(c)
      else:
        chars[c][1] = i
        
    seq.reverse()
    start, end = -1, -1
    # print(chars, seq)
    
    while seq:
      curr = seq.pop()
      if start < 0 or end < 0:
        start, end = chars[curr]
        continue
        
      s0, e0 = chars[curr]
      if s0 < end:
        end = max(e0, end)
      else:
        # print(curr, start, end)
        parts.append(end-start+1)
        start, end = s0, e0
      
    if start >= 0:
      parts.append(end-start+1)
      
    return parts  