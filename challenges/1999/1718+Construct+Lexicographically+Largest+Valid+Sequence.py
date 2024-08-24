'''
1718. Construct the Lexicographically Largest Valid Sequence

Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]

Constraints:

1 <= n <= 20
'''

from typing import List

class Solution:
  def constructDistancedSequence(self, n: int) -> List[int]:
    if n == 1:
      return [1]
    
    count = 1 + 2*(n-1)
    seq = [0]*count
    target = (1 << (n+1)) - 2
    # print('t:', bin(target)[2:])
    
    def check(i: int, val: int, mask: int):
      if val == 1:
        return True
      
      # already used
      if (1<<val) & mask > 0:
        return False
          
      # the other number is out of bound
      if i+val >= count:
        return False
          
      # position already taken
      if seq[i+val] > 0:
        return False
      
      return True
    
    def dp(i: int, mask: int):
      if mask == target:
        return True
      
      if i >= count:
        return False
      
      if seq[i] > 0:
        return dp(i+1, mask)
      
      # print('check:', i, seq)
      
      for val in range(n, 0, -1):
        if not check(i, val, mask):
          continue
          
        seq[i] = val
        if val > 1:
          seq[i+val] = val
        
        if dp(i+1, mask | (1<<val)):
          return True
        
        seq[i] = 0
        if val > 1:
          seq[i+val] = 0
        
      return False
      
    dp(0, 0)
    
    return seq
        