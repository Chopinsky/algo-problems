'''
2499. Minimum Total Cost to Make Arrays Unequal

You are given two 0-indexed integer arrays nums1 and nums2, of equal length n.

In one operation, you can swap the values of any two indices of nums1. The cost of this operation is the sum of the indices.

Find the minimum total cost of performing the given operation any number of times such that nums1[i] != nums2[i] for all 0 <= i <= n - 1 after performing all the operations.

Return the minimum total cost such that nums1 and nums2 satisfy the above condition. In case it is not possible, return -1.

Example 1:

Input: nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]
Output: 10
Explanation: 
One of the ways we can perform the operations is:
- Swap values at indices 0 and 3, incurring cost = 0 + 3 = 3. Now, nums1 = [4,2,3,1,5]
- Swap values at indices 1 and 2, incurring cost = 1 + 2 = 3. Now, nums1 = [4,3,2,1,5].
- Swap values at indices 0 and 4, incurring cost = 0 + 4 = 4. Now, nums1 =[5,3,2,1,4].
We can see that for each index i, nums1[i] != nums2[i]. The cost required here is 10.
Note that there are other ways to swap values, but it can be proven that it is not possible to obtain a cost less than 10.
Example 2:

Input: nums1 = [2,2,2,1,3], nums2 = [1,2,2,3,3]
Output: 10
Explanation: 
One of the ways we can perform the operations is:
- Swap values at indices 2 and 3, incurring cost = 2 + 3 = 5. Now, nums1 = [2,2,1,2,3].
- Swap values at indices 1 and 4, incurring cost = 1 + 4 = 5. Now, nums1 = [2,3,1,2,2].
The total cost needed here is 10, which is the minimum possible.
Example 3:

Input: nums1 = [1,2,2], nums2 = [1,2,2]
Output: -1
Explanation: 
It can be shown that it is not possible to satisfy the given conditions irrespective of the number of operations we perform.
Hence, we return -1.

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
1 <= nums1[i], nums2[i] <= n
'''

from typing import List
from collections import defaultdict


class Solution:
  '''
  the trick is to swap indices that have equal values of nums1 and nums2, this will consume most
  of the values in the array; then swap the remainder (if any) with values in nums1 that are not
  the same as the remainder values, this will handle the rest; the key observation is that the 
  most efficient solution will only take `i` cost for each index that will need to make the swap
  happen, hence we only add `i` to the final cost for each index that will need to take part in
  the swaps.
  '''
  def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    freq = defaultdict(int)
    swaps, cost = 0, 0
    max_freq, max_freq_val = 0, -1
    
    # find out which value has the highest frequency, which will be the "leftovers" after matching
    # all values that need to swap out
    for i in range(n):
      if nums1[i] != nums2[i]:
        continue
      
      val = nums1[i]
      freq[val] += 1
      cost += i
      swaps += 1
      
      if freq[val] > max_freq:
        max_freq = freq[val]
        max_freq_val = val
        
    # check all the values that are not the match but can be used to swap out the highest frequency
    # numbers, break early if we've found enough of such indices
    for i in range(n):
      if max_freq <= swaps // 2:
        break
        
      if nums1[i] == nums2[i] or nums1[i] == max_freq_val or nums2[i] == max_freq_val:
        continue
      
      cost += i
      swaps += 1
    
    if float(max_freq) > swaps / 2.0:
      return -1
    
    return cost
  