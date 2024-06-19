'''
3153. Sum of Digit Differences of All Pairs

You are given an array nums consisting of positive integers where all integers have the same number of digits.

The digit difference between two integers is the count of different digits that are in the same position in the two integers.

Return the sum of the digit differences between all pairs of integers in nums.

Example 1:

Input: nums = [13,23,12]

Output: 4

Explanation:
We have the following:
- The digit difference between 13 and 23 is 1.
- The digit difference between 13 and 12 is 1.
- The digit difference between 23 and 12 is 2.
So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.

Example 2:

Input: nums = [10,10,10,10]

Output: 0

Explanation:
All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] < 10^9
All integers in nums have the same number of digits.
'''

from typing import List

class Solution:
  def sumDigitDifferences(self, nums: List[int]) -> int:
    def calc_digits(val: int):
      d = 0
      
      while val > 0:
        d += 1
        val //= 10
      
      return d
    
    digits = calc_digits(nums[0])
    counts = [[0]*10 for _ in range(digits)]
    diff_sum = 0
    # print(digits, counts)
    
    def count_diff(val: int, prev: int):
      pos = 0
      c = 0
      
      while val > 0:
        num = val%10    
        c += prev - counts[pos][num]
        counts[pos][num] += 1
        val //= 10
        pos += 1
      
      return c
    
    for i in range(len(nums)):
      diff_sum += count_diff(nums[i], i)
      
    return diff_sum
        