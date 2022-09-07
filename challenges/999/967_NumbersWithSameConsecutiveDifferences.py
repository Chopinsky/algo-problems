'''
967. Numbers With Same Consecutive Differences

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Constraints:

2 <= n <= 9
0 <= k <= 9
'''

from typing import List


class Solution:
  def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
    curr, nxt = [i for i in range(1, 10)], list()
    n -= 1
    
    while n > 0:
      for num in curr:
        tail = num % 10
        low, high = tail-k, tail+k
        
        if low >= 0:
          nxt.append(10*num + low)
          
        if high < 10 and high != low:
          nxt.append(10*num + high)
        
      n -= 1
      curr, nxt = nxt, curr
      nxt.clear()
      
    return curr
  