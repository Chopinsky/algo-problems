'''
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1

Constraints:

0 <= n <= 8
'''

from math import comb, factorial


class Solution:
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    if n == 0:
      return 1
    
    cnt = 10
    for ln in range(2, n+1):
      for _ in range(1, 10):
        cnt += comb(9, ln-1) * factorial(ln-1)

    return cnt
    