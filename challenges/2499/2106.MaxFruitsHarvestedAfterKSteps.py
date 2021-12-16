'''
Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.

You are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.

 

Example 1:


Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
Output: 9
Explanation: 
The optimal way is to:
- Move right to position 6 and harvest 3 fruits
- Move right to position 8 and harvest 6 fruits
You moved 3 steps and harvested 3 + 6 = 9 fruits in total.
Example 2:

Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
Output: 14
Explanation: 
You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
The optimal way is to:
- Harvest the 7 fruits at the starting position 5
- Move left to position 4 and harvest 1 fruit
- Move right to position 6 and harvest 2 fruits
- Move right to position 7 and harvest 4 fruits
You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.
Example 3:


Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
Output: 0
Explanation:
You can move at most k = 2 steps and cannot reach any position with fruits.
 

Constraints:

1 <= fruits.length <= 105
fruits[i].length == 2
0 <= startPos, positioni <= 2 * 105
positioni-1 < positioni for any i > 0 (0-indexed)
1 <= amounti <= 10^4
0 <= k <= 2 * 10^5
'''


from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
    fpos = [f[0] for f in fruits]
    prefix = [f[1] for f in fruits]
    n = len(fruits)
    
    if not k:
      idx = bisect_left(fpos, startPos)
      if idx < len(fruits) and fpos[idx] == startPos:
        return prefix[idx]
      
      return 0
      
    for i in range(1, len(prefix)):
      prefix[i] += prefix[i-1]
    
    idx = bisect_left(fpos, startPos-k)
    ldx = bisect_right(fpos, startPos) - 1
    total = 0
    
    # print('prefix', prefix, fpos)
    # print('init', idx, fpos[idx], ldx, fpos[ldx] if ldx >= 0 else None)
    
    while idx < n:
      pos = fpos[idx]
      if pos >= startPos and pos-startPos > k:
        break
        
      if abs(pos-startPos) > k:
        idx += 1
        continue
      
      count = 0
      rem = k - 2 * abs(startPos - pos)
      
      if pos <= startPos:
        if ldx >= 0:
          count += prefix[ldx] - (prefix[idx-1] if idx > 0 else 0)
          
        if rem > 0:
          right = startPos + rem
          jdx = bisect_right(fpos, right) - 1

          if jdx >= 0 and fpos[jdx] > startPos:
            count += prefix[jdx] - (prefix[ldx] if ldx >= 0 else 0)
        
      else:
        count += prefix[idx] - (prefix[ldx] if ldx >= 0 else 0)
        
        if rem > 0:
          left = startPos - rem
          jdx = bisect_left(fpos, left)
          
          if jdx < n and fpos[jdx] <= startPos:
            count += prefix[ldx] - (prefix[jdx-1] if jdx > 0 else 0)
      
      # print('iter:', idx, pos, count)
      total = max(total, count)
      idx += 1
      
    return total
      