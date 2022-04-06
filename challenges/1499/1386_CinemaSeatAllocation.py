'''

A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

Example 1:

Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.
Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4

Constraints:

1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
All reservedSeats[i] are distinct.
'''

from typing import List


class Solution:
  def maxNumberOfFamilies(self, n: int, reserved: List[List[int]]) -> int:
    count = 0
    reserved.sort()
    reserved.append([n+1, 0])
    curr_row = 0
    row_seats = 0
    
    s1 = 15 << 1
    s2 = 15 << 5
    s3 = s1 | s2
    s4 = 15 << 3
    # print('{0:b}'.format(s3))
    # print('{0:b}'.format(s4))
    
    for r, c in reserved:
      if r != curr_row:
        # print(curr_row, '{0:b}'.format(row_seats))
        
        # count seats from the last row
        if curr_row > 0:
          if row_seats & s3 == 0:
            count += 2
            
          elif row_seats & s4 == 0 or row_seats & s1 == 0 or row_seats & s2 == 0:
            count += 1
            
        # count free rows between
        if r - curr_row > 1:
          free_rows = r - curr_row - 1
          count += free_rows * 2
          
        curr_row = r
        row_seats = 0
      
      if r <= n:
        row_seats |= 1 << (c-1)
    
    return count
  