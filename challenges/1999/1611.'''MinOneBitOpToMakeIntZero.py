'''
Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

Example 1:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
Example 2:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.

Constraints:

0 <= n <= 10^9
'''


from functools import lru_cache


class Solution:
  '''
  1XXXXXX -> 1100000 -> 100000 -> 0

  1XXXXXX -> 1100000 needs minimumOneBitOperations(1XXXXXX ^ 1100000),
  because it needs same operations 1XXXXXX ^ 1100000 -> 1100000 ^ 1100000 = 0.

  1100000 -> 100000 needs 1 operation.
  100000 -> 0, where 100000 is 2^k, needs 2^(k+1) - 1 operations.

  In total,
  f(n) = f((b >> 1) ^ b ^ n) + 1 + b - 1,
  where b is the maximum power of 2 that small or equals to n.
  '''
  def minimumOneBitOperations(self, n: int) -> int:
    @lru_cache(None)
    def min_op(n: int) -> int:
      if n <= 1:
        return n
      
      base = 1
      while (base << 1) <= n:
        base <<= 1
        
      return min_op(n ^ (base | (base >> 1))) + base
      
    return min_op(n)
  