'''
Given an array of positive integers target and an array initial of same size with all zeros.

Return the minimum number of operations to form a target array from initial if you are allowed to do the following operation:

Choose any subarray from initial and increment each value by one.
The answer is guaranteed to fit within the range of a 32-bit signed integer.

Example 1:

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.

Example 2:

Input: target = [3,1,1,2]
Output: 4
Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).

Example 3:

Input: target = [3,1,5,4,2]
Output: 7
Explanation: (initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] 
                                  -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target).

Example 4:

Input: target = [1,1,1,1]
Output: 1

Constraints:

1 <= target.length <= 10^5
1 <= target[i] <= 10^5
'''


from typing import List


class Solution:
  def minNumberOperations(self, target: List[int]) -> int:
    ops = 0
    base = 0
    stack = []
    
    for i, n in enumerate(target):
      # skip continuous numbers
      if i > 0 and n == target[i-1]:
        continue
        
      # init
      if not stack:
        stack.append(n)
        continue
      
      # climbing up, update the peak
      if (len(stack) == 1 and n > stack[-1]):
        stack[-1] = n
        continue

      # climbing down, keep appending
      if n <= stack[-1]:
        if n < stack[-1]:
          stack.append(n)
        
        continue
      
      # passing through a mountain, rising again
      ops += stack[0] - base
      # print(i, n, base, stack, ops)
      
      # resetting the base and the queue
      base = stack[-1]
      stack.clear()
      stack.append(n)
      
    return ops + (0 if not stack else stack[0]-base)
    
    