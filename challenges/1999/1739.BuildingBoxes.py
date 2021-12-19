'''
You have a cubic storeroom where the width, length, and height of the room are all equal to n units. You are asked to place n boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:

You can place the boxes anywhere on the floor.
If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
Given an integer n, return the minimum possible number of boxes touching the floor.

Example 1:

Input: n = 3
Output: 3
Explanation: The figure above is for the placement of the three boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.

Example 2:

Input: n = 4
Output: 3
Explanation: The figure above is for the placement of the four boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.

Example 3:

Input: n = 10
Output: 6
Explanation: The figure above is for the placement of the ten boxes.
These boxes are placed in the corner of the room, where the corner is on the back side.

Constraints:

1 <= n <= 10^9
'''


class Solution:
  def minimumBoxes(self, n: int) -> int:
    if n <= 3:
      return n
    
    last = [0, 0]
    base, total, side = 1, 1, 1
    
    # expanding the base to add 1 more layer of 
    # boxes, until we added more boxes than the 
    # required amount, aka `n`
    while total < n:
      last[0], last[1] = base, total
      side += 1
      base += side
      total += base
      
    # print(last, base, total)
    if total == n:
      return base
    
    if last[1]+1 == n:
      return last[0] + 1
    
    base, total = last
    l, r = 1, side
    
    # for every 1 additional box added to the base of
    # the pile, if the box is added to the i-th row, it
    # will let us add a total of 
    #       `sum(val for val in range(1, i))`
    # more boxes, hence we can binary search `i` to find 
    # the row that will let us add enough boxes to fit all
    # n boxes in the pile.
    while l < r:
      m = (l + r) // 2
      curr_total = total + ((1 + m) * m) // 2
      
      if curr_total == n:
        l = m
        break
        
      if curr_total < n:
        l += 1
      else:
        r -= 1
    
    curr_total = total + ((1 + l) * l) // 2
    if curr_total < n:
      l += 1
      
    return base + l
  