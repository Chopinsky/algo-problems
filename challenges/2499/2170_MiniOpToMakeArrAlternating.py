'''
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
'''


from typing import List
from collections import Counter


class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
      return 1 if n == 2 and nums[0] == nums[1] else 0
    
    even_cnt = Counter(nums[::2])
    odd_cnt = Counter(nums[1::2])
    et = n//2 + (1 if n%2 == 1 else 0)
    ot = n//2
    
    even = sorted([(cnt, val) for val, cnt in even_cnt.items()], reverse=True)
    odd = sorted([(cnt, val) for val, cnt in odd_cnt.items()], reverse=True)
    # print(even, et, odd, ot)
    
    if even[0][1] != odd[0][1]:
      return (et - even[0][0]) + (ot - odd[0][0])
    
    if len(even) == 1 and len(odd) == 1:
      return min(et, ot)
    
    if len(even) == 1:
      return min(et, ot - odd[1][0])
    
    if len(odd) == 1:
      return min(ot, et - even[1][0])
    
    return min(et-even[0][0]+ot-odd[1][0], ot-odd[0][0]+et-even[1][0])
  