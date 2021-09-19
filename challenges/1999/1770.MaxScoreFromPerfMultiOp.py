from typing import List
import math

class Solution:
  '''
  idea is to define state: dp[i][j] = max score if we have used left `i` elements
  and right `j` elements already, answer is max(dp[i][m-i]) for 0 <= i <= m
  '''
  def maxScore(self, nums: List[int], multi: List[int]) -> int:
    m, n = len(multi), len(nums)
    dp = [[0] * (m+1) for _ in range(m+1)]
    ans = -math.inf

    for i in range(0, m+1):
      for j in range(0, m-i+1):
        if i == 0 and j == 0:
          continue

        if i == 0:
          dp[0][j] = dp[0][j-1] + nums[n-j] * multi[j-1]
          continue

        if j == 0:
          dp[i][j] = dp[i-1][0] + nums[i-1] * multi[i-1]
          continue

        dp[i][j] = max(
          dp[i-1][j] + nums[i-1] * multi[i+j-1],
          dp[i][j-1] + nums[n-j] * multi[i+j-1]
        )

        if i+j == m:
          ans = max(ans, dp[i][j])

    # print(dp)

    return ans

s = Solution()
t = [
  [[1,2,3],[3,2,1],14],
  [[-5,-3,-3,-2,7,1],[-10,-5,3,4,6],102]
]

for [n, m, a] in t:
  ans = s.maxScore(n, m)
  print("=========")
  print("Test case:", n, m)
  print("Expected:", a)
  print("Found:", ans)
  print("")
