'''
Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

Example 1:

Input: nums = [1,4,2,7], low = 2, high = 6
Output: 6
Explanation: All nice pairs (i, j) are as follows:
    - (0, 1): nums[0] XOR nums[1] = 5 
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5
Example 2:

Input: nums = [9,8,4,2,1], low = 5, high = 14
Output: 8
Explanation: All nice pairs (i, j) are as follows:
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 2 * 10^4
1 <= low <= high <= 2 * 10^4
'''


from typing import List
from collections import defaultdict


class Solution:
  def countPairs(self, nums: List[int], low: int, high: int) -> int:
    trie = {0: None, 1: None, 'c': 0}
    c = defaultdict(int)
    count = 0
    
    def insert(val: int):
      c[val] += 1
      curr = trie
      curr['c'] += 1
      
      for i in range(15, -1, -1):
        bit = (val >> i) & 1
        
        if not curr[bit]:
          curr[bit] = {
            0: None,
            1: None,
            'c': 0,
          }
          
        curr = curr[bit]
        curr['c'] += 1
        
    def query(val: int, upper: int) -> int:
      if upper <= 0:
        return c[val] if upper == 0 else 0
      
      base = 0
      cnt = 0
      curr = trie
      
      for i in range(15, -1, -1):
        if not curr:
          break
          
        bit = (val >> i) & 1
        
        # can add 1<<i @ i-th bit, add all 0s @ i-th bit
        if (base | (1 << i)) <= upper:
          cnt += curr[bit]['c'] if curr[bit] else 0
          curr = curr[1-bit]
          base |= 1 << i
          
        # must be 0 @ i-th bit
        else:
          curr = curr[bit]
      
      return cnt + (curr['c'] if curr else 0)
    
    for val in nums:
      h, l = query(val, high), query(val, low-1)
      # print(val, h, l)
      count += h - l
      insert(val)
      
    # print(trie)
    return count
    