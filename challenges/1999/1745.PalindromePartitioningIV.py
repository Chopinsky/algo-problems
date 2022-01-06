'''
Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.
 

Constraints:

3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.
'''


from bisect import bisect_right


class Solution:
  def checkPartitioning0(self, s: str):
    n = len(s)
    dp = [[True if i >= j else False for j in range(n)] for i in range(n)]

    # build up the dp[i][j] for if s[i:j] if a palindorme
    for l in range(2, n+1):
      i = 0
      j = i+l-1

      while j < n:
        dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        i += 1
        j += 1

    for i in range(1, n-1):
      for j in range(i, n-1):
        if dp[0][i-1] and dp[i][j] and dp[j+1][n-1]:
          return True

    return False


  def checkPartitioning(self, s: str) -> bool:
    n = len(s)
    prefix_pals = [0]
    suffix_pals = [n-1]
    pal_set = set()
    
    for i in range(n):
      l, r = i-1, i+1
      while l >= 0 and r < n and s[l] == s[r]:
        pal_set.add((l, r))
        if l == 0:
          prefix_pals.append(r)
          
        if r == n-1:
          suffix_pals.append(l)
          
        l -= 1
        r += 1
      
      l, r = i, i+1
      while l >= 0 and r < n and s[l] == s[r]:
        pal_set.add((l, r))
        if l == 0:
          prefix_pals.append(r)
          
        if r == n-1:
          suffix_pals.append(l)
          
        l -= 1
        r += 1

    suffix_pals.sort()
    # print(prefix_pals, suffix_pals, pal_set)
    
    for l in prefix_pals:
      idx = bisect_right(suffix_pals, l+1)
      if idx >= len(suffix_pals):
        continue
        
      for r in suffix_pals[idx:]:
        if l+1 == r-1 or (l+1, r-1) in pal_set:
          return True
    
    return False
