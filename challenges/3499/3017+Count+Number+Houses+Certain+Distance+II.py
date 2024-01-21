'''
3017. Count the Number of Houses at a Certain Distance II

You are given three positive integers n, x, and y.

In a city, there exist houses numbered 1 to n connected by n streets. There is a street connecting the house numbered i with the house numbered i + 1 for all 1 <= i <= n - 1 . An additional street connects the house numbered x with the house numbered y.

For each k, such that 1 <= k <= n, you need to find the number of pairs of houses (house1, house2) such that the minimum number of streets that need to be traveled to reach house2 from house1 is k.

Return a 1-indexed array result of length n where result[k] represents the total number of pairs of houses such that the minimum streets required to reach one house from the other is k.

Note that x and y can be equal.

Example 1:

Input: n = 3, x = 1, y = 3
Output: [6,0,0]
Explanation: Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.
Example 2:

Input: n = 5, x = 2, y = 4
Output: [10,8,2,0,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), and (5, 4).
- For k == 2, the pairs are (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), and (5, 3).
- For k == 3, the pairs are (1, 5), and (5, 1).
- For k == 4 and k == 5, there are no pairs.
Example 3:

Input: n = 4, x = 1, y = 1
Output: [6,4,2,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), and (4, 3).
- For k == 2, the pairs are (1, 3), (3, 1), (2, 4), and (4, 2).
- For k == 3, the pairs are (1, 4), and (4, 1).
- For k == 4, there are no pairs.

Constraints:

2 <= n <= 10^5
1 <= x, y <= n
'''

from typing import List


class Solution:
  def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
    if x >= y:
      x, y = y, x
      
    ans = [0]*n
    if x+1 >= y:
      for i in range(n):
        ans[i] = 2*(n-i-1)
        
      return ans
      
    lc = x-1
    rc = n-y
    cc = y-x+1
    max_ln = max(
      lc + rc + 1, # left end to right end
      lc + cc//2,  # left to any node in cycle
      rc + cc//2,  # right to any node in cycle
    )
    
    # print('init:', lc, rc, cc, max_ln)
    
    def cycle_cycle(ln: int) -> int:
      if ln > cc//2:
        return 0

      # any arc for i->j and j->i where min_dist(i, j) == ln
      if ln < cc//2 or cc%2 == 1:
        return 2*cc
      
      return cc
    
    def left_cycle(ln: int) -> int:
      if lc == 0 or ln > lc+cc//2:
        return 0
      
      cnt = 0
      if lc >= ln:
        # side to cycle head, and vice versa
        cnt += 2
        
      idx = max(1, x-(ln-1))
      jdx = x - max(0, ln-cc//2)

      # cnt the side <-> cycle cases
      if jdx > idx:
        cnt += 4*(jdx-idx)
      
      # count the jdx <-> cycle case
      if jdx < x:
        cnt += 4 if cc % 2 == 1 else 2
      
      return cnt
    
    def right_cycle(ln: int) -> int:
      if rc == 0 or ln > rc+cc//2:
        return 0
      
      cnt = 0
      if rc >= ln:
        # side to cycle head, and vice versa
        cnt += 2
        
      idx = min(n, y+(ln-1))
      jdx = y + max(0, ln-cc//2)
        
      # cnt the side <-> cycle cases
      if idx > jdx:
        cnt += 4*(idx-jdx)
        
      # count the jdx <-> cycle case
      if jdx > y:
        cnt += 4 if cc % 2 == 1 else 2
          
      return cnt
    
    def side(ln: int, sc: int) -> int:
      if sc == 0 or ln > sc-1:
        return 0
      
      return 2*(sc-ln)
    
    def left_right(ln: int) -> int:
      if lc == 0 or rc == 0 or ln < 3 or ln > lc+rc+1:
        return 0
      
      # end to end
      if ln == lc+rc+1:
        return 2
      
      idx = max(1, x - (ln-2))
      jdx = x-1
      
      # not enough rc for the x-1 <-> right side cases
      if rc < ln-2:
        jdx = x - (ln-rc-1)
        
      if jdx >= idx:
        return 2*(jdx-idx+1)
      
      return 0
    
    for ln in range(1, n):
      if ln > max_ln:
        break

      ans[ln-1] = cycle_cycle(ln) + left_cycle(ln) + right_cycle(ln) + side(ln, lc) + side(ln, rc) + left_right(ln)
      
    return ans
        