'''
2763. Sum of Imbalance Numbers of All Subarrays

The imbalance number of a 0-indexed integer array arr of length n is defined as the number of indices in sarr = sorted(arr) such that:

0 <= i < n - 1, and
sarr[i+1] - sarr[i] > 1
Here, sorted(arr) is the function that returns the sorted version of arr.

Given a 0-indexed integer array nums, return the sum of imbalance numbers of all its subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,3,1,4]
Output: 3
Explanation: There are 3 subarrays with non-zero imbalance numbers:
- Subarray [3, 1] with an imbalance number of 1.
- Subarray [3, 1, 4] with an imbalance number of 1.
- Subarray [1, 4] with an imbalance number of 1.
The imbalance number of all other subarrays is 0. Hence, the sum of imbalance numbers of all the subarrays of nums is 3. 
Example 2:

Input: nums = [1,3,3,3,5]
Output: 8
Explanation: There are 7 subarrays with non-zero imbalance numbers:
- Subarray [1, 3] with an imbalance number of 1.
- Subarray [1, 3, 3] with an imbalance number of 1.
- Subarray [1, 3, 3, 3] with an imbalance number of 1.
- Subarray [1, 3, 3, 3, 5] with an imbalance number of 2. 
- Subarray [3, 3, 3, 5] with an imbalance number of 1. 
- Subarray [3, 3, 5] with an imbalance number of 1.
- Subarray [3, 5] with an imbalance number of 1.
The imbalance number of all other subarrays is 0. Hence, the sum of imbalance numbers of all the subarrays of nums is 8. 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
'''

from typing import List


class Solution:
  def sumImbalanceNumbers(self, nums: List[int]) -> int:
    total = 0

    for i in range(len(nums)):
      seen = set()
      cnt = 0

      for num in nums[i:]:
        # imbalance count only change if a new number to 
        # the sorted array
        if num not in seen:
          # breaking the (num-1, num+1) pair, -1
          if (num-1 in seen) and (num+1 in seen):
            cnt -= 1

          # this will create a new pair, with either a smaller
          # number, or a larger number, and if both exists, this
          # only adds one new pair
          if seen and (num-1 not in seen) and (num+1 not in seen):
            cnt += 1

          seen.add(num)

        # update the total count of the imbalance count
        total += cnt

    return total
      
      
  def sumImbalanceNumbers0(self, nums: List[int]) -> int:
    top = max(nums)
    n = len(nums)
    
    def add(g, val):
      if val == 0:
        g[val] += 1
        return
      
      while val < len(g):
        g[val] += 1
        val += (val & -val)
        
    def query(g, val):
      if val < 0:
        return 0
      
      res = g[0]
      while val > 0:
        res += g[val]
        val -= (val & -val)
        
      return res
    
    def pos(g, val):
      curr = query(g, val)
      if val == 0:
        return curr
      
      prev = query(g, val-1)
      return curr - prev
    
    def change(g, val):
      curr = pos(g, val)
      if curr > 0:
        return 0

      left = pos(g, val-1) if val > 0 else 0
      right = pos(g, val+1) if val < top else 0
      
      if left != right and (left == 0 or right == 0):
        return 0
      
      ll = query(g, val-2) if val > 1 else 0

      # right-most position
      if val == top:
        return 1 if left == 0 and ll > 0 else 0

      if left == 0 and right == 0:
        rr = query(g, top)-query(g, val+1) if val < top-1 else 0
        return 1 if ll != 0 or rr != 0 else 0

      return -1
    
    def calc(i):
      curr = 0
      cnt = 0
      g = [0] * (top+1)
      curr_max = nums[i]
      
      for j in range(i, n):
        val = nums[j]
        if val >= curr_max:
          if val > curr_max:
            curr += 1 if val-curr_max > 1 else 0
          
          curr_max = val
          
        else:
          # update counter
          c = change(g, val)
          curr += c
          # print('change:', (i, j), val, '->', (c, curr))
        
        # update
        cnt += curr
        add(g, val)
      
      # print('sub:', i, cnt)
      return cnt
      
    total = 0
    for i in range(n-1):
      total += calc(i)
        
    return total
  