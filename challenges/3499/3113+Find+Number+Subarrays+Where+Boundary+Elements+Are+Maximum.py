'''
3113. Find the Number of Subarrays Where Boundary Elements Are Maximum

You are given an array of positive integers nums.

Return the number of subarrays of nums, where the first and the last elements of the subarray are equal to the largest element in the subarray.

Example 1:

Input: nums = [1,4,3,3,2]

Output: 6

Explanation:

There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray:

subarray [1,4,3,3,2], with its largest element 1. The first element is 1 and the last element is also 1.
subarray [1,4,3,3,2], with its largest element 4. The first element is 4 and the last element is also 4.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [1,4,3,3,2], with its largest element 2. The first element is 2 and the last element is also 2.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
Hence, we return 6.

Example 2:

Input: nums = [3,3,3]

Output: 6

Explanation:

There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray:

subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
Hence, we return 6.

Example 3:

Input: nums = [1]

Output: 1

Explanation:

There is a single subarray of nums which is [1], with its largest element 1. The first element is 1 and the last element is also 1.

Hence, we return 1.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''

from typing import List

class Solution:
  '''
  use the monotonic decreasing array to store the previous largest number, and if the tail value
  matches the number currently being examined, then we can form <count> number of subarrays meeting
  the requirement; here <count> is the number of this value seen prior before a bigger value has been
  seen in the scan process
  '''
  def numberOfSubarrays(self, nums: List[int]) -> int:
    stack = []
    count = 0
    
    for val in nums:
      # pop any numbers that are smaller, these numbers can no longer
      # serve as the boundary values of the subarrays
      while stack and stack[-1][0] < val:
        stack.pop()
        
      # updating the numbers that can be formed for the subarrays
      if stack and stack[-1][0] == val:
        stack[-1][1] += 1
      else:
        stack.append([val, 1])
    
      count += stack[-1][1]
      
    return count
        