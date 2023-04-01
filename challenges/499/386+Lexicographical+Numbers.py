'''
386. Lexicographical Numbers

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]

Constraints:

1 <= n <= 5 * 10^4
'''

from typing import List


class Solution:
  def lexicalOrder(self, n: int) -> List[int]:
    d = []
    c = 1
    
    for _ in range(n):
      d.append(c)

      if c*10 <= n:
          c *= 10
          
      else:
        if c >= n:
          c //= 10

        c += 1
        while c%10 == 0:
          c //= 10
            
    return d
  

  def lexicalOrder(self, n: int) -> List[int]:
    arr = sorted([str(i+1) for i in range(n)])
    return [int(v) for v in arr]
    