'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:

1 <= n <= 1690
'''

from bisect import bisect_right

class Solution:
  def nthUglyNumber(self, n: int) -> int:
    nums = [1]
    x, y, z = 0, 0, 0
    
    for i in range(n-1):
      minimum = min(nums[x]*2, nums[y]*3, nums[z]*5)
      nums.append(minimum)
      
      if minimum == nums[x]*2:
        x += 1
        
      if minimum == nums[y]*3:
        y += 1
        
      if minimum == nums[z]*5:
        z += 1
        
    return nums[-1]
        

  def nthUglyNumber(self, n: int) -> int:
    if n <= 6:
      return n
    
    cnt = 3
    lst = [1,2,3,4,5]
    
    two = 2
    three = 1
    five = 1
    
    while cnt < n:
      m = min(2*two, 3*three, 5*five)
      lst.append(m)
      
      # print(cnt, m, two, three, five)
      
      if m == 2*two:
        i2 = bisect_right(lst, two)
        two = lst[i2]
        
      if m == 3*three:
        i3 = bisect_right(lst, three)
        three = lst[i3]
        
      if m == 5*five:
        i5 = bisect_right(lst, five)
        five = lst[i5]
      
      cnt += 1
      
    return min(2*two, 3*three, 5*five)
  