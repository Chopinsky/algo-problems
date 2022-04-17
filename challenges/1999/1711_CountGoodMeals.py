'''
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

You can pick any two different foods to make a good meal.

Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

Note that items with different indices are considered different even if they have the same deliciousness value.

Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
 

Constraints:

1 <= deliciousness.length <= 10^5
0 <= deliciousness[i] <= 2^20
'''

from typing import List
from collections import Counter


class Solution:
  def countPairs(self, delic: List[int]) -> int:
    c = Counter(delic)
    top = max(c)
    val = 1
    target = []
    
    while val < top*2:
      target.append(val)
      val <<= 1
      
    # print(target, c)
    count = 0
    seen = set()
    
    for v0 in sorted(c):
      for t in target:
        if t <= v0 or t-v0 not in c:
          continue
          
        v0, v1 = min(v0, t-v0), max(v0, t-v0)
        if (v0, v1) in seen:
          continue
          
        seen.add((v0, v1))
        # print(v0, v1, c[v0], c[v1])
        
        if v0 == v1:
          count += max(0, c[v0] * (c[v0] - 1) // 2)
        else:
          count += c[v0] * c[v1]
          
    return count % (10**9 + 7)
          