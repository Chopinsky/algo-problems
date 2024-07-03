'''
3147. Taking Maximum Energy From the Mystic Dungeon

In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.

In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.

You are given an array energy and an integer k. Return the maximum possible energy you can gain.
'''

from typing import List

class Solution:
  def maximumEnergy(self, energy: List[int], k: int) -> int:
    dp = [val for val in energy]
    n = len(energy)
    
    for i in range(n):
      if i+k < n:
        dp[i+k] = max(dp[i+k], dp[i]+energy[i+k])
        
    # print(dp)
    return max(dp[-k:])
        