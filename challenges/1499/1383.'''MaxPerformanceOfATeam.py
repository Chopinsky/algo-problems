'''
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 10 ** 9 + 7.

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation:
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72

Constraints:

1 <= <= k <= n <= 10 ** 5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10 ** 5
1 <= efficiency[i] <= 10 ** 8
'''

from typing import List
from heapq import heappush, heappop, heappushpop


class Solution:
  def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    mod = 10**9 + 7
    perf = sorted([(e, s) for s, e in zip(speed, efficiency)], reverse=True)
    res = 0
    speed_sum = 0
    q = []
    # print(perf)
    
    for e, s in perf:
      if len(q) < k:
        heappush(q, s)
        speed_sum += s
        res = max(res, speed_sum * e)
        continue
        
      if s <= q[0]:
        continue
        
      removed = heappushpop(q, s)
      # print(e, s, removed)
      
      speed_sum += (s - removed)
      res = max(res, speed_sum * e)
    
    return res % mod
    

  def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    if k == 1:
      return max([efficiency[i] * speed[i] for i in range(n)])

    src = [(efficiency[i], speed[i]) for i in range(n)]
    src.sort(reverse=True)

    s = []
    total = 0
    perf = 0

    for i in range(n):
      if len(s) < k:
        # build up the team ground up, this is because there are cases where less members
        # could lead to higher performance
        heappush(s, src[i][1])
        total += src[i][1]

        curr = (total * src[i][0])
        if curr > perf:
          perf = curr

      else:
        #build the team when it's full of the members (i.e. len(s) == k)
        small = s[0]

        # not going to improve the overall performance since efficiency
        # multiplier is equal or smaller, but overall speed added is
        # also smaller
        if src[i][1] <= small:
          continue

        # keep the best team with the biggest speed sum, later team can
        # use it to calc its best team performance
        heappop(s)
        heappush(s, src[i][1])
        total += src[i][1] - small

        # compare and update team performance up to this member
        curr = total * src[i][0]
        if curr > perf:
          perf = curr

    # print("final:", s)

    return perf % (10 ** 9 + 7)
