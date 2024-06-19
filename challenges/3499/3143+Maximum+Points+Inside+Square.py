'''
3143. Maximum Points Inside the Square

You are given a 2D array points and a string s where, points[i] represents the coordinates of point i, and s[i] represents the tag of point i.

A valid square is a square centered at the origin (0, 0), has edges parallel to the axes, and does not contain two points with the same tag.

Return the maximum number of points contained in a valid square.

Note:

A point is considered to be inside the square if it lies on or within the square's boundaries.
The side length of the square can be zero.
 

Example 1:



Input: points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"

Output: 2

Explanation:

The square of side length 4 covers two points points[0] and points[1].

Example 2:

Input: points = [[1,1],[-2,-2],[-2,2]], s = "abb"

Output: 1

Explanation:

The square of side length 2 covers one point, which is points[0].

Example 3:

Input: points = [[1,1],[-1,-1],[2,-2]], s = "ccd"

Output: 0

Explanation:

It's impossible to make any valid squares centered at the origin such that it covers only one point among points[0] and points[1].

Constraints:

1 <= s.length, points.length <= 10^5
points[i].length == 2
-10^9 <= points[i][0], points[i][1] <= 10^9
s.length == points.length
points consists of distinct coordinates.
s consists only of lowercase English letters.
'''

from typing import List

class Solution:
  def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
    n = len(s)
    cand = sorted({0} | set(max(abs(x), abs(y)) for x, y in points))
    # print('coord:', cand)
    
    def check(ln: int) -> int:
      mask = 0
      count = 0
      
      for i in range(n):
        x, y = points[i]
        inside = max(abs(x), abs(y)) <= ln
        if not inside:
          continue
          
        key = 1 << (ord(s[i]) - ord('a'))
        if key & mask > 0:
          return -1
        
        mask |= key
        count += 1
      
      return count
    
    l, r = 0, len(cand)-1
    most = 0
    
    while l <= r:
      mid = (l+r) // 2
      ln = cand[mid]
      count = check(ln)
      
      if count >= 0:
        most = max(most, count)
        l = mid+1
      else:
        r = mid-1
    
    return most
        