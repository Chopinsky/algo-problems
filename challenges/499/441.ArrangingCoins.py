'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:

1 <= n <= 2 ** 31 - 1
'''

class Solution:
  def arrangeCoins(self, n: int) -> int:
    # boundary condition:
    # ((1+8n) ** 0.5 - 1) / 2 > m > ((5+8n)**0.5 - 3) / 2
    return (int)((2*n + 0.25) ** 0.5 - 0.5)

  def arrangeCoins1(self, n: int) -> int:
    if n <= 2:
      return 1

    l, r = 1, n+1

    while l < r:
      m = (l+r)//2
      num = m*(m+1)//2

      if num > n:
        r = m-1
        continue

      if n-num <= m+1:
        # print("matching:", n, m, num)
        return m+1 if (n-num == m+1) else m

      l = m+1

    # print("out:", n, l, l*(l+1)//2)
    return l
