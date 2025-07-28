'''
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

Example 1:

Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

Example 2:

Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.

Example 3:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
 

Constraints:

1 <= nums.length <= 16
1 <= nums[i] <= 10^5
'''

from typing import List
from collections import defaultdict, Counter


class Solution:
  def countMaxOrSubsets(self, nums: List[int]) -> int:
    curr = defaultdict(int)

    for v0 in nums:
      nxt = curr.copy()
      nxt[v0] += 1

      for v1, c1 in curr.items():
        nxt[v0|v1] += c1

      curr = nxt

    top = max(curr)
    print('done:', top, curr)

    return curr[top]
        
  def countMaxOrSubsets(self, nums: List[int]) -> int:
    counter, nxt = defaultdict(int), defaultdict(int)
    c = Counter(nums)
    
    for val in c:
      base = (1 << c[val]) - 1
      nxt[val] += base
      # print(val, base, counter)
      
      # build all subsets with val
      for vs, cnt in counter.items():
        nxt[val|vs] += base * cnt
        
      # merge results
      for vs, cnt in nxt.items():
        counter[vs] += cnt
        
      nxt.clear()
      
    # print(counter)
    return counter[max(counter)]

  def countMaxOrSubsets(self, nums: List[int]) -> int:
    n = len(nums)
    
    def nums_or(mask: int):
      pos = 1
      idx = 0
      val = 0
      
      while pos <= mask:
        if pos & mask > 0:
          val |= nums[idx]
          
        pos <<= 1
        idx += 1
        
      return val
    
    count = 0
    max_val = nums_or((1<<n)-1)
    # print('init:', max_val)
    
    for mask in range(1, (1<<n)):
      res = nums_or(mask)
      if res == max_val:
        count += 1
        
    return count
        