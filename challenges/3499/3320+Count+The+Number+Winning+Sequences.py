'''
3320. Count The Number of Winning Sequences
'''

from functools import cache


class Solution:
  def countWinningSequences(self, s: str) -> int:
    mod = 10**9 + 7
    n = len(s)
    key = {
      'F': 0,
      'W': 1,
      'E': 2,
    }
    
    @cache
    def dp(i: int, bal: int, prev: int) -> int:
      if i >= n:
        return 1 if bal > 0 else 0
      
      # lose anyway
      if n-i+bal < 1:
        return 0
      
      # win anyway
      if bal-(n-i) > 1:
        return pow(2, n-i, mod)
      
      cnt = 0
      alice = key[s[i]]
      
      for bob in range(3):
        # can't do consecutive summon
        if bob == prev:
          continue
          
        if (bob == 0 and alice == 2) or (bob-alice == 1):
          # bob wins the round
          c = dp(i+1, bal+1, bob)
        elif bob == alice:
          # draw
          c = dp(i+1, bal, bob)
        else:
          # bob loses
          c = dp(i+1, bal-1, bob)
            
        cnt += c
      
      # print('done:', (i, bal, prev), cnt)
      return cnt % mod
      
    return dp(0, 0, -1)
    