'''
1404. Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  
Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  
Example 3:

Input: s = "1"
Output: 0

Constraints:

1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
'''

from collections import deque


class Solution:
  def numSteps(self, s: str) -> int:
    a = deque(list(int(val) for val in s))
    steps = 0
    
    def add_one():
      carryover = 1
      i = len(a)-1

      while i >= 0 and carryover > 0:
        a[i] += carryover
        carryover = 0

        if a[i] > 1:
          a[i] %= 2
          carryover += 1

        i -= 1

      if carryover > 0:
        a.appendleft(1)

    while len(a) > 1:
      if a[-1] > 0:
        add_one()
        steps += 1

      a.pop()
      steps += 1
      # print('iter:', a)

    return steps

  def numSteps(self, s: str) -> int:
    decimals = [int(ch) for ch in s][::-1]
    ops = 0
    idx = 0
    # print(decimals)
    
    def add(i: int):
      n = len(decimals)
      if i >= n:
        return
      
      while i < n:
        decimals[i] = 1 - decimals[i]
        if decimals[i] == 1:
          break
          
        i += 1
      
      if i >= n:
        decimals.append(1)
    
    while idx < len(decimals)-1:
      if decimals[idx] == 1:
        add(idx+1)
        ops += 1
      
      ops += 1
      idx += 1
    
    return ops
        
  def numSteps(self, s: str) -> int:
    digits = list(s)
    steps = 0
    
    while len(digits) > 1 or digits[-1] != '1':
      # print(steps, digits)
      steps += 1
      
      # even: pop
      if digits[-1] == '0':
        digits.pop()
        continue
        
      # odd: update
      idx = len(digits)-1
      if digits[idx] == '0':
        digits[idx] = '1'
        
      else:
        while idx >= 0 and digits[idx] == '1':
          digits[idx] = '0'
          idx -= 1
          
        if idx >= 0:
          digits[idx] = '1'
        else:
          digits = ['1'] + digits

    return steps
    