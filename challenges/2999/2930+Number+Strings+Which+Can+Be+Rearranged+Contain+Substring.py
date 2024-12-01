'''
2930. Number of Strings Which Can Be Rearranged to Contain Substring
'''

class Solution:
  def stringCount(self, n: int) -> int:
    prev = {
      (0, 0, 0): 1,
      (0, 0, 1): 0,
      (0, 0, 2): 0,
      (0, 1, 0): 0,
      (0, 1, 1): 0,
      (0, 1, 2): 0,
      (1, 0, 0): 0,
      (1, 0, 1): 0,
      (1, 0, 2): 0,
      (1, 1, 0): 0,
      (1, 1, 1): 0,
      (1, 1, 2): 0,
    }
    dp = {}
    
    mod = 10**9 + 7
    
    for i in range(n):
      dp.clear()
      
      dp[0, 0, 0] = (23*prev[0, 0, 0]) % mod
      dp[0, 0, 1] = (prev[0, 0, 0] + 23*prev[0, 0, 1]) % mod
      dp[0, 0, 2] = (prev[0, 0, 1] + 24*prev[0, 0, 2]) % mod
      
      dp[0, 1, 0] = (prev[0, 0, 0] + 24*prev[0, 1, 0]) % mod
      dp[0, 1, 1] = (prev[0, 0, 1] + prev[0, 1, 0] + 24*prev[0, 1, 1]) % mod
      dp[0, 1, 2] = (prev[0, 0, 2] + prev[0, 1, 1] + 25*prev[0, 1, 2]) % mod
      
      dp[1, 0, 0] = (prev[0, 0, 0] + 24*prev[1, 0, 0]) % mod
      dp[1, 0, 1] = (prev[0, 0, 1] + prev[1, 0, 0] + 24*prev[1, 0, 1]) % mod
      dp[1, 0, 2] = (prev[0, 0, 2] + prev[1, 0, 1] + 25*prev[1, 0, 2]) % mod
      
      dp[1, 1, 0] = (prev[0, 1, 0] + prev[1, 0, 0] + 25*prev[1, 1, 0]) % mod
      dp[1, 1, 1] = (prev[0, 1, 1] + prev[1, 0, 1] + prev[1, 1, 0] + 25*prev[1, 1, 1]) % mod
      dp[1, 1, 2] = (prev[0, 1, 2] + prev[1, 0, 2] + prev[1, 1, 1] + 26*prev[1, 1, 2]) % mod
      
      # print('iter:', i, dp)
      dp, prev = prev, dp
      
    return prev[1, 1, 2]
  