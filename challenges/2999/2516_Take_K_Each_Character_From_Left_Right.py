'''
2516. Take K of Each Character From Left and Right

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

Constraints:

1 <= s.length <= 10^5
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
'''


class Solution:
  def takeCharacters(self, s: str, k: int) -> int:
    if k == 0:
      return 0
    
    c0 = s.count('a')
    c1 = s.count('b')
    c2 = s.count('c')
    
    if c0 < k or c1 < k or c2 < k:
      return -1
    
    n = len(s)
    suffix = []
    
    for i in range(n-1, -1, -1):
      ch = s[i]
      prev = suffix[-1] if i < n-1 else (0, 0, 0)
      curr = (
        prev[0]+(1 if s[i] == 'a' else 0),
        prev[1]+(1 if s[i] == 'b' else 0),
        prev[2]+(1 if s[i] == 'c' else 0),
      )
      
      suffix.append(curr)
      
    suffix = suffix[::-1]
    prev = [0, 0, 0]
    curr = [0, 0, 0]
    j = n-1

    def update(arr, i, d=1):
      ch = s[i]
      if ch == 'a':
        arr[0] += d
        
      if ch == 'b':
        arr[1] += d
        
      if ch == 'c':
        arr[2] += d
      
    def can_pop():
      if j >= n:
        return False
      
      ch = s[j]
      d0 = -1 if ch == 'a' else 0
      d1 = -1 if ch == 'b' else 0
      d2 = -1 if ch == 'c' else 0
      
      return (
        prev[0]+curr[0]+d0 >= k
        and prev[1]+curr[1]+d1 >= k
        and prev[2]+curr[2]+d2 >= k
      )
      
    while j >= 0:
      update(prev, j)
      if (prev[0] >= k and prev[1] >= k and prev[2] >= k):
        break
        
      j -= 1  
      
    remove = n-j
    for i in range(n):
      update(curr, i)
        
      while can_pop():
        update(prev, j, -1)
        j += 1
        
      remove = min(remove, i+1+n-j)
      
    return remove
      
  def takeCharacters(self, s: str, k: int) -> int:
    ch = [0, 0, 0]
    i, n = 0, len(s)
    
    while i < n and min(ch) < k:
      idx = ord(s[i]) - ord('a')
      ch[idx] += 1
      i += 1
      
    if min(ch) < k:
      return -1
    
    j = n-1
    time = i
    i -= 1
    # print(i, time, ch)
    
    while i >= 0:
      idx = ord(s[i]) - ord('a')
      ch[idx] -= 1
      i -= 1
      
      if ch[idx] < k:
        while j > i and s[j] != s[i+1]:
          jdx = ord(s[j]) - ord('a')
          ch[jdx] += 1
          j -= 1
          
        if j > i:
          ch[idx] += 1
          j -= 1
        
      # print(i, s[i+1], j, time, ch)
      time = min(time, (i+n-j))
      
    return time
    