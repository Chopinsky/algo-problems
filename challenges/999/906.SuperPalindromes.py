from math import ceil, floor, sqrt
from py_math import is_palin

'''
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

Example 2:

Input: left = "1", right = "2"
Output: 1

Constraints:

1 <= left.length, right.length <= 18
left and right consist of only digits.
left and right cannot have leading zeros.
left and right represent integers in the range [1, 1018].
left is less than or equal to right.
'''

class Solution:
  '''
  The idea is to generate palindrome number first, and check if it's square
  is also a palindrom in the range.

  We then check all numbers whose generated palindrom number's square will
  fall into the range. The genearted numbers can have even or odd digits,
  depending on if we want the odd mirroring or even mirroring.

  This way, we will skip all the non-panlindrom numbers from the first place.
  '''
  def superpalindromesInRange(self, left: str, right: str) -> int:
    lnum, rnum = int(left), int(right)
    low, high = floor(sqrt(lnum)), ceil(sqrt(rnum))
    lstr, hstr = str(low), str(high)

    lb_raw, ub_raw = max(0, (len(lstr)+1)//2), (len(hstr)+1)//2
    lb, ub = int('1' + '0' * (lb_raw-1)), min(100000, int('1' + '0' * ub_raw))
    count = 0

    for k in range(lb, ub+1):
      base = str(k)
      rev = base[::-1]

      # check even mirror -- '120' to '120012'
      tgt = int(base + rev) ** 2
      if lnum <= tgt <= rnum and is_palin(tgt):
        count += 1

      # check odd mirror -- '120' to '12012'
      tgt = k*k if k < 10 else int(base + rev[1:]) ** 2
      if lnum <= tgt <= rnum and is_palin(tgt):
        count += 1

      if tgt > rnum:
        break

    return count
