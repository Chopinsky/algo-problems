'''
2532. Time to Cross a Bridge

There are k workers who want to move n boxes from an old warehouse to a new one. You are given the two integers n and k, and a 2D integer array time of size k x 4 where time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi].

The warehouses are separated by a river and connected by a bridge. The old warehouse is on the right bank of the river, and the new warehouse is on the left bank of the river. Initially, all k workers are waiting on the left side of the bridge. To move the boxes, the ith worker (0-indexed) can :

Cross the bridge from the left bank (new warehouse) to the right bank (old warehouse) in leftToRighti minutes.
Pick a box from the old warehouse and return to the bridge in pickOldi minutes. Different workers can pick up their boxes simultaneously.
Cross the bridge from the right bank (old warehouse) to the left bank (new warehouse) in rightToLefti minutes.
Put the box in the new warehouse and return to the bridge in putNewi minutes. Different workers can put their boxes simultaneously.
A worker i is less efficient than a worker j if either condition is met:

leftToRighti + rightToLefti > leftToRightj + rightToLeftj
leftToRighti + rightToLefti == leftToRightj + rightToLeftj and i > j
The following rules regulate the movement of the workers through the bridge :

If a worker x reaches the bridge while another worker y is crossing the bridge, x waits at their side of the bridge.
If the bridge is free, the worker waiting on the right side of the bridge gets to cross the bridge. If more than one worker is waiting on the right side, the one with the lowest efficiency crosses first.
If the bridge is free and no worker is waiting on the right side, and at least one box remains at the old warehouse, the worker on the left side of the river gets to cross the bridge. If more than one worker is waiting on the left side, the one with the lowest efficiency crosses first.
Return the instance of time at which the last worker reaches the left bank of the river after all n boxes have been put in the new warehouse.

Example 1:

Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
Output: 6
Explanation: 
From 0 to 1: worker 2 crosses the bridge from the left bank to the right bank.
From 1 to 2: worker 2 picks up a box from the old warehouse.
From 2 to 6: worker 2 crosses the bridge from the right bank to the left bank.
From 6 to 7: worker 2 puts a box at the new warehouse.
The whole process ends after 7 minutes. We return 6 because the problem asks for the instance of time at which the last worker reaches the left bank.
Example 2:

Input: n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
Output: 50
Explanation: 
From 0  to 10: worker 1 crosses the bridge from the left bank to the right bank.
From 10 to 20: worker 1 picks up a box from the old warehouse.
From 10 to 11: worker 0 crosses the bridge from the left bank to the right bank.
From 11 to 20: worker 0 picks up a box from the old warehouse.
From 20 to 30: worker 1 crosses the bridge from the right bank to the left bank.
From 30 to 40: worker 1 puts a box at the new warehouse.
From 30 to 31: worker 0 crosses the bridge from the right bank to the left bank.
From 31 to 39: worker 0 puts a box at the new warehouse.
From 39 to 40: worker 0 crosses the bridge from the left bank to the right bank.
From 40 to 49: worker 0 picks up a box from the old warehouse.
From 49 to 50: worker 0 crosses the bridge from the right bank to the left bank.
From 50 to 58: worker 0 puts a box at the new warehouse.
The whole process ends after 58 minutes. We return 50 because the problem asks for the instance of time at which the last worker reaches the left bank.

Constraints:

1 <= n, k <= 10^4
time.length == k
time[i].length == 4
1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000
'''

from typing import List
from heapq import heappush, heappop
import math


class Solution:
  def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
    curr = 0
    left, right = [], []
    left_ready, right_ready = [], []
    
    for i in range(k):
      heappush(left_ready, (0, -i))
    
    # print('pre:', left_ready)
    
    while n > 0:
      # left side workers ready to cross @ curr
      while left_ready and left_ready[0][0] <= curr:
        # print('unload left:', left_ready)
        _, ni = heappop(left_ready)
        heappush(left, (-time[-ni][0]-time[-ni][2], ni))
        
      # right side workers ready to cross @ curr
      while right_ready and right_ready[0][0] <= curr:
        # print('unload right:', right_ready)
        _, ni = heappop(right_ready)
        heappush(right, (-time[-ni][0]-time[-ni][2], ni))
        
      # print('status:', curr, left, right)
      
      # right worker cross first
      if right:
        _, ni = heappop(right)
        idx = -ni
        # print('right cross:', (curr, curr+time[idx][2]), idx)
        
        # cross to the left and carry the box
        curr += time[idx][2]
        n -= 1
        
        # put into the left_ready queue
        heappush(left_ready, (curr+time[idx][3], -idx))
        continue
        
      # left worker need to cross now
      if left and len(right)+len(right_ready) < n:
        _, ni = heappop(left)
        idx = -ni
        
        # the worker will be in queue after picking
        # an box
        curr += time[idx][0]
        
        # the worker will be ready at a later time
        heappush(right_ready, (curr+time[idx][1], -idx))
        continue
        
      # if none of the workers are ready, fast-forward to the earliest moment
      # one of them are ready to cross
      left_time = left_ready[0][0] if left_ready else math.inf
      right_time = right_ready[0][0] if right_ready else math.inf
      curr = min(left_time, right_time)
        
    return curr
    