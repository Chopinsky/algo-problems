'''
1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4

Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10^5
All the integers in rating are unique.
'''

from typing import List

class Solution:
  def numTeams(self, rating: List[int]) -> int:
    up = [0]
    down = [0]
    n = len(rating)
    
    for i in range(1, n):
      v0 = rating[i]
      c0 = 0
      c1 = 0
      
      for j in range(i):
        v1 = rating[j]
        if v0 > v1:
          c0 += 1
        
        if v0 < v1:
          c1 += 1
      
      up.append(c0)
      down.append(c1)
    
    count = 0
    # print(up, down)
    
    for i in range(2, n):
      v0 = rating[i]
      
      for j in range(1, i):
        v1 = rating[j]
        
        if v0 > v1:
          count += up[j]
        
        if v0 < v1:
          count += down[j]
    
    return count
    
  def numTeams(self, rating: List[int]) -> int:
    arr = sorted((val, i) for i, val in enumerate(rating))
    n = len(rating)
    fenwick = [0]*(n+1)
    total = 0
    
    def query(idx: int) -> int:
      s = fenwick[0]
      while idx > 0:
        s += fenwick[idx]
        idx -= (idx & -idx)
      
      return s
    
    def update(idx: int) -> int:
      if idx == 0:
        fenwick[idx] += 1
        return
      
      while idx < n:
        fenwick[idx] += 1
        idx += (idx & -idx)
    
    # print(arr)
    
    for small in range(0, n):
      idx = arr[small][1]
      if small > 0 and small < n-1 and idx > 0 and idx < n-1:
        left_small = query(idx)
        left_large = idx - left_small
        large = n-small-1
        right_small = small - left_small
        right_large = large - left_large
        
        # print(small, arr[small], (left_small, right_large), (left_large, right_small))
        total += (left_small * right_large) + (left_large * right_small)

      update(idx)
    
    return total
        