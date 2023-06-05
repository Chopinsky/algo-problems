'''
2719. Count of Integers

You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. We denote an integer x to be good if:

num1 <= x <= num2
min_sum <= digit_sum(x) <= max_sum.
Return the number of good integers. Since the answer may be large, return it modulo 109 + 7.

Note that digit_sum(x) denotes the sum of the digits of x.

Example 1:

Input: num1 = "1", num2 = "12", min_num = 1, max_num = 8
Output: 11
Explanation: There are 11 integers whose sum of digits lies between 1 and 8 are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.
Example 2:

Input: num1 = "1", num2 = "5", min_num = 1, max_num = 5
Output: 5
Explanation: The 5 integers whose sum of digits lies between 1 and 5 are 1,2,3,4, and 5. Thus, we return 5.

Constraints:

1 <= num1 <= num2 <= 10^22
1 <= min_sum <= max_sum <= 400
'''

from functools import lru_cache


class Solution:
  '''
  the key is to divide the problem into 2 parts:
  1) let `count(top: int)` return the number of values whose digit sums fall in the [min_sum, max_sum]
     range, and with the top value be top; then the problem is equivalent to `count(num2) - count(num1-1)`
  2) to calculate `count(top: int)`, we need to go through each digit-position: for position-j, if all
     previous digits are the top-digit, then we can't go above digit[j] at this position, or we go over
     the top bound; so we check:
       `dp(j+1, running_sums+digit[j], isBounded) + 
        [0..digit[j]-1].reduce(
          init: 0, 
          reducer: (k, prev) => prev+dp(j+1, running_sums+k, notBounded),
        )`
     and for the notBounded iterations, just ignore the 1st part of the equation above, the allowed digits
     for this position are [0, 10).
  '''
  def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
    upper, lower = max_sum, min_sum
    mod = 10**9 + 7
    
    @lru_cache(None)
    def dp(i: int, s: int, bounded: bool, d: str) -> int:
      ln = len(d)
      if i >= ln or s > upper or (s+9*(ln-i)) < lower:
        return 0
      
      val = int(d[i])
      top_digit = val if bounded else 10

      if i == ln-1:
        start = max(0, lower-s)
        end = min(9, top_digit, upper-s)
        return max(0, end-start+1)
      
      count = dp(i+1, s+val, True, d) if bounded else 0
      for v in range(top_digit):
        count = (count + dp(i+1, s+v, False, d)) % mod
        
      return count
    
    # f(num2, min_sum, max_sum)
    c2 = dp(0, 0, True, num2)
    
    # f(num1-1, min_sum, max_sum)
    num1 = str(int(num1) - 1)
    c1 = dp(0, 0, True, num1)
    # print('nums:', (num1, c1), (num2, c2))
    
    return ((c2+mod) - c1) % mod
        