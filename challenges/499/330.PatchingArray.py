'''
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].

Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 10 ** 4
nums is sorted in ascending order.
1 <= n <= 2 ** 31 - 1

Test cases:

[1,3]
6
[1,5,10]
20
[1,2,2]
5
[1,7,21,31,34,37,40,43,49,87,90,92,93,98,99]
12
[1,2,31,33]
2147483647
[1,2,16,19,31,35,36,64,64,67,69,71,73,74,76,79,80,91,95,96,97]
8
'''

from typing import List

class Solution:
  def minPatches(self, nums: List[int], n: int) -> int:
    top = 0
    ops = 0

    if nums[0] > 1:
      # add 1 to the array
      top = 1
      ops += 1
    
    for curr in nums:
      # print('iter:', curr, top, ops)
      while top+1 < curr and top < n:
        val = top+1
        top += val
        ops += 1
        
      top += curr
      if top >= n:
        break
      
    while top < n:
      val = top+1
      top += val
      ops += 1
        
    return ops
        

  '''
  use the idea of `dynamic programming` without using dp.

  idea is that suppose we've patched the array up to index `i-1`, such that
  all numbers in [1, sum(nums[:i])] can be formed using the patched array up
  to index `i-1`, then if: a) nums[i] > sum(nums[:i]), we keep inserting 
  the `sub_arr_sum + 1` to getting a new range coverage, until -- b) 
  nums[i] <= sum(patched_nums[:i]), and we use nums[i] to form the new array
  without insertions.

  so in plainer words, for a subarray that's patched and can reach any number
  in range [1, m], then adding n to the array will make the coverage extends
  to [1, m+n] without any gap. but the original array must be in ascending 
  order to make this possible.
  '''
  def minPatches(self, nums: List[int], n: int) -> int:
    count = 0 if nums[0] == 1 else 1
    idx = 1 if nums[0] == 1 else 0
    curr = 1
    top = 1
    
    while top < n:
      # print('iter:', idx, curr, top)
      
      # loop over between `curr` and `nums[idx]` to insert numbers
      # that are missing
      while idx < len(nums) and nums[idx] > top+1 and top < n:
        curr = top+1
        top += curr
        count += 1
        
      # in case we're done in the loop above
      if top >= n:
        break
        
      if idx < len(nums):
        # use the number in the array
        curr = nums[idx]
        idx += 1
      else:
        # insert a new number `top+1`, and increament the count
        curr = top+1
        count += 1
        
      top += curr

    return count
        