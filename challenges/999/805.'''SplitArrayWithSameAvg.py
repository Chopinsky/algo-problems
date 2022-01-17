'''
You are given an integer array nums.

You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).

Return true if it is possible to achieve that and false otherwise.

Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.

Example 1:

Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
Example 2:

Input: nums = [3,1]
Output: false

Constraints:

1 <= nums.length <= 30
0 <= nums[i] <= 10^4
'''


from typing import List
from functools import lru_cache


class Solution:
  '''
  the trick is that for 2 subseq to have the same average, that average will 
  need to be the average of the entire array as well, hence:
      s/n == (sum0+sum1) / (cnt0+cnt1) == sum0/cnt0 == sum1/cnt1
  the problem is essentially asking for the subseq size of k, if the sum of the
  subseq which equals to `s * k // n` can be constructed using k elements from
  the array.
  '''
  def splitArraySameAverage(self, nums: List[int]) -> bool:
    n = len(nums)
    s = sum(nums)
    
    # check if there is a subseq starting from `i`-th element, 
    # that has a total of `k` elements and it can add up to `target`
    @lru_cache(None)
    def find(target: int, k: int, i: int) -> bool:
      # endgame
      if k == 0:
        return target == 0
      
      # invalid cases: negative sum or the remainder
      # elements won't meet the `k`-length requirement
      if target < 0 or k > n-i:
        return False
      
      # if use i-th number to find the target, or don't use it
      return find(target-nums[i], k-1, i+1) or find(target, k, i+1)
      
    # k is the size of the shorter array, which is at most the size
    # of `n//2 + 1`
    for k in range(1, n//2+1):
      # if sum0/cnt0 == sum1/cnt1, then (sum0+sum1)/(cnt0+cnt1) == sum0/cnt0 == s/n,
      # hence ((sum0+sum1) * cnt0) / (cnt0+cnt1) must be an integer
      if (s * k) % n != 0:
        continue
        
      if find(s*k//n, k, 0):
        return True
      
    return False
