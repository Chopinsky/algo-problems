'''
You are given an integer array rolls of length n and an integer k. You roll a k sided dice numbered from 1 to k, n times, where the result of the ith roll is rolls[i].

Return the length of the shortest sequence of rolls that cannot be taken from rolls.

A sequence of rolls of length len is the result of rolling a k sided dice len times.

Note that the sequence taken does not have to be consecutive as long as it is in order.

Example 1:

Input: rolls = [4,2,1,2,3,3,2,4,1], k = 4
Output: 3
Explanation: Every sequence of rolls of length 1, [1], [2], [3], [4], can be taken from rolls.
Every sequence of rolls of length 2, [1, 1], [1, 2], ..., [4, 4], can be taken from rolls.
The sequence [1, 4, 2] cannot be taken from rolls, so we return 3.
Note that there are other sequences that cannot be taken from rolls.
Example 2:

Input: rolls = [1,1,2,2], k = 2
Output: 2
Explanation: Every sequence of rolls of length 1, [1], [2], can be taken from rolls.
The sequence [2, 1] cannot be taken from rolls, so we return 2.
Note that there are other sequences that cannot be taken from rolls but [2, 1] is the shortest.
Example 3:

Input: rolls = [1,1,3,2,2,2,3,3], k = 4
Output: 1
Explanation: The sequence [4] cannot be taken from rolls, so we return 1.
Note that there are other sequences that cannot be taken from rolls but [4] is the shortest.

Constraints:

n == rolls.length
1 <= n <= 10^5
1 <= rolls[i] <= k <= 10^5
'''

from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution:
  '''
  this is a pretty difficult mind game without seeing hints ... basic idea is that to obtain
  all combinations of numbers 1~n with length k, we must be able to obtain all
  combinations of the numbers with length k-1, and we should be able to find numbers 1~n after
  the last index where we can obtain the k-1 length combinations; so we just rinse and repeat,
  until a point where we can no longer get all 1~n numbers after an array index, and this will
  be the roll length that we won't find a combination at this length. 
  '''
  def shortestSequence(self, rolls: List[int], k: int) -> int:
    nums = sorted(set(rolls))
    if len(nums) < k or nums[k-1] != k:
      return 1
    
    nums = nums[:k]
    pos = defaultdict(list)
    n = len(rolls)
    
    for i in range(n):
      pos[rolls[i]].append(i)
      
    # print(pos)
    ln, last_idx = 1, -1
    done = False
    
    while not done:
      nxt_idx = -1
      for num in nums:
        idx = bisect_right(pos[num], last_idx)
        if idx >= len(pos[num]):
          done = True
          break
          
        nxt_idx = max(nxt_idx, pos[num][idx])
        
      if nxt_idx < 0:
        done = True
        break
        
      if not done:
        # print('iter:', ln, nxt_idx)
        last_idx = nxt_idx
        ln += 1
    
    return ln
    