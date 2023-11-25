'''
2945. Find Maximum Non-decreasing Array Length

You are given a 0-indexed integer array nums.

You can perform any number of operations, where each operation involves selecting a subarray of the array and replacing it with the sum of its elements. For example, if the given array is [1,3,5,6] and you select subarray [3,5] the array will convert to [1,8,6].

Return the maximum length of a non-decreasing array that can be made after applying operations.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [5,2,2]
Output: 1
Explanation: This array with length 3 is not non-decreasing.
We have two ways to make the array length two.
First, choosing subarray [2,2] converts the array to [5,4].
Second, choosing subarray [5,2] converts the array to [7,2].
In these two ways the array is not non-decreasing.
And if we choose subarray [5,2,2] and replace it with [9] it becomes non-decreasing. 
So the answer is 1.
Example 2:

Input: nums = [1,2,3,4]
Output: 4
Explanation: The array is non-decreasing. So the answer is 4.
Example 3:

Input: nums = [4,3,2,6]
Output: 3
Explanation: Replacing [3,2] with [5] converts the given array to [4,5,6] that is non-decreasing.
Because the given array is not non-decreasing, the maximum possible answer is 3.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''

from typing import List
from bisect import bisect_right


class Solution:
  '''
  the idea is to build the answer, aka dp, from len == 0 to len == size of `nums`; for len == ln,
  we find the first index-j, such that for array built for dp[j], the last value is last_val[j],
  and sum(nums[j+1:ln]) >= last_val[j], this will guarantee that the new array after merging nums[j+1:ln]
  will still be a non-decreasing array, and we append sum(nums[j+1:ln]) to the array built for dp[j];

  how to efficient find this index-j? use a monotonic increasing queue.

  the queue will have each element as a tuple of: (last_val[i]+prefix[i]); adding prefix[i] is to 
  enable us to find the index-j using bisect, becase we want to find sum(nums[j+1:ln]) >= last_val[j],
  so adding prefix[j] on both side will give us: sum(nums[ln]) >= last_val[j]+prefix[j], and the right
  hand side can be known before appending to the queue. 

  so once we build the queue, we can find index-j using `bisect_right(queue, (prefix[i], ))`, and then
  we shall pop the tail of the queue whose pre-calc value is greater or equal than last_val[i]+prefix[i].

  for Python, we use a `ln` variable to mark the last valid index in the queue, such that we only consider
  partial of the queue for calculations: i.e., the queue for calc is `queue[:ln]`, however, the queue
  in the memory can have a longer lenght; we do this to minimize the number of allocations in this frequent
  push-pop algo
  '''
  def findMaximumLength(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
      return n if nums[-1] >= nums[0] else 1
    
    prefix = [val for val in nums]
    for i in range(1, n):
      prefix[i] += prefix[i-1]
    
    # dp == [(length of final array after ops, last value in this array)]
    dp = [(0, 0), (1, nums[0])]

    # s0 == [last value of the array in stack]
    s0 = [0, nums[0]+prefix[0]]
    # s1 == [index of the array in dp]
    s1 = [0, 1]
    # size of the stack after shinks
    ln = 2
    
    for i in range(1, n):
      # print('iter', nums[i], prefix[i], stack)
      k0 = bisect_right(s0, prefix[i], lo=0, hi=ln)-1
      j = dp[k0][0]
      dp.append((dp[j]+1, prefix[i]-(prefix[j-1] if j > 0 else 0)))
      
      # suffix value to insert to the monotonic increasing queue
      sv = dp[-1][1] + prefix[i]
      idx = len(dp)-1

      # where to insert the new values
      k1 = bisect_right(s0, sv, lo=0, hi=ln)
        
      # print('end:', len(s0), k+1, k0+1)
      if k1 >= len(s0):
        s0.append(sv)
        s1.append(idx)
        ln = len(s0)
        
      else:
        s0[k1] = sv
        s1[k1] = idx
        ln = k1+1
      
    return dp[-1][0]
    