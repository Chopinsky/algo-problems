'''
Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
Example 2:

Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.

Constraints:

1 <= k <= houses.length <= 100
1 <= houses[i] <= 10^4
All the integers of houses are unique.
'''


from typing  import List
from functools import lru_cache


class Solution:
  def minDistance(self, houses: List[int], k: int) -> int:
    n = len(houses)
    if k >= n:
      return 0
    
    houses.sort()
    
    @lru_cache(None)
    def calc_dist(i: int, j: int) -> int:
      j = min(j, n-1)
      if i >= j:
        return 0
      
      dist = houses[i+1] - houses[i]
      if i+1 == j:
        return dist

      # the starting index for the right-part, left part contains
      # houses in [i, p0-1], right part contains [p0, p1]
      p0 = i+1

      # adding houses to this section until we visited all houses
      # in the [i, j] index range
      for p1 in range(i+2, j+1):
        # lc: number of houses on the left; rc: number of hosues on
        # the right side of p0
        lc, rc = p0-i, p1-p0

        # add: if we just add house-p1 to the right
        add = houses[p1] - houses[p0-1]
        # move: if we move the mailbox to p0, and then add house-p1 to the right
        move = houses[p1] - houses[p0] + (lc-rc) * (houses[p0]-houses[p0-1])
        # print('pos:', p0, p1, add, move, dist)

        if add <= move:
          # don't move p0 is a better distance choice
          # print('df1', dist, add)
          dist += add
        else:
          # move p0 yields a better distance
          # print('df2', dist, (houses[p1] - houses[p0]), (lc-rc) * (houses[p0]-houses[p0-1]))
          dist += move
          p0 += 1

      # print('fin pos:', p0)
      return dist
    
    @lru_cache(None)
    def dp(i: int, rem: int) -> int:
      # only 1 mailbox left for all remainder houses
      if rem == 1:
        return calc_dist(i, n-1)
      
      # one mailbox for each house
      if n-i <= rem:
        return 0
      
      # if mailbox is on houses[i]
      dist = dp(i+1, rem-1)
      
      # if we include more than 1 house in this section
      for j in range(i+1, n-rem):
        dist = min(dist, calc_dist(i, j)+dp(j+1, rem-1))
      
      return dist
    
    return dp(0, k)
      