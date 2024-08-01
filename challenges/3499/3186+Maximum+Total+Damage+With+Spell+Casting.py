'''
3186. Maximum Total Damage With Spell Casting

A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

Constraints:

1 <= power.length <= 10^5
1 <= power[i] <= 10^9
'''

from collections import Counter
from typing import List

class Solution:
  def maximumTotalDamage(self, power: List[int]) -> int:
    damage = []
    powers = Counter(power)
    cand = sorted(powers)
    prev_max = 0
    # print(powers)
    
    for p in cand:
      idx = len(damage)-1
      curr = powers[p]*p
      
      while idx >= 0 and damage[idx][0]+2 >= p:
        idx -= 1
      
      if idx >= 0:
        curr += damage[idx][1]
        
      damage.append((p, max(prev_max, curr)))
      prev_max = max(prev_max, curr)
    
    # print(damage)
    
    return damage[-1][1]
    