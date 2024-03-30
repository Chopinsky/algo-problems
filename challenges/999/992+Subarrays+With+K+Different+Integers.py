'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length
'''


from typing import List
from collections import defaultdict

class Solution:
  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    cnt = defaultdict(int)
    n = len(nums)
    j0, subs = 0, 0
    
    for i in range(n):
      if i > 0:
        v0 = nums[i-1]
        cnt[v0] -= 1
        if not cnt[v0]:
          del cnt[v0]
      
      while j0 < n and len(cnt) < k:
        cnt[nums[j0]] += 1
        j0 += 1
      
      if j0 >= n and len(cnt) < k:
        break
        
      j1 = j0
      while j1 < n and nums[j1] in cnt:
        j1 += 1
        
      # print('iter:', (i, j0, j1), j1-j0+1)
      subs += j1-j0+1
        
    return subs
        
  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    counter = {}
    start, left = 0, 0
    count = 0

    # val serves as the right side bound of the window for 
    # [start, index_of_val], we need to find the next window
    # with `k` unique numbers and check how many of the smaller
    # windows can exist in the current big window
    for val in nums:
      if val in counter:
        counter[val] += 1
      else:
        counter[val] = 1

      # remove the distinct at the start of the window, i.e. shifting 
      # the window by moving the pointers forward by 1
      if len(counter) == k+1:
        counter.pop(nums[left], None)
        left += 1
        start = left

      # update the window and the total tally, in the end, there will 
      # one and only one nums[left] in the counter, because of
      # the `counter[nums[left]] > 1` condition
      if len(counter) == k:
        while counter[nums[left]] > 1:
          counter[nums[left]] -= 1
          left += 1

        count += left - start + 1

    return count

  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    cs = set(nums)
    if len(cs) < k:
      return 0
    
    n = len(nums)
    count = 0
    pos = defaultdict(list)
    counter = {}
    
    for i, val in enumerate(nums):
      pos[val].append(i)
    
    i, r = 0, 0
    while i < n:
      l = i
      base = None
      
      while r < n and len(counter) < k:
        val = nums[r]
        if val in counter:
          counter[val] += 1
          
        elif len(counter) < k:
          counter[val] = 1
          if len(counter) == k:
            # freeze the unique numbers in the window
            base = set(counter)  
            break
          
        r += 1
      
      # print(i, 'expanding done', l, r, base, counter)
      # we haven't gotten enough unique numbers from i
      # and onwards, done and break
      if not base:
        break
        
      # now [i, j] is the max-range for this window, 
      # let's try find smaller windows
      while r < n:
        while l < r and counter[nums[l]] > 1:
          counter[nums[l]] -= 1
          l += 1
          
        # print(i, 'adding:', count, l-i+1, l, r)
        count += l-i+1
        r += 1
        
        # next right letter is not good
        if r >= n or nums[r] not in base:
          break
      
        # add this number to the counter
        counter[nums[r]] += 1
      
      # print(i, 'shrinking done', l, r, count, counter)
      # done with this window, now shift 1 from the left
      counter[nums[l]] -= 1
      if not counter[nums[l]]:
        counter.pop(nums[l], None)
        
      i = l+1
    
    return count
        