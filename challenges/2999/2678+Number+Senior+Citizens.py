'''
2678. Number of Senior Citizens
'''

from typing import List

class Solution:
  def countSeniors(self, details: List[str]) -> int:
    count = 0
    
    for p in details:
      age = int(p[11:13])
      if age > 60:
        count += 1
    
    return count
    
        