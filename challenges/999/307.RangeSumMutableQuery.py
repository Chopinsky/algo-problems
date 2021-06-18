'''
Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
'''

from typing import List

class NumArray:
  def __init__(self, nums: List[int]):
    n = len(nums)
    self.fenwick = [0] * (n+1)
    self.nums = nums
    
    for i, n in enumerate(nums):
      self.f_update(i, n, True)
    

  def update(self, idx: int, val: int) -> None:
    return self.f_update(idx, val, False)
    
    
  def f_update(self, idx: int, val: int, init: bool) -> None:
    if not init:
      diff = val - self.nums[idx]
      self.nums[idx] = val
    else:
      diff = val
    
    idx += 1
    
    while idx < len(self.fenwick):
      self.fenwick[idx] += diff
      idx += (idx & -idx)
    

  def sumRange(self, left: int, right: int) -> int:
    return self.presum(right) - self.presum(left-1)
  
  
  def presum(self, idx: int) -> int:
    s = 0
    idx += 1
    
    while idx > 0:
      s += self.fenwick[idx]
      idx -= (idx & -idx)
    
    return s

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)