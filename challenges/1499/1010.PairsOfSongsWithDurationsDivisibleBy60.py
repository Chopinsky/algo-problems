'''
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 10^4
1 <= time[i] <= 500
'''


from typing import List
from collections import defaultdict


class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    mod_60 = defaultdict(int)
    score = 0
    
    for t in time:
      mod_60[t % 60] += 1

    # 30 + 30 == 60
    score += mod_60[30] * (mod_60[30] - 1) // 2 
    
    # 60 + 60 == 120
    score += mod_60[0] * (mod_60[0] - 1) // 2
    
    # get all pairs
    for i in range(1, 30):
      score += mod_60[i] * mod_60[60-i]

    return score
  
      
  def numPairsDivisibleBy60a(self, time: List[int]) -> int:
    song_len = defaultdict(int)
    count = 0
    max_t = 0
  
    for t in time:
      target = 60
      while target <= max_t + t:
        if target - t in song_len:
          count += song_len[target-t]
          
        target += 60
      
      max_t = max(max_t, t)
      song_len[t] += 1
    
    return count
  