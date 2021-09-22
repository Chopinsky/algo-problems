'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
'''

class Solution:
  def eraseOverlapIntervals(self, itvls: List[List[int]]) -> int:
    itvls.sort(key=lambda x: x[1])
    count = 0
    prev = itvls[0][1]
    
    for i in range(1, len(itvls)):
      if itvls[i][0] < prev:
        count += 1
        
      else:
        prev = itvls[i][1]
    
    return count
  
    
  def eraseOverlapIntervals0(self, itvls: List[List[int]]) -> int:
    itvls.sort(key=lambda x: (x[1], x[0]))
    endings = [e for _, e in itvls]
    # print(itvls, endings)
    
    n = len(itvls)
    dp = [0] * n
    
    for i, [s, e] in enumerate(itvls):
      if i == 0 or s >= itvls[i-1][1]:
        dp[i] = dp[i-1] if i > 0 else 0
        continue

      j = bisect_right(endings, s) - 1
      if j < 0:
        # delete self or all before self
        dp[i] = min(dp[i-1] + 1, i)
      else:
        dp[i] = min(dp[i-1] + 1, dp[j] + i - j - 1)
    
    return dp[-1]
  
