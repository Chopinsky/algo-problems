'''
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
Example 2:

Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01
Example 3:

Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01

Constraints:

1 <= n <= 30
1 <= k <= 2^(n - 1)
'''


class Solution:
  def kthGrammar(self, n: int, k: int) -> int:
    curr = 0
    k -= 1
    d = []
    
    while k > 0:
      d.append(k&1)
      k >>= 1
    
    if len(d) < n-1:
      d = [0] * (n-1-len(d)) + d
      
    d.reverse()
    # print(d)
    
    for i in range(n-1):
      if d[i] == 1:
        curr = 1 - curr
    
    return curr
  