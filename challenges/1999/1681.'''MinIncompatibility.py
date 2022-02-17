'''
You are given an integer array nums​​​ and an integer k. You are asked to distribute this array into k subsets of equal size such that there are no two equal elements in the same subset.

A subset's incompatibility is the difference between the maximum and minimum elements in that array.

Return the minimum possible sum of incompatibilities of the k subsets after distributing the array optimally, or return -1 if it is not possible.

A subset is a group integers that appear in the array with no particular order.

Example 1:

Input: nums = [1,2,1,4], k = 2
Output: 4
Explanation: The optimal distribution of subsets is [1,2] and [1,4].
The incompatibility is (2-1) + (4-1) = 4.
Note that [1,1] and [2,4] would result in a smaller sum, but the first subset contains 2 equal elements.
Example 2:

Input: nums = [6,3,8,1,3,1,2,2], k = 4
Output: 6
Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and [1,3].
The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
Example 3:

Input: nums = [5,3,3,6,3,3], k = 3
Output: -1
Explanation: It is impossible to distribute nums into 3 subsets where no two elements are equal in the same subset.
 

Constraints:

1 <= k <= nums.length <= 16
nums.length is divisible by k
1 <= nums[i] <= nums.length
'''


from typing import List, Set, Tuple
from functools import lru_cache
from collections import Counter
import math


class Solution:
  def minimumIncompatibility00(self, nums: List[int], k: int) -> int:
    ln = len(nums)
    if ln % k or any(nums.count(num) > k for num in nums):
      return -1 
    
    nums.sort()
    n = ln // k
    res = math.inf
    buckets = [[] for _ in range(k)]

    def dp(i: int, curr_score: int, empty_buckets: int):
      nonlocal res
      
      # better results exists, done
      if curr_score + (ln-i-empty_buckets) >= res:
        return
      
      # end of the iteration
      if i == ln:
        res = min(res, curr_score)
        return

      for j in range(k):
        ### put an integer in a new bucket
        if not buckets[j]:
          # the prev bucket is empty too, illegal case and done
          if j > 0 and not buckets[j-1]:
            break 

          # put the integer#i into bucket j
          buckets[j].append(nums[i])
          dp(i+1, curr_score, empty_buckets-1)
          buckets[j].pop()

        ### put an integer in the previous bucket
        else:
          # full bucket
          if len(buckets[j]) == n:
            continue 
            
          # bucket already has this number
          if buckets[j][-1] == nums[i]:
            continue 
            
          # last bucket already used this number
          if j > 0 and len(buckets[j]) == len(buckets[j-1]) and buckets[j][-1] == buckets[j-1][-1]:
            continue

          buckets[j].append(nums[i])
          dp(i+1, curr_score+buckets[j][-1]-buckets[j][-2], empty_buckets)
          buckets[j].pop()
              
    dp(0, 0, k)
    return res
      
    
  def minimumIncompatibility(self, nums: List[int], k: int) -> int:
    self.res = math.inf
    n = len(nums)
    sets = [set() for _ in range(k)]
    bucket_limit = n // k

    def find_change(s: Set[int], x: int) -> int:
      low = min(s)
      high = max(s)
      
      if x < low:
        return low - x
      
      elif x > high:
        return x - high
      
      return 0

    def dp(i: int, score: int):
      if i == n:
        self.res = min(self.res, score)
        return

      seen = set()
      for s in sets:
        if nums[i] in s or len(s) == bucket_limit:
          continue

        tup = tuple(s)
        if tup in seen:
          continue

        seen.add(tup)
        inc = find_change(s, nums[i]) if len(s) > 0 else 0

        if score + inc < self.res:
          s.add(nums[i])
          dp(i+1, inc + score)
          s.remove(nums[i])

    dp(0, 0)
    
    if self.res == math.inf:
      return -1
    
    return self.res
      
    
  def minimumIncompatibility0(self, nums: List[int], k: int) -> int:
    if len(nums) == k:
      return 0
    
    c = Counter(nums)
    if max(c.values()) > k:
      return -1
    
    # each bucket has all numbers
    if max(c.values()) == k and min(c.values()) == k:
      # print(c)
      return max(c)-min(c)
    
    # place neighboring numbers in the same bucket
    if len(c) >= k and len(c) % k == 0 and len(set(c.values())) == 1:
      vals = sorted(c)
      span = len(c) // k
      # print(vals, [vals[i+span-1]-vals[i] for i in range(0, len(vals), span)])
      return sum(vals[i+span-1]-vals[i] for i in range(0, len(vals), span))
    
    limit = len(nums) // k
    n = len(nums)
    nums.sort()
    # print(nums)
    
    @lru_cache(None)
    def dp(i: int, buckets: Tuple) -> int:
      if i == n:
        return sum(r-l for _, l, r, _ in buckets)
      
      val = nums[i]
      base = 1 << val
      low = math.inf
      buckets = list(buckets)
      
      for j in range(k):
        cnt, l, r, mask = buckets[j]
        if cnt+1 > limit or mask & base > 0:
          continue
      
        buckets[j] = (cnt+1, l if l > 0 else val, val, mask|base)
        low = min(low, dp(i+1, tuple(sorted(buckets))))
        buckets[j] = (cnt, l, r, mask)
        
      return low
        
    return dp(0, tuple([(0, -1, -1, 0) for _ in range(k)]))
  