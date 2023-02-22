'''
2571. Minimum Operations to Reduce an Integer to 0

You are given a positive integer n, you can do the following operation any number of times:

Add or subtract a power of 2 from n.
Return the minimum number of operations to make n equal to 0.

A number x is power of 2 if x == 2i where i >= 0.

Example 1:

Input: n = 39
Output: 3
Explanation: We can do the following operations:
- Add 20 = 1 to n, so now n = 40.
- Subtract 23 = 8 from n, so now n = 32.
- Subtract 25 = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
Example 2:

Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 21 = 2 to n, so now n = 56.
- Add 23 = 8 to n, so now n = 64.
- Subtract 26 = 64 from n, so now n = 0.
So the minimum number of operations is 3.

Constraints:

1 <= n <= 10^5
'''


class Solution:
  def minOperations(self, n: int) -> int:
    bc = list(bin(n)[2:])[::-1]
    # print(bc)
    ops = 0
    idx = 0
    
    while idx < len(bc):
      if bc[idx] == '0':
        idx += 1
        continue
        
      jdx = idx
      cnt = 0
      
      while jdx < len(bc) and bc[jdx] == '1':
        cnt += 1
        jdx += 1
      
      if cnt == 1:
        idx += 1
        continue
        
      # add (1 << idx)
      ops += 1
      while idx < len(bc) and bc[idx] == '1':
        bc[idx] = '0'
        idx += 1

      if idx < len(bc):
        bc[idx] = '1'

      else:
        bc.append('1')
        break
          
    # print('fin:', bc)
    return ops + bc.count('1')
    