'''
2553. Maximum Number of Integers to Choose From a Range I

You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

The chosen integers have to be in the range [1, n].
Each integer can be chosen at most once.
The chosen integers should not be in the array banned.
The sum of the chosen integers should not exceed maxSum.
Return the maximum number of integers you can choose following the mentioned rules.

Example 1:

Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation: You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.
Example 2:

Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation: You cannot choose any integer while following the mentioned conditions.
Example 3:

Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.

Constraints:

1 <= banned.length <= 1^4
1 <= banned[i], n <= 10^4
1 <= maxSum <= 10^9
'''

from typing import List
from bisect import bisect_right


class Solution:
  def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
    banned = sorted(set(banned))
    prefix = [val for val in banned]
    for i in range(1, len(prefix)):
      prefix[i] += prefix[i-1]
      
    def check(cnt: int):
      if cnt == 0:
        return True, 0
      
      total = ((1+cnt)*cnt)//2
      idx = bisect_right(banned, cnt)-1
      if idx >= 0:
        cnt -= idx+1
        total -= prefix[idx]
        
      # print('check:', cnt, idx, total)
      return total <= maxSum, cnt
      
    l, r = 0, n
    last = 0
    # print('init:', banned, prefix)
    
    while l <= r:
      mid = (l+r)//2
      res, cnt = check(mid)
      
      if res:
        last = cnt
        l = mid+1
      else:
        r = mid-1
    
    return last
        
  def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
    banned = set(banned)
    running_sum = 0
    count = 0
    
    for val in range(1, n+1):
      if running_sum+val > maxSum:
        break
        
      if val in banned:
        continue
        
      running_sum += val 
      count += 1
      
    return count
    