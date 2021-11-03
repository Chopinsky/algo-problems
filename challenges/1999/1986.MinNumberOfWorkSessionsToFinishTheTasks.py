from typing import List
from functools import lru_cache
import math


class Solution:
  def minSessions(self, tasks: List[int], session: int) -> int:
    total = sum(tasks)
    n = len(tasks)
    slots = None
        
    min_count = sum(tasks) // session
    if total % session:
        min_count += 1
        
    def assign(idx: int, k: int):
      # end of assignments, check if it's valid
      if idx == n:
        for i in range(k):
          if not slots[i] or slots[i] > session:
            return False
          
        return True
      
      checked = set()
      for i in range(k):
        if slots[i]+tasks[idx] > session:
          continue
          
        if slots[i] in checked:
          continue
          
        slots[i] += tasks[idx]
        
        if assign(slots, idx+1, k):
          return True
        
        slots[i] -= tasks[idx]
        checked.add(slots[i])
      
      return False
    
    tasks.sort(reverse=True)
    for i in range(min_count, n):
      slots = [0] * i
      if assign(slots, 0, i):
        return i
      
    return n
    
        
  def minSessions0(self, tasks: List[int], session: int) -> int:
    if sum(tasks) <= session:
      return 1
    
    base_count = 0
    tasks.sort()
    
    while tasks and tasks[-1] == session:
      base_count += 1
      tasks.pop()
      
    if not tasks:
      return base_count
    
    n = len(tasks)
    tasks.reverse()
    # print(tasks, base_count)
    
    @lru_cache(None)
    def dp(taken: int, rem: int) -> int:
      if taken == ((1<<n) - 1):
        # print('end:', format(taken, '#014b'), rem)
        return 0
      
      best = math.inf
      
      for i in range(n):
        if 1<<i & taken > 0:
          continue
        
        if rem >= tasks[i]:
          nxt = dp(taken | 1<<i, rem-tasks[i])
        else:
          nxt = 1 + dp(taken | 1<<i, session-tasks[i])
          
        best = min(best, nxt)
        
      return best
    
    return base_count + 1 + dp(0, session)
  