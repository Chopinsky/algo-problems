'''
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''

from heapq import heappush, heappop
from typing import List


class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    ans = []
    store = {}
    stack = []
    
    for i in range(k):
      val = nums[i]
      if val not in store:
        store[val] = 1
        heappush(stack, -val)
      else:
        store[val] += 1
    
    ans.append(-stack[0])
    
    for i in range(k, len(nums)):
      v0 = nums[i-k]
      v1 = nums[i]
      
      store[v0] -= 1
      if v1 not in store:
        store[v1] = 1
      else:
        store[v1] += 1
        
      if not store[v0]:
        store.pop(v0, None)
        
      if store[v1] == 1:
        heappush(stack, -v1)
        
      while stack and (-stack[0] not in store):
        heappop(stack)
      
      ans.append(-stack[0])
    
    return ans
  