'''
2461. Maximum Sum of Distinct Subarrays With Length K

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.

Constraints:

1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''

from collections import Counter, defaultdict
from typing import List


class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    dup_count = 0
    counter = defaultdict(int)
    ans = 0
    curr = 0
    
    for i in range(len(nums)):
      val = nums[i]
      curr += val
      counter[val] += 1
      if counter[val] == 2:
        dup_count += 1
        
      if i >= k:
        prev = nums[i-k]
        curr -= prev
        counter[prev] -= 1
        if counter[prev] == 1:
          dup_count -= 1
          
      # print('iter:', i, curr, counter, dup_count)
      if i >= k-1 and dup_count == 0:
        ans = max(ans, curr)
    
    return ans
        
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    counter = Counter(nums[:k])
    sums = sum(nums[:k])
    ans = sums if len(counter) == k else 0
    # print(counter, sums)
    
    for i in range(k, len(nums)):
      curr, last = nums[i], nums[i-k]
      counter[last] -= 1
      if not counter[last]:
        counter.pop(last, None)
        
      counter[curr] = counter.get(curr, 0) + 1
      sums += curr - last
      
      if len(counter) == k:
        ans = max(ans, sums)
        # print(i, counter, sums)
      
    return ans
    