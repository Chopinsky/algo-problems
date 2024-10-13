'''
3317. Find the Number of Possible Ways for an Event
'''

from functools import cache
from math import comb

MOD = 10**9 + 7


@cache
def dp(n: int, s: int) -> int:
  '''
  number of settings to assign n-people to s-stages
  '''
  if n < s: 
    return 0

  if s == 1: 
    return 1
  
  # pick one stage from s possible options, assign someone
  # to it and move on (never assign anyone else to it), or 
  # assign someone to it and still keep it in the options-pool
  return s * (dp(n-1, s) + dp(n-1, s-1)) % MOD


class Solution:
  def numberOfWays(self, n: int, x: int, y: int) -> int:
    cnt = 0
    
    for s in range(min(n, x)):
      # pad 1 to get the stage count
      s += 1
      
      # get different possible settings
      stage_settings = comb(x, s)
      ppl_settings = dp(n, s)
      score_settings = pow(y, s, MOD)
      
      # update total count
      cnt = (cnt + stage_settings * ppl_settings * score_settings) % MOD

    return cnt
    