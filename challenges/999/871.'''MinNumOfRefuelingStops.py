'''
A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).

Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: 
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

Note:

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
'''

from heapq import heappush, heappop
from bisect import bisect_left
from typing import List

class Solution:
  def minRefuelStops(self, target: int, fuel: int, stations: List[List[int]]) -> int:
    pq = []
    count, i = 0, 0
    
    while fuel < target:
      # we can reach stations #-i with the max fuel, add the possible refuel 
      # opportunity to the queue, and make sure the most fuel-able station is
      # at the top of the queue -- we will fuel there
      while i < len(stations) and stations[i][0] <= fuel:
        heappush(pq, -stations[i][1])
        i += 1
        
      # we can no longer reach any further stations with all the fueling opportunities
      if not pq:
        return -1
      
      # we only fuel at the station with the most gas -- this is a lookback action,
      # we assume we are at stations[i] which can be reached with the previous tank.
      #
      # Now we must refuel or we can't go further, we choose to refuel at a previous
      # station with the most gas available to us, and we refuel there. Now we have 
      # more gas in the tank than previous tank, we can continue the next iteration. Since
      # we fueled in that station, we add 1 to the total count
      fuel += -heappop(pq)
      count += 1
      
    # we've reached the target, done
    return count
    
  def minRefuelStops1(self, t: int, s: int, stations: List[List[int]]) -> int:
    if s >= t:
      return 0
    
    n = len(stations)
    refuels = [0] * (n+1)
    
    for i in range(n+1):
      if i == 0:
        refuels[0] = s
        continue
        
      dist = (stations[i-1][0]-stations[i-2][0]) if i > 1 else stations[i-1][0]
      
      for j in range(i):
        # minus spent fuels
        refuels[j] -= dist
          
        # can't reach station #-i
        if j == i-1 and refuels[j] < 0:
          return -1
        
      for j in range(i, 0, -1):
        # find optimal fuel levels
        if refuels[j-1] >= 0 and refuels[j] >= 0:
          refuels[j] = max(refuels[j], refuels[j-1]+stations[i-1][1])
            
      # print(i, dist, refuels)

    # print(refuels)
    
    last = t-stations[-1][0] if n > 0 else t
    if refuels[0] >= last:
      return 0
    
    if refuels[-1] < last:
      return -1
    
    return bisect_left(refuels, last)
  