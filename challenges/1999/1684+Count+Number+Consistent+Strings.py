'''
1684. Count the Number of Consistent Strings
'''

from typing import List

class Solution:
  def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    chars = set(allowed)
    count = 0
    
    for w in words:
      c = set(w)
      consistent = True
      
      for ch in c:
        if ch not in chars:
          consistent = False
          break
          
      if consistent:
        count += 1
      
    return count
        