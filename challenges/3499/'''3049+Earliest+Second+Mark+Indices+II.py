'''
3049. Earliest Second to Mark Indices II

You are given two 1-indexed integer arrays, nums and, changeIndices, having lengths n and m, respectively.

Initially, all indices in nums are unmarked. Your task is to mark all indices in nums.

In each second, s, in order from 1 to m (inclusive), you can perform one of the following operations:

1. Choose an index i in the range [1, n] and decrement nums[i] by 1.
2. Set nums[changeIndices[s]] to any non-negative value.
3. Choose an index i in the range [1, n], where nums[i] is equal to 0, and mark index i.
4. Do nothing.

Return an integer denoting the earliest second in the range [1, m] when all indices in nums can be marked by choosing operations optimally, or -1 if it is impossible.

Example 1:

Input: nums = [3,2,3], changeIndices = [1,3,2,2,2,2,3]
Output: 6
Explanation: In this example, we have 7 seconds. The following operations can be performed to mark all indices:
Second 1: Set nums[changeIndices[1]] to 0. nums becomes [0,2,3].
Second 2: Set nums[changeIndices[2]] to 0. nums becomes [0,2,0].
Second 3: Set nums[changeIndices[3]] to 0. nums becomes [0,0,0].
Second 4: Mark index 1, since nums[1] is equal to 0.
Second 5: Mark index 2, since nums[2] is equal to 0.
Second 6: Mark index 3, since nums[3] is equal to 0.
Now all indices have been marked.
It can be shown that it is not possible to mark all indices earlier than the 6th second.
Hence, the answer is 6.
Example 2:

Input: nums = [0,0,1,2], changeIndices = [1,2,1,2,1,2,1,2]
Output: 7
Explanation: In this example, we have 8 seconds. The following operations can be performed to mark all indices:
Second 1: Mark index 1, since nums[1] is equal to 0.
Second 2: Mark index 2, since nums[2] is equal to 0.
Second 3: Decrement index 4 by one. nums becomes [0,0,1,1].
Second 4: Decrement index 4 by one. nums becomes [0,0,1,0].
Second 5: Decrement index 3 by one. nums becomes [0,0,0,0].
Second 6: Mark index 3, since nums[3] is equal to 0.
Second 7: Mark index 4, since nums[4] is equal to 0.
Now all indices have been marked.
It can be shown that it is not possible to mark all indices earlier than the 7th second.
Hence, the answer is 7.
Example 3:

Input: nums = [1,2,3], changeIndices = [1,2,3]
Output: -1
Explanation: In this example, it can be shown that it is impossible to mark all indices, as we don't have enough seconds. 
Hence, the answer is -1.
 

Constraints:

1 <= n == nums.length <= 5000
0 <= nums[i] <= 10^9
1 <= m == changeIndices.length <= 5000
1 <= changeIndices[i] <= n

Test cases:

[0]
[1]

[2]
[1,1,1]

[3,2,3]
[1,3,2,2,2,2,3]

[0,0,1,2]
[1,2,1,2,1,2,1,2]

[1,2,3]
[1,2,3]

[5,3,2,0,3,5]
[4,3,6,5,6,5,3,6,4,1,2,3,6,1]

[2,2]
[1,2,1,1,2,2,2]

[2,2]
[2,2,1,2]

[3,4]
[2,2,1,1,2,2,1,2,1]

[4,2,2]
[1,2,3,1,1,3,1,3,3,2,1,2]
'''

from typing import List
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
  '''
  the main algo is to find the min-second where we can mark all the `nums`, this can be done 
  using the binary search, and the search range is [n, m], where `n=len(nums)`, and `m=len(changeIndices)`;

  the next step is to check if the `nums` can be marked in `time` seconds -- the goal is to
  fit as many of op-2 for large numbers as possible, and the optimal cost of time is:
    t = n                             # mark ops
        + count_op2                   # 1 op for each op-2
        + sum(nums_not_done_with_op2) # op-1 to reduce val to 0
  and we want t <= time if it's doable in `time` seconds;

  to get the optimal op2 assignment, we can greedily check backwards: from the last index in
  changeIndices[:time] to the first index; then if this is the fist time an index in `nums` 
  can be reduced by op2 (i.e., last encounter in the backwards scan), we check if we have enough
  time-slot left in the [curr_time, time] side to perform op2; if we have enough space left, 
  we can do op2; if not, we check if we can pop an op2 in the [curr_time, time] slot that make
  less cost to do op1 instead, and we replace that one with the curren index being checked; this
  will maximize the amount of op2 and minimize the cost of op1 in total;
  '''
  def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
    n, m = len(nums), len(changeIndices)
    if n == 1:
      cost = 1 + (nums[0] if 1 not in changeIndices or nums[0] == 0 else 1)
      return cost if cost <= m else -1
    
    def can_mark():
      pos = set(changeIndices[:-1])
      cost, cnt = n, 0
      
      for i in range(n):
        val = nums[i]
        if val == 0:
          cnt += 1
          continue
        
        if i+1 in pos:
          cost += 1
        else:
          cost += val
          
      return cost <= m, cnt

    def check(t: int):
      cost = n
      cand = []
      used = set()
      counter = {}
            
      def update(val: int, idx: int, pop: bool):
        if pop:
          # pop replacement
          _, j = heappop(cand)
          used.discard(j)
            
        # add
        heappush(cand, (val, idx))
        used.add(idx)

      for p, i in enumerate(changeIndices[:t-1]):
        i -= 1
        if i not in counter:
          counter[i] = p
      
      for p in range(t-2, -1, -1):
        i = changeIndices[p]-1
        if i in used or counter[i] != p:
          continue
          
        space = (t-p) - 2*len(used)
        v0 = nums[i]
        
        # can just add
        if space >= 2:
          update(v0, i, False)
          continue
        
        # no candidate to replace with
        if len(cand) == 0:
          continue
        
        # find the candidate to replace
        if (v0 > cand[0][0]) or (v0 == cand[0][0] and counter[cand[0][1]] > 0):
          update(v0, i, True)
      
      # update the final costs
      for i in range(n):
        val = nums[i]
        if val == 0:
          continue
          
        if i in used:
          cost += 1
        else:
          cost += val

      # print('check:', t, used, cost)
      return cost <= t
      
    res, cnt = can_mark()
    # print('init:', cnt, total, m)
    
    if not res:
      return -1
    
    if cnt == n:
      return n
    
    l, r = n, m
    last = -1
    
    while l <= r:
      mid = (l+r) // 2
      if check(mid):
        last = mid
        r = mid-1
      else:
        l = mid+1
    
    return last
        