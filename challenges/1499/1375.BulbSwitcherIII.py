'''
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb changes color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned-on bulbs are blue.

Example 1:

Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.

Example 2:

Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).

Example 3:

Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.

Example 4:

Input: light = [2,1,4,3,6,5]
Output: 3

Example 5:

Input: light = [1,2,3,4,5,6]
Output: 6

Constraints:

n == light.length
1 <= n <= 5 * 10^4
light is a permutation of the numbers in the range [1, n]
'''


from typing import List


class Solution:
  def numTimesAllBlue(self, light: List[int]) -> int:
    n, count = len(light), 0
    last_off, top = 1, light[0]
    off = set([i+1 for i in range(n)])
    
    for i in light:
      off.discard(i)
      top = max(top, i)
      
      while (last_off <= n) and (last_off not in off):
        last_off += 1
        
      # print(i, last_off, top, 'add' if last_off > top else '', off)
      if last_off > top:
        count += 1
    
    return count
  