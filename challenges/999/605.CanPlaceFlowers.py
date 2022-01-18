'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''


from typing import List


class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    if len(flowerbed) == 1:
      return True if (flowerbed[0] == 0) else (n == 0)
    
    if 1 not in flowerbed:
      return (len(flowerbed)+1) // 2 >= n
    
    ln = 0
    init = True if flowerbed[0] == 0 else False
    
    for val in flowerbed:
      if n <= 0:
        break
      
      if val == 0:
        ln += 1
        continue
        
      if n > 0:
        if init:
          n -= ln // 2
          init = False
        elif ln >= 1:
          n -= (ln-1) // 2
      
      # print(val, ln, n)
      ln = 0
    
    if ln > 0 and n > 0:
      n -= ln // 2

    # print(n, ln)
    return n <= 0
  