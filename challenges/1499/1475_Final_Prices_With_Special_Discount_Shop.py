'''
1475. Final Prices With a Special Discount in a Shop
'''

from typing import List

class Solution:
  def finalPrices(self, prices: List[int]) -> List[int]:
    ans = []
    n = len(prices)
    
    for i in range(n):
      val = prices[i]
      ans.append(val)
      
      for j in range(i+1, n):
        if prices[j] <= val:
          ans[-1] -= prices[j]
          break
          
    return ans
    
        