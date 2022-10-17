'''
2443. Sum of Number and Its Reverse

Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.

Example 1:

Input: num = 443
Output: true
Explanation: 172 + 271 = 443 so we return true.
Example 2:

Input: num = 63
Output: false
Explanation: 63 cannot be expressed as the sum of a non-negative integer and its reverse so we return false.
Example 3:

Input: num = 181
Output: true
Explanation: 140 + 041 = 181 so we return true. Note that when a number is reversed, there may be leading zeros.

Constraints:

0 <= num <= 10^5
'''


class Solution:
  def sumOfNumberAndReverse(self, num: int) -> bool:
    if num == 0:
      return True
    
    def rev(val: int) -> int:
      d = str(val)[::-1]
      return int(d)
    
    for val in range(num-1, num//2-1, -1):
      val_rev = rev(val)
      if val + val_rev == num:
        # print(val, val_rev)
        return True
      
    return False
    
    