'''
An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has a size of at least two.

Example 1:

Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
Example 2:

Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: An example of a minimum sized set is {1, 2, 3, 4, 5}.
 

Constraints:

1 <= intervals.length <= 3000
intervals[i].length == 2
0 <= ai < bi <= 10^8
'''


from typing import List


class Solution:
  def intersectionSizeTwo(self, itvls: List[List[int]]) -> int:
    itvls.sort(key=lambda x: (x[1], x[0]))
    # print('init', itvls)
    nums = []
    
    for x, y in itvls:
      if len(nums) < 2 or nums[-1] < x:
        nums.append(y-1)
        nums.append(y)
        # print('appended 0:', y-1, y)
        continue
        
      if nums[-2] < x:
        # print('appended 1:', y)
        if nums[-1] == y:
          nums[-1] = y-1
          
        nums.append(y)

    # print(nums)
    return len(nums)
    