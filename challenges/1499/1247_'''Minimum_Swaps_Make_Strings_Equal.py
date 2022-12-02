'''
1247. Minimum Swaps to Make Strings Equal

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
Example 2:

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1

Constraints:

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
'''

class Solution:
  def minimumSwap(self, s1: str, s2: str) -> int:
    n = len(s1)
    x1, y1, x2, y2 = 0, 0, 0, 0
    
    for i in range(n):
      if s1[i] == s2[i]:
        continue
        
      if s1[i] == 'x':
        x1 += 1
      else:
        y1 += 1
        
      if s2[i] == 'x':
        x2 += 1
      else:
        y2 += 1
          
    # print('before', (x1, y1), (x2, y2))
    total = 0
    
    # take care of all the xx/yy pairs:
    cnt = min(x1//2, y2//2)
    x1 -= 2*cnt
    y2 -= 2*cnt
    total += cnt
    
    # the yy/xx pairs:
    cnt = min(y1//2, x2//2)
    y1 -= 2*cnt
    x2 -= 2*cnt
    total += cnt
    
    # there should be at most one xy/yx pair left

    # print('after', (x1, y1), (x2, y2))
    if x1 == y1 == 0:
      return total
    
    if x1 == y1 == 1:
      return total + 2
    
    return -1
    