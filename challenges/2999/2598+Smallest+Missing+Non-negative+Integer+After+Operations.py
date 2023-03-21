'''
2598. Smallest Missing Non-negative Integer After Operations

You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.
 
Constraints:

1 <= nums.length, value <= 10^5
-10^9 <= nums[i] <= 10^9
'''

from typing import List
from collections import defaultdict, Counter


class Solution:
  def beautifulSubsets(self, nums: list[int], k: int) -> int:
    n = len(nums)
    masks = [0] * n
    
    # get forbidden numbers' index
    for i in range(n):
      for j in range(n):
        if i == j:
          continue
          
        if abs(nums[i] - nums[j]) == k:
          masks[i] |= 1 << j

    # init set with masks
    cnt = Counter({0: 1})
    
    # keep adding numbers to the valid subsets
    for i in range(n):
      next_cnt = Counter()
      for mask, freq in cnt.items():
        if not (mask & (1 << i)):
          next_cnt[mask | masks[i]] += freq
          
      cnt += next_cnt

    return sum(cnt.values()) - 1
  

  def findSmallestInteger(self, nums: List[int], value: int) -> int:
    cnt = defaultdict(int)
    for val in nums:
      mod = val % value
      cnt[mod] += 1
      # print(val, mod)
      
    # print(cnt)
    if 0 not in cnt:
      return 0
    
    v0 = 0
    vc = cnt[0]
    
    for v1 in range(1, value):
      if v1 not in cnt:
        return v1
      
      if cnt[v1] < vc:
        v0 = v1
        vc = cnt[v1]
      
    # print(v0, vc)
    return vc*value+v0
    