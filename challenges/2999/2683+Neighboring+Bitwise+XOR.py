'''
2683. Neighboring Bitwise XOR
'''

from typing import List

class Solution:
  '''
  each element in the original array is used twice to get the derived array, so 
  sum(XOR(item) for item in derived) should equal 0, as all elements from the 
  original array should cancel out in this calculation
  '''
  def doesValidArrayExist(self, derived: List[int]) -> bool:
    n = len(derived)
    base = derived[0]
    
    for i in range(1, n):
      base ^= derived[i]
    
    return base == 0
        