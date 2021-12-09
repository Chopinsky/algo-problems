'''
Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

Example 1:

Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.
Example 2:


Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.
 

Constraints:

1 <= m, n <= 3 * 10^4
1 <= k <= m * n
'''


from typing import Tuple


class Solution:
  def findKthNumber(self, m: int, n: int, k: int) -> int:
    if k == 1:
      return 1
    
    if k == m*n:
      return m*n
    
    def count(val: int) -> Tuple[int, int]:
      cnt, same = 0, 0
      
      for i in range(1, min(val, m)+1):
        cnt += min(n, val // i)
        same += 1 if ((i > 1 and val % i == 0 and (val // i) <= n) or (i == 1 and val <= n)) else 0
        
      return (cnt, cnt-same)
    
    # print(count(320), count(312))
    if m > n:
      m, n = n, m
      
    l, r = 1, m*n
    
    while l < r:
      mid = (l + r) // 2
      total, before = count(mid)
      # print(mid, total, before)
      
      if total >= k and before < k:
        return mid
      
      if before >= k:
        r = mid - 1
      elif total < k:
        l = mid + 1
        
    # print('out', l, count(l))
    return l
  