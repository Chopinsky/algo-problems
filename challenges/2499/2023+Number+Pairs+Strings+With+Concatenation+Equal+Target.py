'''
2023. Number of Pairs of Strings With Concatenation Equal to Target

Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

Example 1:

Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"
Example 2:

Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"
Example 3:

Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"

Constraints:

2 <= nums.length <= 100
1 <= nums[i].length <= 100
2 <= target.length <= 100
nums[i] and target consist of digits.
nums[i] and target do not have leading zeros.
'''

from typing import List
from collections import defaultdict


class Solution:
  def numOfPairs(self, nums: List[str], target: str) -> int:
    store = defaultdict(int)
    for val in nums:
      store[val] += 1
      
    cnt = 0
    n = len(target)
    
    for v0, c0 in store.items():
      ln = len(v0)
      
      if (ln >= n) or (not target.startswith(v0)):
        continue

      if v0+v0 == target:
        cnt += c0*(c0-1)
        continue
        
      pair = target[ln:]
      if pair not in store:
        continue
        
      # print('found:')
      cnt += c0 * store[pair]
    
    return cnt
    