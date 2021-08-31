'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

* Insert a character
* Delete a character
* Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''

class Solution:
  # bottom up dp
  def minDistance(self, word1: str, word2: str) -> int:
    l1, l2 = len(word1), len(word2)
    dp = [[float('inf') for _ in range(l2+1)] for _ in range(l1+1)]
    
    for i in range(l1+1):
      dp[i][0] = i
    
    for j in range(l2+1):
      dp[0][j] = j
      
    for i in range(1, l1+1):
      for j in range(1, l2+1):
        # replace
        dp[i][j] = dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1)
        
        # the other situations
        dp[i][j] = min(
          dp[i][j],       # replace
          dp[i-1][j] + 1, # insert
          dp[i][j-1] + 1, # delete
        )
    
    return dp[-1][-1]

  # top down dp
  def minDistance0(self, word1: str, word2: str) -> int:
    cache = {}
    
    def dp(i1: int, i2: int) -> int:
      # insert all chars from word2[i2:]
      if i1 >= len(word1):
        return len(word2[i2:])
      
      # delete all remainder chars in word1[i1:]
      if i2 >= len(word2):
        return len(word1[i1:])
        
      if (i1, i2) in cache:
        return cache[i1, i2]
      
      count = len(word1[i1:]) + len(word2[i2:])
      
      # replace one char at word1[i1] to word2[i2] if they're
      # different
      count = min(count, dp(i1+1, i2+1) + (1 if word1[i1] != word2[i2] else 0))
      
      # insert one char at word2[i2]
      count = min(count, dp(i1, i2+1) + 1)
      
      # delete one char at word1[i1]
      count = min(count, dp(i1+1, i2) + 1)
      
      cache[i1, i2] = count
      return count
    
    return dp(0, 0)
  
