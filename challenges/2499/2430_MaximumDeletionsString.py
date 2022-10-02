'''
2430. Maximum Deletions on a String

You are given a string s consisting of only lowercase English letters. In one operation, you can:

Delete the entire string s, or
Delete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.
For example, if s = "ababc", then in one operation, you could delete the first two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".

Return the maximum number of operations needed to delete all of s.

Example 1:

Input: s = "abcabcdabc"
Output: 2
Explanation:
- Delete the first 3 letters ("abc") since the next 3 letters are equal. Now, s = "abcdabc".
- Delete all the letters.
We used 2 operations so return 2. It can be proven that 2 is the maximum number of operations needed.
Note that in the second operation we cannot delete "abc" again because the next occurrence of "abc" does not happen in the next 3 letters.
Example 2:

Input: s = "aaabaab"
Output: 4
Explanation:
- Delete the first letter ("a") since the next letter is equal. Now, s = "aabaab".
- Delete the first 3 letters ("aab") since the next 3 letters are equal. Now, s = "aab".
- Delete the first letter ("a") since the next letter is equal. Now, s = "ab".
- Delete all the letters.
We used 4 operations so return 4. It can be proven that 4 is the maximum number of operations needed.
Example 3:

Input: s = "aaaaa"
Output: 5
Explanation: In each operation, we can delete the first letter of s.

Constraints:

1 <= s.length <= 4000
s consists only of lowercase English letters.
'''

from functools import lru_cache


class Solution:
  def deleteString(self, s: str) -> int:
    n = len(s)
    if len(set(s)) == 1:
      return n

    # longest common substring length starting from i and j; init
    # condition: lcs[i+1][*] or lcs[*][j+1] is 0, since it's out
    # of the `s` bounds
    lcs = [[0]*(n+1 for _ in range(n+1))]

    # maximum deletion operations starting from index-i
    dp = [1] * n

    for i in range(n-1, -1, -1):
      for j in range(i+1, n):
        # expanding the lcs from the previous `i+1` and `j+1` index
        if s[i] == s[j]:
          lcs[i][j] = lcs[i+1][j+1] + 1

        # if common string covers s[i:j], then we can remove s[i:j]
        # and use previous knowledge about max deletion operations for
        # s[j:] to get an optimal op count
        if lcs[i][j] >= j-i:
          dp[i] = max(dp[i], dp[j]+1)

    return dp[0]


  def deleteString(self, s: str) -> int:
    n = len(s)
    
    @lru_cache(None)
    def cmp(i: int, j: int) -> bool:
      return s[i:j] == s[j:j+j-i]
    
    @lru_cache(None)
    def dp(i: int) -> int:
      if i == n-1:
        return 1
      
      if len(set(s[i:])) == 1:
        return n-i
      
      most = 1
      for j in range(i+1, n):
        if j-i > n-j:
          break
          
        if not cmp(i, j):
          continue
          
        most = max(most, 1+dp(j))
        
      return most
      
    return dp(0)
      