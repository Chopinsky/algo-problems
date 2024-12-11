'''
2358. Maximum Number of Groups Entering a Competition
'''

from typing import List


class Solution:
  def maximumGroups(self, grades: List[int]) -> int:
    n = len(grades)
    if n < 3:
      return 1
    
    grades.sort()
    groups = [1]
    ln = 1
    
    while ln+groups[-1]+1 <= n:
      groups.append(groups[-1]+1)
      ln += groups[-1]
        
    if groups[-1] <= groups[-2]:
      groups[-1] += groups.pop()
      
    return len(groups)
        