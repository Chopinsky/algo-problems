'''
2337. Move Pieces to Obtain a String

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.
Example 2:

Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
Example 3:

Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.

Constraints:

n == start.length == target.length
1 <= n <= 10^5
start and target consist of the characters 'L', 'R', and '_'.
'''

from typing import List


class Solution:
  def canChange(self, start: str, target: str) -> bool:
    if len(start) != len(target):
      return False
    
    def condense(s: str) -> List:
      stack = []
      for i in range(len(s)):
        ch = s[i]
        if ch == '_':
          continue
          
        stack.append((ch, i))
        
      return stack
    
    a0 = condense(start)
    a1 = condense(target)
    if len(a0) != len(a1):
      return False
    
    for (c0, i0), (c1, i1) in zip(a0, a1):
      # print('iter:', c0, i0, c1, i1)
      if c0 != c1:
        return False
      
      if c0 == 'L' and i0 < i1:
        return False
      
      if c0 == 'R' and i0 > i1:
        return False
    
    return True
    
  def canChange(self, start: str, target: str) -> bool:
    s, t = [], []
    for i in range(len(target)):
      if start[i] != '_':
        s.append((start[i], i))
        
      if target[i] != '_':
        t.append((target[i], i))
    
    if len(s) != len(t):
      return False
        
    last = -1
    for (c0, i), (c1, j) in zip(s, t):
      # print(c0, i, c1, j)
      if c0 != c1:
        return False
      
      if c0 == 'R' and i > j:
        return False
      
      if c0 == 'L' and i < j:
        return False
    
    return True
  