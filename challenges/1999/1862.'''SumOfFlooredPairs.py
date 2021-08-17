'''
Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.

The floor() function returns the integer part of the division.

Example 1:

Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.

Example 2:

Input: nums = [7,7,7,7,7,7,7]
Output: 49
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''


from typing import List
from collections import Counter
from itertools import accumulate
from bisect import bisect_right


class Solution:
  def sumOfFlooredPairs(self, nums: List[int]) -> int:
    sums = 0
    mod = 10 ** 9 + 7
    
    counter = Counter(nums)
    top = max(nums)
    multiples = [0] * (top+1)
    
    for n, c in counter.items():
      for m in range(n, top+1, n):
        multiples[m] += c
        
    # prefix holds the count of multiples of numbers in the number array, 
    # say for array [2,5,9], at number 6, it holds (1x2, 2x2, 2x3, 5x1), 
    # meaning for 6, we have 6/2 = 3, and 6/5 = 1, sum is 4.
    prefix = list(accumulate(multiples))
    # print(prefix)
    
    # then we just add up the sum of floors:
    #    sum@n_i = sum(n_i/n_i, n_i/n_i-1, n_i/n_i-2, ..., n_i/n0)
    # which equals prefix[n_i]
    for num in nums:
      sums += prefix[num]
    
    return sums % mod 
    
  def sumOfFlooredPairs0(self, nums: List[int]) -> int:
    nums.sort()
    
    counter = Counter(nums)
    num_list = []
    last = 0
    
    for k in sorted(counter.keys()):
      curr = last + counter[k]
      num_list.append((k, curr))
      last = curr
    
    # print(counter, num_list)
    
    sums = 0
    for n, c in num_list:
      if n == 1:
        for n0, _ in num_list:
          sums += n0 * counter[n0] * counter[1]
          
        continue

      sums += counter[n] * counter[n]
      if n == num_list[-1][0]:
        continue
      
      f = 2
      last = c
      
      while n*(f-1) <= num_list[-1][0]:
        loc = bisect_right(num_list, (n*f,)) - 1
        
        # no numbers in between (n-1)*factor and n*factor-1
        if loc < 0 or num_list[loc][0] <= n:
          f += 1
          continue
          
        # print(n, sums, f-1, counter[n], num_list[loc][1]-last)
        
        sums += (f-1) * counter[n] * (num_list[loc][1]-last) % (10 ** 9 + 7)
        last = num_list[loc][1] 
        f += 1
    
    return sums % (10 ** 9 + 7)
    