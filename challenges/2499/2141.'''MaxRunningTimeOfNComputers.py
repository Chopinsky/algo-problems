'''
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.


Example 1:

Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation: 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

Example 2:

Input: n = 2, batteries = [1,1,1,1]
Output: 2
Explanation: 
Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer. 
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.

Constraints:

1 <= n <= batteries.length <= 10^5
1 <= batteries[i] <= 10^9
'''


from typing import List
from heapq import heapify, heappop, heappushpop


class Solution:
  def maxRunTime(self, n: int, b: List[int]) -> int:
    if n == len(b):
      return min(b)
    
    b.sort()
    total = sum(b)
    
    # if the richest batter is going to waste some energy,
    # take it out since it's going to power the n-th computer
    # all the time
    while b[-1] > total/n:
      n -= 1
      total -= b.pop()
      
    # calculate the average time the remainder set of the batter
    # can support the computers
    return total / n
     
    
  def maxRunTime0(self, n: int, b: List[int]) -> int:
    m = len(b)
    if m == n:
      return min(b)
    
    b.sort()
    total = sum(b)
    
    def check(k: int) -> bool:
      if k == b[0]:
        return True
      
      if k*n > total:
        return False
      
      stack = [val-k for val in b[-n:]]
      heapify(stack)
      # print('pre check', k, stack)
      
      # can sustain k-runtime without refuel
      if stack[0] >= 0:
        return True
      
      for i in range(m-n-1, -1, -1):
        # nxt = b[i] + stack[0]
        # heappushpop(stack, nxt)
        val = b[i]
        while stack and val and val+stack[0] >= 0:
          val += heappop(stack)

        if val and stack:
          heappushpop(stack, stack[0]+val)
          
        if not stack or stack[0] >= 0:
          break
        
      # print(k, stack)
      return not stack or stack[0] >= 0
    
    l, r = b[0], (total//n)+1
    last = l
    
    while l < r:
      k = (l + r) // 2
      # print('check', k, check(k))
      
      if check(k):
        l = k + 1
        last = k
      else:
        r = k - 1
        
    # print('fin:', last)
    return l if check(l) else last
