'''
You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
The power of a city is the total number of power stations it is being provided power from.

The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

Note that you can build the k power stations in multiple cities.

Example 1:

Input: stations = [1,2,4,5,0], r = 1, k = 2
Output: 5
Explanation: 
One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.
Example 2:

Input: stations = [4,4,4,4], r = 0, k = 3
Output: 4
Explanation: 
It can be proved that we cannot make the minimum power of a city greater than 4.

Constraints:

n == stations.length
1 <= n <= 10^5
0 <= stations[i] <= 10^5
0 <= r <= n - 1
0 <= k <= 10^9
'''

from typing import List
from collections import defaultdict


class Solution:
  '''
  the key is to use binary search to guess the max-min-power for the problem, and for
  each guess number, we can check if this floor-power can be achieved.

  for checking the viability of a floor-power value, we use a sweaping line to check
  if an accumulated power station additions from previous cities will lift the current
  city under check over the floor-power requirement -- if we need to build more after 
  addition, then we must build extra power stations at this city, otherwise, we're good;
  also need to update the power additions at current city, we keep track of where the
  previous power additions will fall out of the range, and update the accumulation value
  accordingly at every city before checking the power requirements and build.
  '''
  def maxPower(self, stations: List[int], r: int, k: int) -> int:
    n = len(stations)
    padding = 2*r + 1
    curr = sum(stations[:r+1])
    p = [curr]
    
    for m in range(1, n):
      j, i = m-r-1, m+r
      if i < n:
        curr += stations[i]
        
      if j >= 0:
        curr -= stations[j]
        
      # print(m, curr, i, j)
      p.append(curr)
          
    # we can add power stations in the middle-index 
    # and it will cover all cities including the min-power
    # city
    if padding >= n:
      return min(p) + k
    
    # check if the floor-power is viable
    def check(floor_power: int) -> bool:
      used = 0
      actions = defaultdict(int)
      accum = 0
      
      for i in range(n):
        # update extra powers provided from previous new stations
        accum += actions[i]

        # check the deficit from the floor-power requirement
        extra = floor_power - (p[i] + accum)
        
        # need to build more power stations here
        if extra > 0:
          accum += extra
          used += extra

          # remove influence of the power stations built at
          # city-i at city-(i+padding)
          actions[i+padding] += -extra
            
        # we built more than we can, fail
        if used > k:
          return False
                
      return True
      
    low, high = min(p), k+max(p)+1
    ans = low
    # print('init:', low, high)
    
    while low <= high:
      mid = (low + high) // 2
      # print('test:', mid, (low, high))
      
      if check(mid):
        ans = mid
        low = mid+1
      else:
        high = mid-1
      
    return ans
  
  
  '''TLE
  def maxPower1(self, stations: List[int], r: int, k: int) -> int:
    n = len(stations)      
    if n == 1:
      return stations[0] + k
      
    curr = sum(stations[:r+1])
    s = [curr]
    extra = [0]*(n+1)
    
    def update(idx, val):
      if idx >= n:
        # print('skip', idx, val)
        return
      
      idx += 1
      while idx <= n:
        extra[idx] += val
        idx += (idx & -idx)
        
    def query(idx):
      if idx >= n:
        # print('skip', idx, val)
        return
      
      cnt = 0
      idx += 1
      
      while idx > 0:
        cnt += extra[idx]
        idx -= (idx & -idx)
        
      return cnt
    
    for m in range(1, n):
      j, i = m-r-1, m+r
      if i < n:
        curr += stations[i]
        
      if j >= 0:
        curr -= stations[j]
        
      # print(m, curr, i, j)
      s.append(curr)
    
    q = sorted([(c, abs(n//2-i), i) for i, c in enumerate(s)])
    # print(s, q)
    
    def get_one():
      while q:
        c0, _, idx = q[0]
        c1 = s[idx] + query(idx)
        if c0 == c1:
          break
          
        heappop(q)
        heappush(q, (c1, abs(n//2-idx), idx))
          
      return q[0][0], q[0][2]
        
    while k > 0:
      c0, i = get_one()
      heappop(q)
      
      c1, j = get_one()
      addition = 1 if c1 == c0 else min(c1-c0+1, k)
      # print('pop:', (c0, i), (c1, j), addition, k)
      k -= addition
      
      if r > 0 and abs(i-j) <= 2*r+1:
        left = min(i, j)
      else:
        left = 0 if i <= r else i-r  
        
      right = left + 2*r + 1 
      if right > n:
        right = n
        left = max(0, right-2*r-1)
      
      # update the [left, right] range
      update(left, addition)
      update(right, -addition)
      # print('add to:', i, j, (left, right-1), addition, query(i), extra)
      
      heappush(q, (c0+addition, abs(n//2-i), i))
      # print('action:', i, c0+addition, s[i]+query(i), query(i))
      
    c0, _ = get_one()
    return c0
  '''
  