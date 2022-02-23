'''
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
 

Constraints:

1 <= inventory.length <= 10^5
1 <= inventory[i] <= 10^9
1 <= orders <= min(sum(inventory[i]), 10^9)
'''


from typing import List


class Solution:
  '''
  take a batch out each time when we still have orders to fill
  '''
  def maxProfit(self, inv: List[int], orders: int) -> int:
    inv.sort()
    inv.insert(0, 0)
    
    profit = 0
    width = 1
    mod = 10**9 + 7
    
    for i in range(len(inv)-1, 0, -1):
      if inv[i] > inv[i-1]:
        # take `width * (inv[i]-inv[i-1])` more balls out of the inventory
        if width * (inv[i] - inv[i-1]) <= orders:
          add_sum = width * ((inv[i-1] + 1 + inv[i]) * (inv[i] - inv[i-1]) // 2)
          profit = (profit + add_sum) % mod
          orders -= width * (inv[i] - inv[i-1])
          
        # endgame, add those that can be stacked, and add the remainders
        else:
          whole, remaining = divmod(orders, width)
          whole_sales = width * ((inv[i] - whole + 1 + inv[i]) * whole // 2)
          remaining_sales = remaining * (inv[i] - whole)
          profit = (profit + whole_sales + remaining_sales) % mod
          
          break
              
      width += 1
        
    return profit
      
  
  '''
  guess where the height is, then calculate the total profit
  '''
  def maxProfit0(self, inv: List[int], orders: int) -> int:
    mod = 10**9 + 7
    if len(inv) == 1:
      cnt = inv[0]
      total = (cnt + (cnt-orders+1)) * orders // 2
      return total % mod

    inv_sum = sum(inv)
    if inv_sum == orders:
      for cnt in inv:
        total = (total + (cnt+1)*cnt//2) % mod
        
      return total
      
    inv.sort(reverse=True)
    n = len(inv)
    total = 0
    l, r = 1, inv[0]
    last = 1
    
    while l < r:
      m = (l + r) // 2
      # print(l, m, r)
      
      if sum(val-m+1 if val >= m else 0 for val in inv) >= orders:
        l = m + 1
        last = m
      else:
        r = m - 1
    
    if sum(val-l+1 if val >= l else 0 for val in inv) >= orders:
      last = l
    
    # print(inv_sum, last, l)
    for i in range(n):
      val = inv[i]
      if val < last:
        break
        
      total += (val + last) * (val-last+1) // 2
      orders -= val-last+1
    
    # print(total, orders)
    total += orders * last
    
    return total % mod
  