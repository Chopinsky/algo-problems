'''
You are given two 0-indexed integer arrays nums1 and nums2, both of length n.

You can choose two integers left and right where 0 <= left <= right < n and swap the subarray nums1[left...right] with the subarray nums2[left...right].

For example, if nums1 = [1,2,3,4,5] and nums2 = [11,12,13,14,15] and you choose left = 1 and right = 2, nums1 becomes [1,12,13,4,5] and nums2 becomes [11,2,3,14,15].
You may choose to apply the mentioned operation once or not do anything.

The score of the arrays is the maximum of sum(nums1) and sum(nums2), where sum(arr) is the sum of all the elements in the array arr.

Return the maximum possible score.

A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).

Example 1:

Input: nums1 = [60,60,60], nums2 = [10,90,10]
Output: 210
Explanation: Choosing left = 1 and right = 1, we have nums1 = [60,90,60] and nums2 = [10,60,10].
The score is max(sum(nums1), sum(nums2)) = max(210, 80) = 210.
Example 2:

Input: nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20]
Output: 220
Explanation: Choosing left = 3, right = 4, we have nums1 = [20,40,20,40,20] and nums2 = [50,20,50,70,30].
The score is max(sum(nums1), sum(nums2)) = max(140, 220) = 220.
Example 3:

Input: nums1 = [7,11,13], nums2 = [1,1,1]
Output: 31
Explanation: We choose not to swap any subarray.
The score is max(sum(nums1), sum(nums2)) = max(31, 3) = 31.

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
1 <= nums1[i], nums2[i] <= 10^4
'''

from typing import List


class Solution:
  '''
  the trick is to find the subarray whose swapped diff will yield the maximum addition to the source
  array's post-swap sums. so we keep a prefix array for the diff between each values at index-i between
  the source and the target array, then `curr_prefix_diff - prev_small_diff` will yield the maximum swap
  addition to the source array, and we keep updating the `prev_small_diff` for each index we visited.

  this algorithm can be further simplified to only 1 iteration -- we want the `max_diff` as well as the `min_diff`,
  and `max_diff` for nums1 and `min_diff` for nums2, but it's more complex to keep all these states (we need
  2 separate sets of variables to store max/min states).
  '''
  def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    
    def find_max(n1: List[int], n2: List[int]) -> int:
      last_diff = 0
      prev_low = 0
      max_add = 0
      s = 0
      
      for i in range(n):
        s += n1[i] 
        d0 = n2[i] - n1[i]
        prefix_diff = last_diff + d0

        max_add = max(max_add, d0, prefix_diff-prev_low)
        prev_low = min(prev_low, prefix_diff)
        last_diff = prefix_diff
      
      # print(diff, max_add)
      return s + max_add
    
    return max(find_max(nums1, nums2), find_max(nums2, nums1))
    