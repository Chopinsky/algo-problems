'''
You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

Example 1:

Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)

Example 2:

Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)

Example 3:

Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)

Example 4:

Input: tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 2.
- Assign worker 1 to task 0 (6 >= 5)
- Assign worker 2 to task 2 (4 + 5 >= 8)
- Assign worker 4 to task 3 (6 >= 5)

Constraints:

n == tasks.length
m == workers.length
1 <= n, m <= 5 * 10^4
0 <= pills <= m
0 <= tasks[i], workers[j], strength <= 10^9
'''


from typing import List
from collections import deque
from bisect import bisect_right
import math


class Solution:
  def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
    tasks.sort()
    workers.sort()
    m, n = len(tasks), len(workers)
    
    def match(k: int) -> bool:
      if k > n:
        return False
      
      ww = workers[n-k:]
      tt = tasks[:k]
      # print('size', len(ww), len(tt))
      
      if sum(tt) > sum(ww) + pills*strength:
        return False
      
      i, j = 0, 0
      rem = pills
      pilled = deque([])
      first = math.inf
      
      while i < k: #or pilled:
        # print(i, j, len(pilled), first)
        
        if not pilled:
          if tt[i] <= ww[j]:
            i += 1
            j += 1
            continue
            
          if not rem:
            # print('fail-0')
            return False
          
          # worker[j] takes the pill
          nxt_stre = ww[j] + strength
          pilled.append(nxt_stre)
          
          # this worker must take the `first` job or earlier
          first = bisect_right(tt, nxt_stre) - 1
          j += 1

          continue
          
        # a worker is going to be wasted, not going to finish
        if (pilled[0] < tt[i]) or (j < k and ww[j]+strength < tt[i]) or (not rem):
          # print('fail-1', i, j, rem, tt[i], ww[j], pilled[0], first)
          return False
        
        # must assign the pilled worker to this task, otherwise some pilled worker
        # won't be able to take the job
        if first == i:
          pilled.popleft()
          first += 1
          i += 1
          continue
          
        # the pilled worker needs to go first
        if ww[j] >= pilled[0]:
          pilled.popleft()
          i += 1
          continue
          
        # if the worker[j] can still take the task, do it w/o the pill
        if tt[i] <= ww[j]:
          i += 1
          j += 1
          continue
          
        # no more pill to take
        if not rem:
          return False
          
        # the worker needs to take the pill and put into the queue
        nxt_stre = ww[j] + strength
        pilled.append(nxt_stre)
        idx = bisect_right(tt, nxt_stre) - 1
        first = min(first, idx+1-len(pilled))
        
        # take the pill and move on
        rem -= 1
        j += 1
        
        if first < i:
          # print('fail-2')
          return False
          
      # print('end', j, pilled)
      return j == k and not pilled
      
    l, r = 1, min(m, n)
    most = 0

    while l < r:
      mid = (l+r) // 2
      # print('mid', l, mid, r, match(mid))
      
      if match(mid):
        most = max(most, mid)
        l = mid + 1
      else:
        r = mid - 1
      
    # print('out', l, match(l))
    if match(l):
      most = max(most, l)

    return most
        