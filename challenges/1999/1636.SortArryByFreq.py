'''
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
'''

from typing import List
from collections import defaultdict, Counter

class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    c = Counter(nums)
    cand = sorted((cnt, -val) for val, cnt in c.items())
    # print(cand)
    res = []
    
    for cnt, val in cand:
      val = -val
      res += [val]*cnt
      
    return res
        
  def frequencySort(self, nums: List[int]) -> List[int]:
    c = defaultdict(int)
    for i in nums:
      c[i] += 1
      
    arr = []
    for n, f in c.items():
      arr.append((f, -n))
      
    arr.sort()
    ans = []
    
    for f, n in arr:
      n = -n
      ans += [n] * f
      
    return ans