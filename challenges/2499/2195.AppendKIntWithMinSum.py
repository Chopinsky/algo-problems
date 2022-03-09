'''
You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.

Example 1:

Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.
Example 2:

Input: nums = [5,6], k = 6
Output: 25
Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum. 
The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^8
'''


from typing import List


class Solution:
  def minimalKSum(self, nums: List[int], k: int) -> int:
    un = sorted(set(nums))
    idx = 0
    sums = 0
    # print(un)

    if un[0] > 1:
      l, r = 1, un[0]-1
      cnt = r-l+1
      if k <= cnt:
        r = l+k-1
        sums += (l+r) * k // 2
      else:
        sums += (l+r) * cnt // 2
        
      k -= cnt
    
    # print('init', k)
    while idx < len(un) and k > 0:
      # print('iter', idx, un[idx])
      if idx == len(un) - 1:
        l = un[idx] + 1
        r = l + k - 1
        sums += (l+r) * k // 2
        break
      
      l, r = un[idx]+1, un[idx+1]-1
      if l > r:
        idx += 1
        continue
        
      cnt = r-l+1
      if k <= cnt:
        r = l+k-1
        sums += (l+r) * k // 2
        break
        
      # print('iter', l, r, cnt, k)
      sums += (l+r) * cnt // 2
      k -= cnt
      idx += 1
    
    return sums
    