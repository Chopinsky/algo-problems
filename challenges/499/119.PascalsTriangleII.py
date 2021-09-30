'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

Constraints:

0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''


from typing import List


class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    row = [1]
    nxt = []
    n = 0
    
    while n < rowIndex:
      nxt.append(1)
      for i in range(1, len(row)):
        nxt.append(row[i] + row[i-1])
        
      nxt.append(1)
      row, nxt = nxt, row
      nxt.clear()
      
      n += 1
      # print(n, row)
      
    return row
  