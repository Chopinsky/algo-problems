'''
2275. Largest Combination With Bitwise AND Greater Than Zero

The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND greater than 0.

Example 1:

Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.
Example 2:

Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.
 

Constraints:

1 <= candidates.length <= 105
1 <= candidates[i] <= 107
'''

from typing import List
from collections import defaultdict


class Solution:
  '''
  the trick is to let the AND value of a subset to be greater than 0, all numbers
  in the subset must have a digit in its binary form that are all '1'; so we just
  need to find the digit that are all 1.
  '''
  def largestCombination(self, candidates: List[int]) -> int:
    counter = defaultdict(int)
    for val in candidates:
      n = 0
      base = 1
      
      while base <= val:
        if base & val > 0:
          counter[n] += 1
          
        n += 1
        base <<= 1
        
    # print(counter)
    return max(counter.values())
    