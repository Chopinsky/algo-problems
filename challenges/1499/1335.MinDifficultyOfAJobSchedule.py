'''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
'''


from typing import List
from functools import lru_cache
import math


class Solution:
  def minDifficulty(self, job: List[int], d: int) -> int:
    n = len(job)
    
    @lru_cache(None)
    def dp(i: int, rem: int):
      if n-i < rem or rem <= 0:
        return math.inf
      
      if n-i == rem:
        return sum(job[i:])

      if rem == 1:
        return max(job[i:])
      
      curr = 0
      cost = math.inf
      
      for j in range(i, n):
        curr = max(curr, job[j])
        rest = dp(j+1, rem-1)
        if rest == math.inf:
          break
          
        cost = min(cost, curr+rest)
        
      return cost
      
    cost = dp(0, d)
    
    return cost if cost != math.inf else -1  
      
      
  def minDifficulty(self, dif: List[int], d: int) -> int:
    n = len(dif)
    
    @lru_cache(None)
    def dp(i: int, d: int) -> int:
      if i < 0 and d == 0:
        return 0
      
      if i < 0 or d <= 0 or d > i+1:
        return -1
      
      if d == i+1:
        return sum(dif[:i+1])
      
      min_dif = math.inf
      curr_dif = -1
      
      for j in range(i, -1, -1):
        # more days then remaining jobs
        if d-1 > j:
          break
          
        # assuming we take job [j, i] on this day
        curr_dif = max(curr_dif, dif[j])
        nxt_dif = dp(j-1, d-1)
        
        if nxt_dif >= 0:
          min_dif = min(min_dif, curr_dif+nxt_dif)
      
      return -1 if min_dif == math.inf else min_dif
      
    return dp(n-1, d)

    
  def minDifficulty(self, jobs: List[int], d: int) -> int:
    n = len(jobs)
    prefix = [d for d in jobs]
    max_val = [d for d in jobs]

    for i in range(n-2, -1, -1):
      prefix[i] += prefix[i+1]
      max_val[i] = max(max_val[i], max_val[i+1])
    
    @lru_cache(None)
    def check(i: int, d: int) -> int:
      if i >= n and d >= 0:
        return -1 if d > 0 else 0
      
      # all jobs done in 1 day
      if d == 1:
        return max_val[i]
      
      # 1 job for each of the remaining days
      if n-i == d:
        return prefix[i]
      
      curr = 0
      total = math.inf
      
      for j in range(i, n-d+1):
        nxt = check(j+1, d-1)
        if nxt < 0:
          break
          
        curr = max(curr, jobs[j])
        total = min(total, curr+nxt)
        
      return total if total < math.inf else -1
      
    return check(0, d)
  