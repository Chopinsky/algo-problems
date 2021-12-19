'''
You have the task of delivering some boxes from storage to their ports using only one ship. However, this ship has a limit on the number of boxes and the total weight that it can carry.

You are given an array boxes, where boxes[i] = [ports​​i​, weighti], and three integers portsCount, maxBoxes, and maxWeight.

ports​​i is the port where you need to deliver the ith box and weightsi is the weight of the ith box.
portsCount is the number of ports.
maxBoxes and maxWeight are the respective box and weight limits of the ship.
The boxes need to be delivered in the order they are given. The ship will follow these steps:

The ship will take some number of boxes from the boxes queue, not violating the maxBoxes and maxWeight constraints.
For each loaded box in order, the ship will make a trip to the port the box needs to be delivered to and deliver it. If the ship is already at the correct port, no trip is needed, and the box can immediately be delivered.
The ship then makes a return trip to storage to take more boxes from the queue.
The ship must end at storage after all the boxes have been delivered.

Return the minimum number of trips the ship needs to make to deliver all boxes to their respective ports.

 

Example 1:

Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
Output: 4
Explanation: The optimal strategy is as follows: 
- The ship takes all the boxes in the queue, goes to port 1, then port 2, then port 1 again, then returns to storage. 4 trips.
So the total number of trips is 4.
Note that the first and third boxes cannot be delivered together because the boxes need to be delivered in order (i.e. the second box needs to be delivered at port 2 before the third box).
Example 2:

Input: boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
Output: 6
Explanation: The optimal strategy is as follows: 
- The ship takes the first box, goes to port 1, then returns to storage. 2 trips.
- The ship takes the second, third and fourth boxes, goes to port 3, then returns to storage. 2 trips.
- The ship takes the fifth box, goes to port 3, then returns to storage. 2 trips.
So the total number of trips is 2 + 2 + 2 = 6.
Example 3:

Input: boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7
Output: 6
Explanation: The optimal strategy is as follows:
- The ship takes the first and second boxes, goes to port 1, then returns to storage. 2 trips.
- The ship takes the third and fourth boxes, goes to port 2, then returns to storage. 2 trips.
- The ship takes the fifth and sixth boxes, goes to port 3, then returns to storage. 2 trips.
So the total number of trips is 2 + 2 + 2 = 6.
Example 4:

Input: boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7
Output: 14
Explanation: The optimal strategy is as follows:
- The ship takes the first box, goes to port 2, then storage. 2 trips.
- The ship takes the second box, goes to port 2, then storage. 2 trips.
- The ship takes the third and fourth boxes, goes to port 3, then storage. 2 trips.
- The ship takes the fifth box, goes to port 3, then storage. 2 trips.
- The ship takes the sixth and seventh boxes, goes to port 3, then port 4, then storage. 3 trips. 
- The ship takes the eighth and ninth boxes, goes to port 1, then port 5, then storage. 3 trips.
So the total number of trips is 2 + 2 + 2 + 2 + 3 + 3 = 14.

Constraints:

1 <= boxes.length <= 10^5
1 <= portsCount, maxBoxes, maxWeight <= 10^5
1 <= ports​​i <= portsCount
1 <= weightsi <= maxWeight
'''

from typing import List
from bisect import bisect_right


class Solution:
  def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
    n = len(boxes)
    start_from, port_count = 0, 0
    cur_w, cur_b = 0, 0
    dp = [0] * (n+1)

    for i in range(n):
      # add box-i to the ship
      cur_w += boxes[i][1]
      cur_b += 1
      
      # count the number of the ports to make 
      # the trips to
      if i == 0 or boxes[i][0] != boxes[i-1][0]:
        port_count += 1
        
      # find the first box that can fit into the ship and
      # also requires less trips: since dp is monotonically increasing,
      # we will try to minimize `port_count` while avoiding increasing
      # `start_from`, which will add more trips because of `dp[start_from]`
      while (cur_b > maxBoxes) or (cur_w > maxWeight) or (start_from < i and dp[start_from] == dp[start_from+1]):
        # pop the box-<start_from> out of the ship
        cur_b -= 1
        cur_w -= boxes[start_from][1]
        
        # evict a port from the trips since we're not going
        # to that port anymore
        if boxes[start_from][0] != boxes[start_from+1][0]:
          port_count -= 1
          
        # now we start with box-<start_from+1> till box-i
        # for this round trip
        start_from += 1
        
      # dp is monotonic increasing array, 1 is added for the return trip
      dp[i+1] = dp[start_from] + port_count + 1
        
    return dp[n] 
  
  
  def boxDelivering0(self, boxes: List[List[int]], pc: int, mb: int, mw: int) -> int:
    n = len(boxes)
    if n == 1:
      return 2
    
    wt = [box[1] for box in boxes]
    cnt = [1 for _ in range(n)]
    trips = [0 for _ in range(n)]
    dp = [0 if i < n-1 else 2 for i in range(n)]
    
    for i in range(1, n):
      wt[i] += wt[i-1]
      trips[i] = trips[i-1]
      
      if boxes[i][0] == boxes[i-1][0]:
        cnt[i] += cnt[i-1]
      else:
        trips[i] += 1
      
    # print(wt, cnt, trips)
    idx = n-1
    for i in range(n-2, -1, -1):
      w = boxes[i][1]
      
      # has to make a round trip for this box alone
      if mb == 1 or mw == w:
        dp[i] = 2 + dp[i+1]
        continue
        
      # get the right boundary of the segment
      j = bisect_right(wt, wt[i]-w+mw) - 1
      if j <= i:
        dp[i] = 2 + dp[i+1]
        continue
        
      # get the real boundary definied by the ship limits
      idx = min(j, i+mb-1)
      base = dp[i+1]
      
      # try different combos
      while idx > i:
        t = trips[idx] - trips[i] + (dp[idx+1] if idx < n-1 else 0)
        if t > base:
          break
          
        base = t
        # guaranteed correct: idx -= 1, below is believed to be correct
        # and slightly faster
        idx -= cnt[idx]
        
      dp[i] = 2 + base
      
    # print('fin:', dp)
    return dp[0]
  