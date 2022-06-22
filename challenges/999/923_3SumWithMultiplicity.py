'''
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
'''

from typing import List
from collections import defaultdict


class Solution:
  def threeSumMulti(self, arr: List[int], target: int) -> int:
    table = defaultdict(int)
    for num in arr:
      table[num] += 1
      
    mod = 10**9 + 7
    keys = list(table.keys())
    n = len(keys)
    count = 0
    
    for i in range(n):
      x = keys[i]
      for j in range(i, n):
        y = keys[j]
        z = target - x - y

        if z not in table:
          continue

        if x == y == z:
          # comb(table[x], 3)
          count += table[x] * (table[x]-1) * (table[x]-2) // 6
          
        elif x == y:  # i == j and j != k
          # comb(table[x], 2) * table[z]
          count += (table[x] * (table[x] - 1) // 2) * table[z]
          
        elif x < z and y < z:
          # all different nums
          count += table[x] * table[y] * table[z]
                
    return count % mod

  
  def threeSumMulti0(self, arr: List[int], target: int) -> int:
    mod = 10**9 + 7
    sums = defaultdict(int)
    sums[arr[0]+arr[1]] += 1
    count = 0
    
    for i in range(2, len(arr)):
      val = target - arr[i]
      if val in sums:
        count = (count + sums[val]) % mod
        
      if i == len(arr)-1:
        continue
        
      for j in range(i):
        sums[arr[i]+arr[j]] += 1
      
    return count  
    