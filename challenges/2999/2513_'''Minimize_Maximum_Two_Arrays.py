'''
2513. Minimize the Maximum of Two Arrays

We have two arrays arr1 and arr2 which are initially empty. You need to add positive integers to them such that they satisfy all the following conditions:

arr1 contains uniqueCnt1 distinct positive integers, each of which is not divisible by divisor1.
arr2 contains uniqueCnt2 distinct positive integers, each of which is not divisible by divisor2.
No integer is present in both arr1 and arr2.
Given divisor1, divisor2, uniqueCnt1, and uniqueCnt2, return the minimum possible maximum integer that can be present in either array.

Example 1:

Input: divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3
Output: 4
Explanation: 
We can distribute the first 4 natural numbers into arr1 and arr2.
arr1 = [1] and arr2 = [2,3,4].
We can see that both arrays satisfy all the conditions.
Since the maximum value is 4, we return it.
Example 2:

Input: divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1
Output: 3
Explanation: 
Here arr1 = [1,2], and arr2 = [3] satisfy all conditions.
Since the maximum value is 3, we return it.
Example 3:

Input: divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2
Output: 15
Explanation: 
Here, the final possible arrays can be arr1 = [1,3,5,7,9,11,13,15], and arr2 = [2,6].
It can be shown that it is not possible to obtain a lower maximum satisfying all conditions. 

Constraints:

2 <= divisor1, divisor2 <= 10^5
1 <= uniqueCnt1, uniqueCnt2 < 10^9
2 <= uniqueCnt1 + uniqueCnt2 <= 10^9
'''

from math import gcd


class Solution:
  '''
  idea is to guess the number that will satisfy the conditions: we will 
  exclude all numbers divisible to LCM(d1, d2), and numbers divisible to d1 from
  array1, and then numbers divisivble to d2 from array2; then we can check
  if this gives us a number satisfying all other conditions
  '''
  def minimizeSet(self, d1: int, d2: int, c1: int, c2: int) -> int:
    lcm = d1*d2//gcd(d1, d2)
    # print(lcm)    
    l, r = 0, 10**32
    
    while l+1 < r:
      mid = (l+r) // 2
      total = mid - mid//lcm
      ac = mid - mid//d1
      bc = mid - mid//d2
      
      if total >= c1+c2 and ac >= c1 and bc >= c2:
        # mid is a value satisfying the requirements
        r = mid
      else:
        # moving to the right subregion
        l = mid
        
    return r
  