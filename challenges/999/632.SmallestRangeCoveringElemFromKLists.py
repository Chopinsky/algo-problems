'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
Example 3:

Input: nums = [[10,10],[11,11]]
Output: [10,11]
Example 4:

Input: nums = [[10],[11]]
Output: [10,11]
Example 5:

Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-10^5 <= nums[i][j] <= 10^5
nums[i] is sorted in non-decreasing order.
'''

from typing import List
from heapq import heappush, heappop
from collections import defaultdict
import math


class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    k = len(nums)
    if k == 1:
      return [nums[0][0], nums[0][0]]
    
    cnt = defaultdict(int)
    cand = []
        
    for i in range(k):
      for val in nums[i]:
        cand.append((val, i))
    
    ans = None
    cand.sort()
    j = 0
    n = len(cand)
    # print('init:', cand)
    
    def check(l: int, r: int):
      if not ans:
        return True
      
      l0 = r-l
      l1 = ans[1]-ans[0]
      
      return l0 < l1
    
    for i in range(n):
      # pop prev
      if i > 0:
        idx = cand[i-1][1]
        cnt[idx] -= 1
        if not cnt[idx]:
          del cnt[idx]
          
      j = max(i, j)
      left, _ = cand[i]
      
      while j < n and len(cnt) < k:
        right, idx = cand[j]
        cnt[idx] += 1
        j += 1
      
      # done
      if j >= n and len(cnt) < k:
        break
        
      # print('found:', (left, right), cnt, ans)
      if check(left, right):
        ans = [left, right]
    
    return ans
  
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    stack = []
    k = len(nums)
    left, right = math.inf, -math.inf
    
    for i in range(k):
      heappush(stack, (nums[i][0], i, 0))
      left = min(nums[i][0], left)
      right = max(nums[i][0], right)
      
    rng = [left, right]
    # print(rng, stack)
    
    while True:
      val, i, j = heappop(stack)
      
      # can't replace it with another number
      if j == len(nums[i]) - 1:
        break
        
      # add the number to the stack
      nxt = nums[i][j+1]
      heappush(stack, (nxt, i, j+1))
      
      # update range
      left = stack[0][0]
      right = max(nxt, right)
      # print('replace', i, nxt, left, right)
      
      if right - left < rng[1] - rng[0]:
        rng[0] = left
        rng[1] = right
      
    return rng
      