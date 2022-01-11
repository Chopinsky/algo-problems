'''
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.

Constraints:

1 <= k <= 10^5
'''


class Solution:
  def smallestRepunitDivByK(self, k: int) -> int:
    if k == 1:
      return 1
    
    base = 1
    digits = 1
    
    while base < k:
      base = 10*base + 1
      digits += 1
      
    # print(base)
    if base == k:
      return digits
    
    base %= k
    ten_mod = 10 % k
    seen = set()
    
    while base != 0 and base not in seen:
      seen.add(base)
      base = ((base * ten_mod) % k + 1) % k
      digits += 1
      
    return digits if base == 0 else -1
  