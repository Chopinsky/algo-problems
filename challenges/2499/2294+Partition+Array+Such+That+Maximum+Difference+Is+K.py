'''
2294. Partition Array Such That Maximum Difference Is K

You are given an integer array nums and an integer k. You may partition nums into one or more
subsequences such that each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum 
and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no 
elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [3,6,1,2,5], k = 2
Output: 2
Explanation:
We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of 
subsequences needed.
Example 2:

Input: nums = [1,2,3], k = 1
Output: 2
Explanation:
We can partition nums into the two subsequences [1,2] and [3].
The difference between the maximum and minimum value in the first subsequence is 2 - 1 = 1.
The difference between the maximum and minimum value in the second subsequence is 3 - 3 = 0.
Since two subsequences were created, we return 2. Note that another optimal solution is to partition 
nums into the two subsequences [1] and [2,3].
Example 3:

Input: nums = [2,2,4,5], k = 0
Output: 3
Explanation:
We can partition nums into the three subsequences [2,2], [4], and [5].
The difference between the maximum and minimum value in the first subsequences is 2 - 2 = 0.
The difference between the maximum and minimum value in the second subsequences is 4 - 4 = 0.
The difference between the maximum and minimum value in the third subsequences is 5 - 5 = 0.
Since three subsequences were created, we return 3. It can be shown that 3 is the minimum number of 
subsequences needed.

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
0 <= k <= 10^5
'''

from typing import List


class Solution:
  def partitionArray(self, nums: List[int], k: int) -> int:
    cand = sorted(set(nums))
    count = 1
    start = cand[0]
    # print('init:', cand)

    for val in cand[1:]:
      if val-start > k:
        start = val
        count += 1

    return count
        
  def partitionArray(self, nums: List[int], k: int) -> int:
    unique_num = sorted(set(nums))
    start_num = unique_num[0] 
    count = 1
    # print(unique_num)
          
    for i, val in enumerate(unique_num):
      if val-start_num > k:
        start_num = val
        count += 1
      
    return count
  