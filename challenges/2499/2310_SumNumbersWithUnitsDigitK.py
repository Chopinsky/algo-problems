'''
2310. Sum of Numbers With Units Digit K

Given two integers num and k, consider a set of positive integers with the following properties:

The units digit of each integer is k.
The sum of the integers is num.
Return the minimum possible size of such a set, or -1 if no such set exists.

Note:

The set can contain multiple instances of the same integer, and the sum of an empty set is considered 0.
The units digit of a number is the rightmost digit of the number.
 

Example 1:

Input: num = 58, k = 9
Output: 2
Explanation:
One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
Another valid set is [19,39].
It can be shown that 2 is the minimum possible size of a valid set.
Example 2:

Input: num = 37, k = 2
Output: -1
Explanation: It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.
Example 3:

Input: num = 0, k = 7
Output: 0
Explanation: The sum of an empty set is considered 0.

Constraints:

0 <= num <= 3000
0 <= k <= 9
'''

from bisect import bisect_right
from functools import lru_cache
import math


class Solution:
  '''
  the trick is that we can always find a number with unit digit as `k` 
  as long as (num - c * k) % 10 == 0, i.e., we can round up the unit digit
  to match that of the target number
  '''
  def minimumNumbers(self, num: int, k: int) -> int:
    if num == 0:
      return 0

    if k == 0:
      return 1 if num % 10 == 0 else -1

    for cnt in range(1, min(num//k, 10) + 1):
      if (num - cnt*k) % 10 == 0:
        return cnt

    return -1
      
      
  def minimumNumbers0(self, num: int, k: int) -> int:
    # empty set
    if num == 0:
      return 0
    
    # the num alone in the set will make it
    if num % 10 == k:
      return 1
    
    cand = []
    base = k
    
    while base <= num:
      if base > 0:
        cand.append(base)
        
      base += 10
    
    # print(cand)
    
    @lru_cache(None)
    def dp(target: int, i: int) -> int:
      if target == 0:
        return 0
      
      if target < 0 or i < 0:
        return math.inf
      
      # print(target, i, cand[i] if i < len(cand) else 'NaN')
      val = cand[i]
      
      if target < val:
        j = bisect_right(cand, target)-1
        return dp(target, j)
      
      upper = target // val
      if target % val == 0:
        return upper
      
      min_cnt = dp(target, i-1)
      # print('base case:', target, val, min_cnt)
      
      for cnt in range(upper, 0, -1):
        nxt_target = target - cnt*val
        j = bisect_right(cand, nxt_target)-1        
        # print('before:', target, val, cnt, nxt_target, j)
        
        if j < 0:
          continue

        nxt_cnt = dp(nxt_target, j)
        if nxt_cnt != math.inf:
          min_cnt = min(min_cnt, cnt+nxt_cnt)
          if cnt + nxt_cnt > min_cnt:
            break
        
      return min_cnt
    
    c = dp(num, len(cand)-1)
    return c if c != math.inf else -1
    