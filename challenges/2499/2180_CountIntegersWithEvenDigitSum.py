'''
2180. Count Integers With Even Digit Sum

Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.

Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

Constraints:

1 <= num <= 1000
'''


class Solution:
  def countEven(self, num: int) -> int:
    count = (8 if num >= 10 else num) // 2
    odd = set([1, 3, 5, 7, 9])
    # print(count)
    
    for val in range(11, num+1):
      odd_cnt = 0
      while val > 0:
        if val % 10 in odd:
          odd_cnt += 1
          
        val //= 10
        
      if odd_cnt % 2 == 0:
        # print(val)
        count += 1
      
    return count
    
    