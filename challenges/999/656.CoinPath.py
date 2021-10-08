'''
Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.

Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to the place indexed N using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed N then you need to return an empty array.

Example 1:

Input: [1,2,4,-1,2], 2
Output: [1,3,5]
Example 2:

Input: [1,2,4,-1,2], 1
Output: []
Note:

Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
Length of A is in the range of [1, 1000].
B is in the range of [1, 100].
'''


from typing import List
import math


class Solution():
  def coin_path(self, coins: List[int], k: int) -> List[int]:
    n = len(coins)
    dp = [[math.inf, -1, math.inf] if i else [coins[0], -1, 0] for i in range(n)]

    for i in range(1, n):
      for j in range(i-1, max(0, i-k)-1, -1):
        if coins[j] < 0:
          continue

        if dp[i][0] > dp[j][0] or (dp[i][0] == dp[j][0] and dp[i][2] > dp[j][2]):
          dp[i][0] = dp[j][0]
          dp[i][1] = j
          dp[i][2] = dp[j][2]

      dp[i][0] += coins[i]
      dp[i][2] += 1

    # print(dp)
    i = n-1
    ans = []

    if dp[i][1] == -1:
      return ans

    while i >= 0:
      ans.append(i+1)
      i = dp[i][1]

    ans.reverse()

    return ans


s = Solution()
t = [
  [[1,2,4,-1,2], 2, [1,3,5]],
  [[1,2,4,-1,2], 1, []],
]

for coins, jump, res in t:
  ans = s.coin_path(coins, jump)
  print('\n============')
  print('Test case:', coins, jump)
  print("Expected:", res)
  print("Got:     ", ans)
