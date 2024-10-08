'''
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 

Constraints:

arr.length == n
1 <= n <= 10^5
n is even.
-10^9 <= arr[i] <= 10^9
1 <= k <= 10^5
'''

from typing import List
from collections import defaultdict


class Solution:
  def canArrange(self, arr: List[int], k: int) -> bool:
    cnt = defaultdict(int)
    for val in arr:
      cnt[val % k] += 1
      
    # print(cnt)
    for val, c0 in cnt.items():
      if val == 0:
        if c0 % 2 == 1:
          return False
        
        continue
      
      cval = k - val
      c1 = cnt[cval]
        
      if c0 != c1:
        return False
      
    return True
        
  def canArrange(self, arr: List[int], k: int) -> bool:
    cand = defaultdict(int)
    for val in arr:
      mod = val % k
      if mod == 0:
        if cand[0] > 0:
          cand[0] -= 1
        else:
          cand[0] += 1
          
        continue
        
      if mod and cand[k-mod] > 0:
        cand[k-mod] -= 1
      else:
        cand[mod] += 1
      
    # print(arr, cand)
    return all(val == 0 for val in cand.values())
  