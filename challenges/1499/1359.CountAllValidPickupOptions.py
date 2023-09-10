'''
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90

Constraints:

1 <= n <= 500
'''


from functools import lru_cache
from math import comb


class Solution:
  def countOrders(self, n: int) -> int:
    mod = 10**9 + 7
    res = 1
    
    # pick 1 p/d pair from i-counts of the choices, then
    # place the p service at the front, and choose 2*i-1 
    # positions for the d service
    for i in range(2, n+1):
      res = (res * i * (2*i-1)) % mod
    
    return res


  def countOrders(self, n: int) -> int:
    mod = 10**9+7
    
    @lru_cache(None)
    def dp(n: int) -> int:
      if n == 1:
        return 1
      
      return (comb(2*n,2) * dp(n-1)) % mod
      
    return dp(n)
  