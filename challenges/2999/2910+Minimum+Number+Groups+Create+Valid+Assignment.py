'''
2910. Minimum Number of Groups to Create a Valid Assignment

You are given a collection of numbered balls and instructed to sort them into boxes for a nearly balanced distribution. There are two rules you must follow:

Balls with the same box must have the same value. But, if you have more than one ball with the same number, you can put them in different boxes.
The biggest box can only have one more ball than the smallest box.
​Return the fewest number of boxes to sort these balls following these rules.

Example 1:

Input:  balls = [3,2,3,2,3] 

Output:  2 

Explanation:

We can sort balls into boxes as follows:

[3,3,3]
[2,2]
The size difference between the two boxes doesn't exceed one.

Example 2:

Input:  balls = [10,10,10,3,1,1] 

Output:  4 

Explanation:

We can sort balls into boxes as follows:

[10]
[10,10]
[3]
[1,1]
You can't use fewer than four boxes while still following the rules. For example, putting all three balls numbered 10 in one box would break the rule about the maximum size difference between boxes.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9

Test cases:

[3,2,3,2,3]
[10,10,10,3,1,1]
[1,1,3,3,1,1,2,2,3,1,3,2]
'''

from math import ceil
from collections import Counter
from typing import List

class Solution:
  def minGroupsForValidAssignment(self, nums: List[int]) -> int:
    c = Counter(nums)
    n = len(nums)
    
    if len(c) == n:
      return n
    
    def count(cnt: int):
      total = 0
      for c1 in c.values():
        # can't distribute evenly with +1 diff
        if c1%cnt > c1//cnt:
          return n
        
        total += ceil(c1 / (cnt+1))
        
      return total
    
    return min(count(c0+1) for c0 in range(min(c.values())))
  