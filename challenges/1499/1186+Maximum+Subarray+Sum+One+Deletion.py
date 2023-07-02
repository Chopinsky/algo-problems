'''
1186. Maximum Subarray Sum with One Deletion

Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.

Constraints:

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
'''

from typing import List


class Solution:
  def maximumSum(self, arr: List[int]) -> int:
    result = max(arr)
    n = len(arr)
    if n == 1:
      return result
    
    prefix = [val for val in arr]
    for i in range(1, n):
      prefix[i] += prefix[i-1]

    small = min(0, prefix[0])
    large = prefix[-1]
    left = [0]*n
    right = [0]*n
    
    if n > 1:
      left[1] = arr[0]
      right[-2] = arr[-1]
    
    for i in range(2, n):
      left[i] = prefix[i-1] - small
      small = min(small, prefix[i-1])
    
    for i in range(n-2, -1, -1):
      right[i] = large - prefix[i]
      large = max(large, prefix[i])
    
    # print(left, right)
    
    for i in range(n):
      # print(i, result)
      if i == 0:
        result = max(result, arr[i], arr[i]+right[i], right[i])
        continue
        
      if i == n-1:
        result = max(result, arr[i], left[i]+arr[i], left[i])
        continue
        
      result = max(result, arr[i], left[i]+arr[i], arr[i]+right[i], left[i]+right[i], left[i]+arr[i]+right[i])
    
    return result
        