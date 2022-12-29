'''
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.

Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.

Constraints:

tasks.length == n
1 <= n <= 10^5
1 <= enqueueTimei, processingTimei <= 10^9
'''


from typing import List
from heapq import heappop, heappush


class Solution:
  def getOrder(self, tasks: List[List[int]]) -> List[int]:
    tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])  
    # print(tasks)
    
    ans, q = [], []
    time = -1
    idx, n = 0, len(tasks)
    
    while q or idx < n:
      # enqueue
      while idx < n and tasks[idx][0] <= time:
        _, pt, jdx = tasks[idx]
        heappush(q, (pt, jdx))
        idx += 1
        
      # no more tasks to process, pull the first one out
      # of the remainder tasks and process it
      if not q:
        time = tasks[idx][0]+tasks[idx][1]
        ans.append(tasks[idx][2])
        idx += 1
        continue
        
      # pull one out of the queue and process it
      pt, jdx = heappop(q)
      ans.append(jdx)
      time += pt
        
    return ans
    
    
  def getOrder(self, tasks: List[List[int]]) -> List[int]:
    src = sorted((s, p, i) for i, (s, p) in enumerate(tasks))
    idx = 1
    ans = []
    stack = [(src[0][1], src[0][2])]
    clock = src[0][0]
    # print(src)
    
    while stack:
      time, i = heappop(stack)
      clock += time
      ans.append(i)
      
      # if CPU goes idle after finishing i-th task
      if not stack and idx < len(src) and clock < src[idx][0]:
        clock = src[idx][0]
      
      while idx < len(src) and src[idx][0] <= clock:
        heappush(stack, (src[idx][1], src[idx][2]))
        idx += 1
        
    return ans
    