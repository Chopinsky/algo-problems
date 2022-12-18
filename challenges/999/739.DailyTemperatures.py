'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
'''

from typing import List


class Solution:
  def dailyTemperatures(self, temp: List[int]) -> List[int]:
    stack = []
    temp = temp[::-1]
    ans = []
    # print(temp)
    
    for i in (range(len(temp))):
      val = temp[i]
      while stack and stack[-1][0] <= val:
        stack.pop()
        
      ans.append(0 if not stack else i-stack[-1][1])
      stack.append((val, i))
      # print(val, stack, ans[-1])
      
    return ans[::-1]


  def dailyTemperatures(self, temp: List[int]) -> List[int]:
    n = len(temp)
    ans = [0] * n
    stack = [(temp[-1], n-1)]
    
    for i in range(n-2, -1, -1):
      t0 = temp[i]
      while stack and stack[-1][0] <= t0:
        stack.pop()
        
      if stack:
        ans[i] = stack[-1][1] - i
        
      stack.append((t0, i))
      
    return ans
  
