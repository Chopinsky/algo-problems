'''
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

Constraints:

1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length
'''

from typing import List


class Solution:
  def totalFruit(self, fruits: List[int]) -> int:
    first, second = -1, -1
    second_count = 0
    run_count = 0
    total_count = 0
    idx = 0
    n = len(fruits)
    
    # initial scan
    while idx < n:
      fruit_type = fruits[idx]
      
      if first < 0 or fruit_type == first:
        # add to the 1st basket, but swap orders
        if second >= 0:
          first, second = second, first
          second_count = 1
          
        # add the 1st fruit to the 1st basket
        else:
          first = fruit_type
          
        run_count += 1
      
      elif second < 0 or fruit_type == second:
        # add to the 2nd basket
        second = fruit_type
        second_count += 1
        run_count += 1
        
      else:
        # reset the orders
        first = second
        second = fruit_type

        # reset the counters
        run_count = second_count+1
        second_count = 1
        
      # print(idx, first, second, second_count, run_count)
      total_count = max(total_count, run_count)
      idx += 1
    
    # print(first, second, total_count)
    return total_count
    