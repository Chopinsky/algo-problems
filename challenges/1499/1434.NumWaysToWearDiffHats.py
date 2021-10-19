'''
There are n people and 40 types of hats labeled from 1 to 40.

Given a list of list of integers hats, where hats[i] is a list of all hats preferred by the i-th person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to choose hats given the conditions. 
First person choose hat 3, Second person choose hat 4 and last one hat 5.

Example 2:

Input: hats = [[3,5,1],[3,5]]
Output: 4
Explanation: There are 4 ways to choose hats
(3,5), (5,3), (1,3) and (1,5)

Example 3:

Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
Output: 24
Explanation: Each person can choose hats labeled from 1 to 4.
Number of Permutations of (1,2,3,4) = 24.

Example 4:

Input: hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
Output: 111

Constraints:

n == hats.length
1 <= n <= 10
1 <= hats[i].length <= 40
1 <= hats[i][j] <= 40
hats[i] contains a list of unique integers.
'''


from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
  '''
  trick is to gather ppl for hats, instead of putting hats on ppl
  '''
  def numberWays(self, hats: List[List[int]]) -> int:
    mod = 1_000_000_007
    hat_ppl = defaultdict(list)
    
    for i, h in enumerate(hats):
      for hn in h:
        hat_ppl[hn].append(i)
    
    hat_arr = sorted(hat_ppl.keys(), key=lambda x: len(hat_ppl[x]))
    n = len(hat_arr)
    tgt = (1 << len(hats)) - 1
    # print(hat_ppl, hat_arr, bin(tgt))

    @lru_cache(None)
    def dp(i: int, assigned: int) -> int:
      if i >= n:
        # print(bin(assigned))
        return 1 if (assigned == tgt) else 0
      
      h = hat_arr[i]
      total = dp(i+1, assigned) # if don't use this hat on ppl
      # print('init', i, bin(assigned))
      
      for ppl in hat_ppl[h]:
        idx = 1 << ppl
        if idx & assigned > 0:
          continue
          
        total += dp(i+1, assigned | idx)
        
      return total % mod
    
    return dp(0, 0)
    