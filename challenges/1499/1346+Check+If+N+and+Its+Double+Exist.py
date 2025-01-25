from typing import List

class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    if arr.count(0) > 1:
      return True
    
    vals = set(arr)
    for val in vals:
      if val == 0:
        continue
      
      if 2*val in vals:
        return True
      
    return False
        