'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?
'''

from functools import lru_cache


class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n3 != n1+n2:
      return False
    
    @lru_cache(None)
    def dp(i: int, j: int, k: int) -> bool:
      if k >= n3:
        return i >= n1 and j >= n2
      
      if i >= n1 and j >= n2:
        return k >= n3
      
      if i >= n1:
        return s2[j:] == s3[k:]
      
      if j >= n2:
        return s1[i:] == s3[k:]
      
      if s1[i] == s3[k] and dp(i+1, j, k+1):
        return True
      
      if s2[j] == s3[k] and dp(i, j+1, k+1):
        return True
      
      return False
    
    return dp(0, 0, 0)
        
        
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    m, n, l = len(s1), len(s2), len(s3)
    
    @lru_cache(None)
    def test(i: int, j: int, k: int) -> bool:
      # print(i, j, k)
      if k >= l:
        return i == m and j == n
      
      if i >= m:
        return s2[j:] == s3[k:]
        
      if j >= n:
        return s1[i:] == s3[k:]
      
      if s1 + s2 == s3 or s2 + s1 == s3:
        return True
      
      if s1[i] == s3[k] and test(i+1, j, k+1):
        return True
      
      if s2[j] == s3[k] and test(i, j+1, k+1):
        return True
      
      return False
      
    return test(0, 0, 0)


  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    n0, n1, n2 = len(s1), len(s2), len(s3)

    # length not matching, false
    if n0+n1 != n2:
      return False

    # empty strings, done
    if n2 == 0:
      return True

    if n0 == 0:
      return s2 == s3

    if n1 == 0:
      return s1 == s3

    # not going to match with the initial character
    if s1[0] != s3[0] and s2[0] != s3[0]:
      return False

    # matching with each chars
    dp = [[False] * (n1+1) for _ in range(n0+1)]
    stack = []
    seen = set()

    # init conditions
    if s1[0] == s3[0]:
      dp[1][0] = True
      stack.append((1, 0))
      seen.add((1, 0))

    if s2[0] == s3[0]:
      dp[0][1] = True
      stack.append((0, 1))
      seen.add((0, 1))

    while len(stack) > 0:
      (i, j), stack = stack[0], stack[1:]

      if i+1 <= n0 and s1[i] == s3[i+j] and (i+1, j) not in seen:
        dp[i+1][j] = True
        stack.append((i+1, j))
        seen.add((i+1, j))

      if j+1 <= n1 and s2[j] == s3[i+j] and (i, j+1) not in seen:
        dp[i][j+1] = True
        stack.append((i, j+1))
        seen.add((i, j+1))

    # print(dp)

    return dp[n0][n1]
