'''
2561. Rearranging Fruits

You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.

Example 1:

Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
Example 2:

Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.
 

Constraints:

basket1.length == bakste2.length
1 <= basket1.length <= 10^5
1 <= basket1[i],basket2[i] <= 10^9
'''

from typing import List
from collections import Counter


class Solution:
  def minCost(self, b1: List[int], b2: List[int]) -> int:
    f = Counter(b1+b2)
    f1 = Counter(b1)
    # print(f, f1)
    
    for v in f.values():
      if v % 2 == 1:
        return -1
      
    cost = 0
    move_out, move_in = [], []
    
    for v, c in f.items():
      c //= 2
      curr_cnt = f1.get(v, 0)
      
      if c > curr_cnt:
        move_in.append((v, c-curr_cnt))
        
      # no need to change
      elif c < f1[v]:
        move_out.append((v, curr_cnt-c))
      
    move_out.sort()
    move_in.sort(reverse=True)
    min_val = min(f)
    # print(min_val, move_out, move_in)

    '''
    total_swap_cost = 0
    for v, c in move_in + move_out:
      if v == min_val:
        continue
        
      total_swap_cost += min_val * c  
    '''

    while move_out and move_in:
      v0, c0 = move_out.pop()
      v1, c1 = move_in.pop()
      
      moves = min(c0, c1)
      move_cost = min(v0, v1) * moves
      swap_cost = 2 * min_val * moves
      cost += min(move_cost, swap_cost)
        
      if c0 > moves:
        move_out.append((v0, c0-moves))
        
      if c1 > moves:
        move_in.append((v1, c1-moves))

    return cost

    '''
    # print(cost, swap_cost)
    return min(cost, total_swap_cost)
    '''
    