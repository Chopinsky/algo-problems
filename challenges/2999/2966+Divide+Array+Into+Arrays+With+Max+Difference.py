'''
2966. Divide Array Into Arrays With Max Difference

You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

Example 1:

Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.
Example 2:

Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.

Constraints:

n == nums.length
1 <= n <= 10^5
n is a multiple of 3.
1 <= nums[i] <= 10^5
1 <= k <= 10^5
'''

from typing import List


class Solution:
  def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    nums.sort()
    ans = []
    n = len(nums)

    for i in range(0, n, 3):
      arr = nums[i:i+3]
      # print('iter:', arr)
      if arr[-1]-arr[0] > k:
        return []

      ans.append(arr)

    return ans

  def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    n = len(nums)
    if n%3 != 0:
      return []
    
    nums.sort()
    ans = []
    
    for i in range(0, n, 3):
      if nums[i+2]-nums[i] > k:
        return []
      
      ans.append(nums[i:i+3])
      
    return ans
        