'''
You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.

Constraints:

2 <= properties.length <= 10^5
properties[i].length == 2
1 <= attacki, defensei <= 10^5
'''

from typing import List
from collections import defaultdict


class Solution:
  def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
    chars = defaultdict(list)
    count = 0
    large = -1
    
    for a, d in properties:
      chars[a].append(d)
    
    for a in sorted(chars, reverse=True):
      nxt_large = -1
      for d in chars[a]:
        if d < large:
          count += 1
          
        nxt_large = max(nxt_large, d)
        
      large = max(large, nxt_large)
    
    return count
    

  def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
    properties.sort(reverse=True)
    hd, count = 0, 0
    tmp = [0, 0]
    
    for a, d in properties:
      if a != tmp[0]:
        hd = max(hd, tmp[1])
        tmp[0], tmp[1] = a, d
      
      if d < hd:
        count += 1
      
    return count
  
