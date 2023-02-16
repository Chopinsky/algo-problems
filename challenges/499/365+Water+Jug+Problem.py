'''
365. Water and Jug Problem

You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
 

Example 1:

Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example 
Example 2:

Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false
Example 3:

Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true

Constraints:

1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
'''

from math import gcd


class Solution:
  '''
  the trick is that eventually, we can only get the amount of waters 
  that are multiples of the gcd(j1, j2) 
  '''
  def canMeasureWater(self, j1: int, j2: int, t: int) -> bool:
    if t > j1+j2:
      return False
    
    return t % gcd(j1, j2) == 0
    
    
  def canMeasureWater0(self, j1: int, j2: int, t: int) -> bool:
    if t > j1+j2:
      return False
    
    def found(a: int, b: int) -> bool:
      return t == a or t == b or t == a+b
      
    if found(j1, j2):
      return True
    
    if j1 == j2:
      return False
    
    if j1 > j2:
      j1, j2 = j2, j1
      
    stack = [(j1, j2)]
    seen = set(stack)
    
    def add(a: int, b: int) -> bool:
      if a == 0:
        a = j1
        
      if b == 0:
        b = j2
        
      if (a, b) not in seen:
        stack.append((a, b))
        seen.add((a, b))
        
      return found(a, b)

    while stack:
      a, b = stack.pop()
      
      '''a moves'''
      # refill a from source
      if add(j1, b):
        return True

      # refill (all or part of) a from b
      move = min(j1-a, b)
      if add(a+move, b-move):
        return True

      # empty b and move a to b and refill a
      if add(j1, a):
        return True
        
      # add b to full from source
      if add(a, j2):
        return True
      
      '''b moves'''
      # refill (all or part of) b from a
      move = min(j2-b, a)
      if add(a-move, b+move):
        return True

      # empty a and put b in a if b <= j1
      if b <= j1 and add(b, j2):
        return True
    
    # print(seen)
    return False
    