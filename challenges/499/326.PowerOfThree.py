'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

Input: n = 27
Output: true

Example 2:

Input: n = 0
Output: false

Example 3:

Input: n = 9
Output: true

Example 4:

Input: n = 45
Output: false

Constraints:

-2 ** 31 <= n <= 2 ** 31 - 1

'''


class Solution:
  def isPowerOfThree1(self, n: int) -> bool:
    # 1162261467 is 3 ** 19, which is the only 3 ** n number that is smaller than 2 ** 31 - 1,
    # and any 3 ** n number will be a factor of this top number, but not any other numbers.
    return n > 0 and 1162261467 % n == 0


  def isPowerOfThree(self, n: int) -> bool:
    while n > 0:
      if n == 1:
        return True

      if n < 1 or n % 3 != 0:
        return False

      n /= 3
