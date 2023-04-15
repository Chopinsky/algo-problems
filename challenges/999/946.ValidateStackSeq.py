'''
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
'''


from typing import List


class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    if len(pushed) != len(popped):
      return False
    
    idx = 0
    stack = []
    n = len(popped)
    
    for val in pushed:
      stack.append(val)
      while stack and idx < n and popped[idx] == stack[-1]:
        stack.pop()
        idx += 1
        
    return idx == n
    
    
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    i, stack = 0, []
    for x in pushed:
      while stack and stack[-1] == popped[i]:
        stack.pop()
        i += 1

      stack.append(x)

    while stack and stack[-1] == popped[i]:
      stack.pop()
      i += 1

    return not stack
    
    
  def validateStackSequences0(self, pushed: List[int], popped: List[int]) -> bool:
    if len(pushed) != len(popped):
      return False
    
    stack = []
    i, j = 0, 0
    n = len(popped)
    
    while j < n:
      # pop first
      while stack and stack[-1] == popped[j]:
        stack.pop()
        j += 1
        
      if j == n and i < n:
        return False
      
      # now push
      if i < n:
        stack.append(pushed[i])
        i += 1
        
      if i >= n and stack and j < n and stack[-1] != popped[j]:
        return False
    
    return i == n and j == n
    