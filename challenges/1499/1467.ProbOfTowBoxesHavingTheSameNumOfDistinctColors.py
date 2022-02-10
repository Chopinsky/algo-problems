'''
Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i.

All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

Return the probability that the two boxes have the same number of distinct balls. Answers within 10-5 of the actual value will be accepted as correct.

Example 1:

Input: balls = [1,1]
Output: 1.00000
Explanation: Only 2 ways to divide the balls equally:
- A ball of color 1 to box 1 and a ball of color 2 to box 2
- A ball of color 2 to box 1 and a ball of color 1 to box 2
In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1
Example 2:

Input: balls = [2,1,1]
Output: 0.66667
Explanation: We have the set of balls [1, 1, 2, 3]
This set of balls will be shuffled randomly and we may have one of the 12 distinct shuffles with equal probability (i.e. 1/12):
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
After that, we add the first two balls to the first box and the second two balls to the second box.
We can see that 8 of these 12 possible random distributions have the same number of distinct colors of balls in each box.
Probability is 8/12 = 0.66667
Example 3:

Input: balls = [1,2,1,2]
Output: 0.60000
Explanation: The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all the 180 possible random shuffles of this set but it is easy to check that 108 of them will have the same number of distinct colors in each box.
Probability = 108 / 180 = 0.6

Constraints:

1 <= balls.length <= 8
1 <= balls[i] <= 6
sum(balls) is even.
'''


from typing import List
from math import comb
from functools import lru_cache


class Solution:
  def getProbability(self, balls: List[int]) -> float:
    total = sum(balls)
    n = len(balls)
    base = comb(total, total//2)
    
    # quick query for the number of remainder balls
    prefix = [val for val in balls]
    for i in range(n-2, -1, -1):
      prefix[i] += prefix[i+1]  
    
    # dp: choosing from color-i (and forwrad), with `rem` balls
    #     to put into bucket a, with `a` counts of unique colors
    #     in bucket a, and `b` counts of unique colors in bucket b
    @lru_cache(None)
    def dp(i: int, rem: int, a: int, b: int) -> int:
      # illegal case
      if rem < 0:
        return 0
      
      # all colors visited, check if unique colors are equal
      if i >= n:
        return 1 if (rem == 0 and a == b) else 0
        
      # no more balls for a, remainder balls to b
      if rem == 0:
        b += n - i
        return 1 if (a == b) else 0
      
      # unable to get required number of balls, or to achieve
      # equal unique colors
      if rem > prefix[i] or a+(n-i) < b or b+(n-i) < a:
        return 0
      
      # bucket a needs to take all remainder balls
      if a+(n-i) == b:
        return 1 if rem == prefix[i] else 0
      
      # bucket b needs to take all remainder balls
      if b+(n-i) == a:
        return 1 if rem == 0 else 0
      
      cnt = 0
      for c in range(balls[i]+1):
        if c > rem:
          break
          
        # the color balances when choosing c balls from color-i
        nxt_a = a + (1 if c > 0 else 0)
        nxt_b = b + (1 if c < balls[i] else 0)
        
        # select c balls from color-i, times the remainder choices
        cnt += comb(balls[i], c) * dp(i+1, rem-c, nxt_a, nxt_b)
      
      return cnt
    
    all_combo = dp(0, total//2, 0, 0)
    # print(all_combo, base)
    
    return all_combo / base
    