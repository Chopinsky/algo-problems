'''
You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:

The ith (0-indexed) request arrives.
If all servers are busy, the request is dropped (not handled at all).
If the (i % k)th server is available, assign the request to that server.
Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.
You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

Example 1:

Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
Output: [1] 
Explanation: 
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
Example 2:

Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
Output: [0]
Explanation: 
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.
Example 3:

Input: k = 3, arrival = [1,2,3], load = [10,12,11]
Output: [0,1,2]
Explanation: Each server handles a single request, so they are all considered the busiest.
 
Constraints:

1 <= k <= 10^5
1 <= arrival.length, load.length <= 10^5
arrival.length == load.length
1 <= arrival[i], load[i] <= 10^9
arrival is strictly increasing.
'''


from typing import List
from heapq import heappush, heappop
from bisect import bisect_left, insort


class Solution:
  def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
    counter = [0] * k
    busy, before, after = [], [], []
    
    for i in range(k):
      heappush(after, i)
      
    # print('init', after)
   
    for i, t in enumerate(arrival):
      curr = i % k
      while busy and busy[0][0] <= t:
        _, idx = heappop(busy)
        if idx < curr:
          heappush(before, idx)
        else:
          heappush(after, idx)

      # print('curr', i, t, before, after)
      if not before and not after:
        continue
        
      if not after:
        idx = heappop(before)
      else:
        idx = heappop(after)
        
      counter[idx] += 1
      heappush(busy, (t+load[i], idx))
      nxt = (i+1) % k
      
      if nxt == 0:
        while before:
          heappush(after, heappop(before))
      else:
        while after and after[0] < nxt:
          heappush(before, heappop(after))
      
    ans = []
    # print(counter)
    
    for i, cnt in enumerate(counter):
      if not ans or cnt == counter[ans[0]]:
        ans.append(i)
        continue
        
      if cnt > counter[ans[0]]:
        ans.clear()
        ans.append(i)
        
    return ans
  
  
  def busiestServers0(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
    counter = [0] * k
    busy = []
    ready_list = [i for i in range(k)]
    # ready = set(ready_list)
    
    for i, t in enumerate(arrival):
      while busy and busy[0][0] <= t:
        _, idx = heappop(busy)
        insort(ready_list, idx)
      
      if not ready_list:
        continue
        
      idx = i % k
      # print('curr', i, t, ready_list)
      
      if idx > ready_list[-1]:
        idx = ready_list[0]
        del ready_list[0]
      else:
        jdx = bisect_left(ready_list, idx)
        idx = ready_list[jdx]
        del ready_list[jdx]
        
      # print('work to', idx)
      counter[idx] += 1
      heappush(busy, (t+load[i], idx))
    
    ans = []
    # print(counter)
    
    for i, cnt in enumerate(counter):
      if not ans or cnt == counter[ans[0]]:
        ans.append(i)
        continue
        
      if cnt > counter[ans[0]]:
        ans.clear()
        ans.append(i)
        
    return ans
  