import heapq

'''
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1]
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].

Example 3:

Input: target = [8,5]
Output: true

Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9
'''

from heapq import heappush, heappop
from typing import List


class Solution:
  def isPossible(self, target: List[int]) -> bool:
    s = 0
    stack = []
    
    for val in target:
      s += val
      heappush(stack, -val)
      
    while stack[0] != -1:
      val = -heappop(stack)
      rest = s - val
      if rest <= 0:
        # print('1', rest)
        return False
      
      if rest == 1 and val >= 1:
        break
      
      cnt = val // rest
      if cnt < 1 or val == rest:
        # print('2', cnt)
        return False
      
      nxt_val = val - rest*cnt
      if nxt_val <= 0:
        # print('3', nxt_val, val, rest, cnt)
        return False
      
      heappush(stack, -nxt_val)
      s += nxt_val - val
      
    return True
    

  def isPossible(self, arr: List[int]) -> bool:
    if len(arr) == 1:
      return True if arr[0] == 1 else False

    h = []
    s = 0

    for val in arr:
      s += val
      heapq.heappush(h, -val)

    while len(h) > 0 and h[0] < -1:
      val = -heapq.heappop(h)
      rest = s - val
      if rest == 1:
        return True

      if val <= rest or rest <= 0:
        return False

      next_val = val % rest
      # print(val, rest, next_val)

      s = rest + next_val
      heapq.heappush(h, -next_val)

    return True
