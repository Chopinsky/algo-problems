'''
You are given an integer hoursBefore, the number of hours you have to travel to your meeting. To arrive at your meeting, you have to travel through n roads. The road lengths are given as an integer array dist of length n, where dist[i] describes the length of the ith road in kilometers. In addition, you are given an integer speed, which is the speed (in km/h) you will travel at.

After you travel road i, you must rest and wait for the next integer hour before you can begin traveling on the next road. Note that you do not have to rest after traveling the last road because you are already at the meeting.

For example, if traveling a road takes 1.4 hours, you must wait until the 2 hour mark before traveling the next road. If traveling a road takes exactly 2 hours, you do not need to wait.
However, you are allowed to skip some rests to be able to arrive on time, meaning you do not need to wait for the next integer hour. Note that this means you may finish traveling future roads at different hour marks.

For example, suppose traveling the first road takes 1.4 hours and traveling the second road takes 0.6 hours. Skipping the rest after the first road will mean you finish traveling the second road right at the 2 hour mark, letting you start traveling the third road immediately.
Return the minimum number of skips required to arrive at the meeting on time, or -1 if it is impossible.

 

Example 1:

Input: dist = [1,3,2], speed = 4, hoursBefore = 2
Output: 1
Explanation:
Without skipping any rests, you will arrive in (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 hours.
You can skip the first rest to arrive in ((1/4 + 0) + (3/4 + 0)) + (2/4) = 1.5 hours.
Note that the second rest is shortened because you finish traveling the second road at an integer hour due to skipping the first rest.
Example 2:

Input: dist = [7,3,5,5], speed = 2, hoursBefore = 10
Output: 2
Explanation:
Without skipping any rests, you will arrive in (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 hours.
You can skip the first and third rest to arrive in ((7/2 + 0) + (3/2 + 0)) + ((5/2 + 0) + (5/2)) = 10 hours.
Example 3:

Input: dist = [7,3,5,5], speed = 1, hoursBefore = 10
Output: -1
Explanation: It is impossible to arrive at the meeting on time even if you skip all the rests.
 

Constraints:

n == dist.length
1 <= n <= 1000
1 <= dist[i] <= 10^5
1 <= speed <= 10^6
1 <= hoursBefore <= 10^7
'''


from typing import List, Dict
from math import inf, ceil


class Solution:
  def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
    if sum(dist) / speed > hoursBefore:
      return -1
    
    n = len(dist)
    limit = speed * hoursBefore
    skips, nxt = {0:0}, {}
    # print('len:', len(dist))
    
    def add_time(src: Dict[int, int], skip: int, d: int):
      if d > limit:
        return
      
      src[skip] = min(src.get(skip, inf), d)
    
    for i, d0 in enumerate(dist):
      if not skips:
        return -1
        
      for s, d1 in skips.items():
        if d1 % speed == 0:
          add_time(nxt, s, d1+d0)
          
        else:
          add_time(nxt, s+1, d1+d0)
          add_time(nxt, s, speed*ceil(d1/speed) + d0)
          
      skips, nxt = nxt, skips
      nxt.clear()
    
    return min(skips)
  