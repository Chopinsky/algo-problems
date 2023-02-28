'''
2576. Find the Maximum Number of Marked Indices

You are given a 0-indexed integer array nums.

Initially, all of the indices are unmarked. You are allowed to make this operation any number of times:

Pick two different unmarked indices i and j such that 2 * nums[i] <= nums[j], then mark i and j.
Return the maximum possible number of marked indices in nums using the above operation any number of times.

Example 1:

Input: nums = [3,5,2,4]
Output: 2
Explanation: In the first operation: pick i = 2 and j = 1, the operation is allowed because 2 * nums[2] <= nums[1]. Then mark index 2 and 1.
It can be shown that there's no other valid operation so the answer is 2.
Example 2:

Input: nums = [9,2,5,4]
Output: 4
Explanation: In the first operation: pick i = 3 and j = 0, the operation is allowed because 2 * nums[3] <= nums[0]. Then mark index 3 and 0.
In the second operation: pick i = 1 and j = 2, the operation is allowed because 2 * nums[1] <= nums[2]. Then mark index 1 and 2.
Since there is no other operation, the answer is 4.
Example 3:

Input: nums = [7,6,8]
Output: 0
Explanation: There is no valid operation to do, so the answer is 0.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''

from typing import List


class Solution:
  def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
      return 0
    
    nums.sort(reverse=True)
    # print(nums)
    
    marked = set()
    i, j = 0, n//2
    
    while i < n and j < n:
      if i in marked:
        i += 1
        continue
        
      while j < n and (j <= i or j in marked or nums[i] < 2*nums[j]):
        j += 1
        continue
        
      # print(i, j)
      if j >= n:
        break
      
      marked.add(i)
      marked.add(j)
      # print('pair:', (nums[i], nums[j]))
      
      i += 1
      j += 1
        
    return len(marked)
      