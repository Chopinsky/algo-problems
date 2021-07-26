'''
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

Example 1:

Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 

Example 2:

Input: n = 1
Output: 2

Example 3:

Input: n = 2
Output: 3

Constraints:

1 <= n <= 10 ** 9
'''


class Solution:
  '''
  '''
  def findIntegers(self, n: int) -> int:
    if n <= 3:
      return 3 if n == 3 else n+1
    
    presum = [2, 3]
    ones = []
    pos = 0
    
    while n > 0:
      if n&1 > 0:
        ones.append(pos)
        
      pos += 1
      n >>= 1
    
    while len(presum) <= ones[-1]:
      presum.append(presum[-1] + presum[-2])
    
    if len(ones) == 1:
      return presum[-2] + 1

    # print("-------")
    # print(ones)
    # print(presum)
    
    ans = 0
    
    for i in range(len(ones)-1, -1, -1):
      if ones[i] >= 1:
        ans += presum[ones[i]-1]
      else:
        ans += 1
        
      if i < len(ones)-1 and ones[i] == ones[i+1]-1:
        break
        
      if i == 0:
        ans += 1
    
    return ans
    