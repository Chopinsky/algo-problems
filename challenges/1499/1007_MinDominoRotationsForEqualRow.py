'''
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Example 1:

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 10^4
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
'''


from typing import List
import math


class Solution:
  def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    for val in (tops[0], bottoms[0]):
      if all(val in d for d in zip(tops, bottoms)):
        return len(tops) - max(tops.count(val), bottoms.count(val))
      
    return -1
  
  
  def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    cnt0, cnt1 = 0, 0
    n = len(tops)
    
    def count(val: int, a: List[int], b: List[int]) -> int:
      cnt = 0
      for i in range(n):
        if a[i] != val and b[i] != val:
          return math.inf
        
        if a[i] == val:
          continue
          
        cnt += 1
        
      return cnt
          
    c0 = count(tops[0], tops, bottoms)
    c1 = count(bottoms[0], tops, bottoms)
    c2 = count(tops[0], bottoms, tops)
    c3 = count(bottoms[0], bottoms, tops)
    res = min(c0, c1, c2, c3)
    
    return -1 if res == math.inf else res
    