from typing import List

class Solution:
  def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    count = 0
    for val in arr:
      if val%2 == 0:
        count = 0
        continue
        
      count += 1
      if count >= 3:
        return True
      
    return False
        