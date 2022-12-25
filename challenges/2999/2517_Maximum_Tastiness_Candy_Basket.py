'''
2517. Maximum Tastiness of Candy Basket

You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

Return the maximum tastiness of a candy basket.

Example 1:

Input: price = [13,5,1,8,21,2], k = 3
Output: 8
Explanation: Choose the candies with the prices [13,5,21].
The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.
Example 2:

Input: price = [1,3,1], k = 2
Output: 2
Explanation: Choose the candies with the prices [1,3].
The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum tastiness that can be achieved.
Example 3:

Input: price = [7,7,7,7], k = 2
Output: 0
Explanation: Choosing any two distinct candies from the candies we have will result in a tastiness of 0.

Constraints:

1 <= price.length <= 10^5
1 <= price[i] <= 10^9
2 <= k <= price.length
'''

from typing import List


class Solution:
  def maximumTastiness(self, price: List[int], k: int) -> int:
    n = len(price)
    if n == 1:
      return 0
      
    price.sort()
    diff = [(price[i]-price[i-1]) for i in range(1, n)]
    # print(price, diff)
    
    def can_pick(val: int) -> bool:
      cnt = 0
      curr = 0
      
      for i in range(len(diff)):
        curr += diff[i]
        if curr >= val:
          cnt += 1
          curr = 0
          
        if cnt >= k-1:
          # print('pick:', val, cnt)
          return True
      
      return False
    
    score = -1
    l, r = min(diff), price[-1]
    
    while l < r:
      m = (l + r) // 2
      # print(m, l, r)
      
      if can_pick(m):
        score = m
        l = m+1
      else:
        r = m-1
      
    if can_pick(l):
      score = max(score, l)
      
    return score
    