'''
3207. Maximum Points After Enemy Battles
'''

from typing import List

class Solution:
  def maximumPoints(self, enermy: List[int], energy: int) -> int:
    points = 0
    enermy.sort()
    if energy < enermy[0]:
      return points
    
    n = len(enermy)
    i = n-1
    # print('init:', enermy)
    
    while i >= 0:
      # print('iter:', i, energy)
      
      if energy >= enermy[0]:
        cnt, energy = divmod(energy, enermy[0])
        points += cnt
        
      # not going to do op-2
      if points == 0 or i < 0:
        break
        
      energy += enermy[i]
      i -= 1
    
    return points    
