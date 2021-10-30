'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
a move consists of either replacing one occurrence of "XL" with "LX", or 
replacing one occurrence of "RX" with "XR". Given the starting string 
start and the ending string end, return True if and only if there exists 
a sequence of moves to transform one string to the other.

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:

Input: start = "X", end = "L"
Output: false

Example 3:

Input: start = "LLR", end = "RRL"
Output: false

Example 4:

Input: start = "XL", end = "LX"
Output: true

Example 5:

Input: start = "XLLR", end = "LXLX"
Output: false

Constraints:

1 <= start.length <= 10^4
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
'''


from collections import Counter


class Solution:
  def canTransform(self, start: str, end: str) -> bool:
    cs = Counter(start)
    ce = Counter(end)
    
    for ch in ['X', 'L', 'R']:
      # not presenting in the strings
      if ch not in cs and ch not in ce:
        continue
        
      # missing char
      if ch not in cs or ch not in ce:
        return False
      
      # unmatched char count
      if cs[ch] != ce[ch]:
        return False
    
    diff = 0
    
    for i in range(len(start)):
      s, e = start[i], end[i]
      # print(i)
      
      if s == e:
        # can't cross over
        if (s == 'L' and diff > 0) or (s == 'R' and diff < 0):
          return False
        
        continue
      
      if (s == 'L' and e == 'R') or (s == 'R' and e == 'L'):
        return False
      
      if s == 'R' and e == 'X':
        if diff < 0:
          return False
        
        diff += 1
        continue
        
      if s == 'X' and e == 'L':
        if diff > 0:
          return False
        
        diff -= 1
        continue
        
      if s == 'L' and e == 'X':
        if diff >= 0:
          return False
        
        diff += 1
        continue
        
      if s == 'X' and e == 'R':
        if diff <= 0:
          return False
        
        diff -= 1
        continue
    
    # print('end', diff)
    return diff == 0
  