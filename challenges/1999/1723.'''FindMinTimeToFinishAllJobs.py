'''
You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.

Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.

Constraints:

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 10^7
'''


import math
from typing import List
from functools import lru_cache


class Solution:
  def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
    hours = 0
    n = len(jobs)
    worker_hours = [0] * k
    jobs.sort(reverse=True)

    # calculate the upper limit of the hours to work on
    for i in range(0, n, k):
      hours += jobs[i]

    '''
    assign i-th job to the k workers and check if we have a better
    solution, key is to skip users with the current hours already checked,
    because all workers are deemed the same, hence the same worker hours
    means we've checked this combo already
    '''
    def dp(i: int, top: int):
      nonlocal hours

      # we won't 
      if top >= hours:
        return

      if i >= n:
        hours = min(hours, max(worker_hours))
        return

      checked = set()

      # iterate over k-workers and see who has better capacity
      # to take on this job
      for j in range(k):
        # this amount of hour is checked, which will not 
        # yield a better solution since all workers are
        # the same
        if worker_hours[j] in checked:
          continue

        checked.add(worker_hours[j])
        worker_hours[j] += jobs[i]

        # check the next job
        dp(i+1, max(top, worker_hours[j]))
        worker_hours[j] -= jobs[i]

    dp(0, 0)

    return hours


  def minimumTimeRequired0(self, jobs: List[int], k: int) -> int:
    n = len(jobs)
    if n == k:
      return max(jobs)
    
    cap = sum(jobs) / k
    job_hours = {}

    for mask in range(1, 1<<n):
      hours = 0
      red_flag = 0
      
      for i in range(n):
        if 1<<i & mask > 0:
          if red_flag == 1:
            red_flag = 2
            break
            
          hours += jobs[i]
          if hours >= cap:
            red_flag += 1
          
      if red_flag < 2:
        job_hours[mask] = hours
    
    @lru_cache(None)
    def dp(i: int, taken: int) -> int:
      if i == k-1:
        # last worker, has to take all remaining jobs
        hours = 0
        for j in range(n):
          if 1<<j & taken == 0:
            hours += jobs[j]
          
        # print('last worker:', hours, format(taken, '#012b'))
        return hours
      
      hours = math.inf
      for job in job_hours:
        if job & taken == 0:
          curr = max(job_hours[job], dp(i+1, taken | job))
          hours = min(curr, hours)
          
      return hours
    
    return dp(0, 0)
  