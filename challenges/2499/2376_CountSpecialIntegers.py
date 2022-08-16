'''
We call a positive integer special if all of its digits are distinct.

Given a positive integer n, return the number of special integers that belong to the interval [1, n].

Example 1:

Input: n = 20
Output: 19
Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.
Example 2:

Input: n = 5
Output: 5
Explanation: All the integers from 1 to 5 are special.
Example 3:

Input: n = 135
Output: 110
Explanation: There are 110 integers from 1 to 135 that are special.
Some of the integers that are not special are: 22, 114, and 131.

Constraints:

1 <= n <= 2 * 10^9
'''

from functools import lru_cache
from math import comb, factorial


class Solution:
  def countSpecialNumbers(self, n: int) -> int:
    count = 0
    if n < 11:
      return n
    
    digits = []
    while n > 0:
      digits.append(n % 10)
      n //= 10
      
    digits.reverse()
    ln = len(digits)
    seen = set()
    base = set(i for i in range(10))
    # print(digits)
    
    @lru_cache(None)
    def full_count(d: int) -> int:
      if d == 1:
        return 9
      
      return 9 * comb(9, d-1) * factorial(d-1)
    
    # get all special integers with less digit counts
    for i in range(1, ln):
      count += full_count(i)
    
    # going through each digit to get smaller numbers
    # that are `ln` in length and special
    for i in range(ln):
      # last digit, get the tail count (including the number itself
      # if it's also special)
      if i == ln-1:
        count += len(set(i for i in range(digits[i]+1)) - seen)
        continue
      
      # calc the smaller and special numbers with the same
      # leading digits up to index-(i-1)
      for j in range(0 if i > 0 else 1, digits[i]):
        if j in seen:
          continue

        # `rem` is the number of candidate digits, `dc` is the
        # number of slots we need to fill
        rem = len(base - seen - {j})
        dc = ln - i - 1
        # print(j, rem, dc)

        # we can take `dc` of digits out of `rem` candidates,
        # and place them in all possible combinations
        if dc > 0 and rem >= dc:
          count += comb(rem, dc) * factorial(dc)
      
      # no need to countinue the drill down as we've
      # a repeating digit in the higher levels
      if digits[i] in seen:
        break
      
      seen.add(digits[i])
    
    return count
    