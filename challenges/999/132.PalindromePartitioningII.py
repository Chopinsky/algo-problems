'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:

Input: s = "a"
Output: 0

Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
'''

class Solution:
  def minCut(self, s: str) -> int:
    ln = len(s)
    count = [i for i in range(ln-1, -1, -1)]
    count.append(-1)
    
    def is_pal(i: int, j: int) -> bool:
      nonlocal s
      
      if i == j:
        return True
      
      f = s[i:j+1]
      b = f[::-1]
      
      return f == b
    
    for i in range(ln-2, -1, -1):
      for j in range(i, ln):
        if is_pal(i, j):
          # print("seg:", i, j, count[j+1])
          count[i] = min(count[i], 1+count[j+1])
    
    # print(count)
    
    return count[0]
    