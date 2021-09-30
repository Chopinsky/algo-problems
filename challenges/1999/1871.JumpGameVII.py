'''
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
'''


from bisect import bisect_right


class Solution:
  def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    if s[-1] != '0':
      return False
    
    n = len(s)
    if minJump == maxJump:
      i = 0
      while i < n:
        if s[i] != '0':
          return False
        
        i += minJump
        if i == n-1:
          return True
        
      return False
    
    src = []
    for i in range(len(s)):
      if s[i] == '0':
        src.append(i)
        
    # print(src)
    start = [minJump]
    end = [maxJump]
    
    for idx in src[1:]:
      j = bisect_right(start, idx)-1
      
      # an invalid jump
      if j >= len(start) or j < 0 or idx > end[j]:
        continue
        
      ns, ne = idx+minJump, idx+maxJump
      # print(idx, j, ns, ne, start, end)
      
      if ns > end[-1]+1:
        start.append(ns)
        end.append(ne)
      else:
        end[-1] = ne
        
      if start[-1] >= n:
        return False
      
      if end[-1] >= n-1:
        return True
    
    # print(start, end)
    return False
      