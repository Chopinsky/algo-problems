'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

1 <= numRows <= 30
'''

from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    curr = [1]
    ans = [curr]
    
    while numRows > 1:
      nxt = [1]
      for i in range(1, len(curr)):
        nxt.append(curr[i]+curr[i-1])
      
      nxt.append(1)
      numRows -= 1
      curr = nxt
      ans.append(curr)
      
    return ans
      
      
  def generate(self, numRows: int) -> List[List[int]]:
    ans = [[1]]
    
    for i in range(1, numRows):
      row = [1]
      last = ans[-1]
      
      for j in range(1, i):
        row.append(last[j]+last[j-1])
        
      row.append(1)
      ans.append(row)
      
    return ans
  